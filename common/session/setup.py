from typing import List, Tuple
import os.path
import requests
import bs4
import re
from time import perf_counter
from rich.console import Console

from .cookie import cookie


class AdventSession:
    def __init__(self, day: int, year: int = 2020):
        """
        A wrapper for a requests ``Session`` object, containing
        the user cookie and retrieved input data. Handles submitting to AOC,
        and caches past submissions.
        """
        self.day = day
        self.year = year
        self.session = requests.Session()
        self.session.cookies.update({'session': cookie})
        self.console = Console(color_system='auto')
        self.data = self.setup_session()
        self.test_data = self.get_test_data()
        self.start_time = perf_counter()

    def setup_session(self) -> str:
        """Creates .in file if it doesn't exist, otherwise reads from it."""
        filename = f'day{self.day}.in'
        if not os.path.exists(filename):  # get data and store into file
            with self.console.status('Retrieving input...'):
                response = self.session.get(
                    f'https://adventofcode.com/{self.year}/day/{self.day}/input'
                )
                data = response.text
                if 'request this endpoint before it unlocks' in data:
                    self.console.print(
                        f'Day [bold]{self.day}[/bold] '
                        f'has not been unlocked yet!'
                    )
                elif response.status_code == 404:  # otherwise, page not found
                    self.console.print(
                        f'[bold red]404[/bold red]: '
                        f'Invalid day (got [bold]{self.day}[/bold]) '
                        f'or year (got [bold]{self.year}[/bold])'
                    )
                else:  # write retrieved input data to file
                    with open(filename, 'w') as input_file:
                        input_file.write(data)
                    self.console.print(f'Retrieved input for day {self.day}!')
        else:
            with self.console.status('Reading input file...'):
                with open(filename, 'r') as input_file:
                    data = input_file.read()
            self.console.print(f'Read input file for day {self.day}!')
        return data

    def get_test_data(self) -> str:
        """Retrieves test data from a .test file, if it exists."""
        if os.path.exists(f'day{self.day}.test'):
            with open(f'day{self.day}.test', 'r') as test_file:
                data = test_file.read()
            return data

    def submit(self, answer, part: int) -> str:
        """
        Submits an answer, but asks for confirmation before sending.
        Parses the http response and notifies the user as needed.
        Tracks past submissions to reduce errors.

        :param answer: the answer to submit
        :param part: the part of the question to submit for
        :return: raw content of the response
        """
        self.console.print(f'Submitting [yellow bold]{answer}[/yellow bold] '
                           f'for part {part}...')
        answer_list, response_list = self.parse_past_submissions(part)
        if 'right' in response_list:
            idx = response_list.index('right')
            right_answer = answer_list[idx]
            postfix = '(This guess is [red]incorrect[/red])'
            if str(answer) == str(right_answer):
                postfix = '(This guess is [green]correct[/green])'
            self.console.print(
                f'Part {part} was already submitted with the right answer of '
                f'[bold green]{right_answer}[/bold green]!', postfix)
            return ''
        elif str(answer) in answer_list:
            self.console.print(f'You already submitted [bold]{answer}[/bold]!')
            verb = self.get_verbose(
                dict(zip(answer_list, response_list))[str(answer)])
            if verb:
                self.console.print(verb)
            return ''
        inp = self.console.input(
            f'(Press [bold]ENTER[/bold] to continue, '
            f'or write anything to cancel) ')
        if inp:
            return ''
        response = self.session.post(
            f'https://adventofcode.com/{self.year}/day/{self.day}/answer',
            {'level': part, 'answer': answer}
        )
        page = response.text
        parsed = bs4.BeautifulSoup(page, 'html.parser')
        article = parsed.find('article')
        if article is None:
            return page
        par = article.find_next('p')
        text = par.getText()

        wait_match = re.search(r'You have (\d+)s left to wait', text)
        output = ''
        prefix = f'The submission [bold]{answer}[/bold]'
        if wait_match:
            self.console.print(f'You have {wait_match.group(1)}s left to wait!')
        elif 'too low' in text:
            self.console.print(prefix, f'is [blue]too low[/blue]!')
            output = 'low'
        elif 'too high' in text:
            self.console.print(prefix, f'is [magenta]too high[/magenta]!')
            output = 'high'
        elif 'not the right answer' in text:
            self.console.print(prefix, f'is [red]incorrect[/red]!')
            output = 'wrong'
        elif "That's the right answer!" in text:
            self.console.print(prefix, f"is [bold green]correct[/bold green]!")
            output = 'right'
        elif "You don't seem to be solving the right level" in text:
            self.console.print(f"Part {part} was already submitted!")
        if output:
            self.add_submission(answer, output, part)
            if output != 'right':
                self.console.print(f'Past responses for part {part}:')
                self.print_past_submissions(part)
        return text

    def add_submission(self, answer, response, part: int) -> None:
        """Adds a submission to the day and part's .out file."""
        with open(f'day{self.day}.out{part}', 'a') as f:
            f.write(f'[{response}\t]\t{answer}\n')

    def get_past_submissions(self, part: int) -> List[str]:
        """Retrieves past submissions for the day and part."""
        assert part in (1, 2), "Part must be either 1 or 2."
        if not os.path.exists(f'day{self.day}.out{part}'):
            return []

        with open(f'day{self.day}.out{part}', 'r') as f:
            return f.read().strip().splitlines()

    def parse_past_submissions(self, part: int) -> Tuple[List[str], List[str]]:
        """
        Parses a list of past submissions, returning lists of
        submitted answers and server responses.
        """
        submissions = self.get_past_submissions(part)
        response_list = []
        answer_list = []
        for submission in submissions:
            match = re.fullmatch(r'\[([^]]+)]\s(.*)', submission)
            if match:
                response_list.append(match.group(1).strip())
                answer_list.append(match.group(2).strip())
        return answer_list, response_list

    @staticmethod
    def get_verbose(response: str) -> str:
        """Converts a short response into a longer form, with rich coloring."""
        if response == 'low':
            return f'This guess was [blue]too low[/blue]!'
        elif response == 'high':
            return f'This guess was [magenta]too high[/magenta]!'
        elif response == 'right':
            return f'This guess was [green]correct[/green]!'
        elif response == 'wrong':
            return f'This guess was [red]incorrect[/red]!'
        return ''

    def print_past_submissions(self, part: int, sort: bool = False) -> None:
        """Prints a formatted list of past submissions."""
        answers, responses = self.parse_past_submissions(part)
        pretty_dict = dict()
        pretty_responses = []
        for answer, response in zip(answers, responses):
            color = 'none'
            if response == 'low':
                color = 'blue'
            elif response == 'high':
                color = 'magenta'
            elif response == 'right':
                color = 'green'
            elif response == 'wrong':
                color = 'red'
            cur = f'[{color}]{response}[/{color}]'
            pretty_dict[answer] = cur
            pretty_responses.append(cur)
        if sort:
            try:  # try sorting as ints
                self.console.print(
                    '\n'.join(f'[{pretty_dict[str(answer)]}\t]\t{answer}'
                              for answer in sorted(map(int, answers))))
            except ValueError:  # if error, sort lexicographically
                self.console.print(
                    '\n'.join(f'[{pretty_dict[answer]}\t]\t{answer}'
                              for answer in sorted(answers)))
        else:
            self.console.print(
                '\n'.join(f'[{response}\t]\t{answer}'
                          for answer, response in
                          zip(answers, pretty_responses)))

    def reset_start_time(self) -> None:
        """Reset the stored start time."""
        self.start_time = perf_counter()

    def get_elapsed(self) -> float:
        """Retrieve the elapsed time since last stored start time."""
        return perf_counter() - self.start_time

    def print_elapsed(self) -> None:
        """Pretty print the elapsed time."""
        self.console.print(
            f'{self.get_elapsed()} seconds have elapsed.'
        )
