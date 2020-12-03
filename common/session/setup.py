from typing import Union
import os.path
import requests
import bs4
import re
from colorama import Fore, Style

from .cookie import cookie


class AdventSession:
    def __init__(self, day, year=2020):
        self.day = day
        self.year = year
        self.session = requests.Session()
        self.session.cookies.update({'session': cookie})
        self.data = self.setup_session()

    def setup_session(self):
        filename = f'day{self.day}.in'
        if not os.path.exists(filename):  # get data and store into file
            print('Retrieving input...')
            data = self.session.get(
                f'https://adventofcode.com/{self.year}/day/{self.day}/input'
            ).text
            if 'request this endpoint before it unlocks' in data:
                print(f'Day {self.day} has not been unlocked yet!')
                return data  # don't do anything if it hasn't unlocked yet
            with open(filename, 'w') as input_file:
                input_file.write(data)
            print('Done!')
        else:
            with open(filename, 'r') as input_file:
                data = input_file.read()
        return data

    def submit(self, answer, part):
        """
        Submits an answer, but asks for confirmation before sending.
        Parses the http response and notifies the user as needed.
        Tracks past submissions
        :param answer: the answer to submit
        :param part: the part of the question to submit for
        :return: raw content of the response
        """
        print(f'Submitting {Style.BRIGHT}{answer}{Style.RESET_ALL} ...')
        answer_list, response_list = self.parse_past_submissions(part)
        if 'right' in response_list:
            idx = response_list.index('right')
            right_answer = answer_list[idx]
            print(f'Part {part} was already submitted with the right answer of '
                  f'{Style.BRIGHT}{Fore.GREEN}{right_answer}{Style.RESET_ALL}!')
            return
        elif str(answer) in answer_list:
            print(f'You already submitted {Style.BRIGHT}{answer}{Style.RESET_ALL}!')
            verb = self.get_verbose(
                dict(zip(answer_list, response_list))[str(answer)])
            if verb:
                print(verb)
            return
        inp = input(f'(Press ENTER to continue, or write anything to cancel) ')
        if inp:
            return
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

        wait_match = re.search(r'You have (\d+) left to wait', text)
        output = ''
        if wait_match:
            print(f'You have {wait_match.group(1)}s left to wait!')
        elif 'too low' in text:
            print(f'The submission {Style.BRIGHT}{answer}{Style.RESET_ALL}'
                  f' is {Fore.BLUE}too low{Style.RESET_ALL}!')
            output = 'low'
        elif 'too high' in text:
            print(f'The submission {Style.BRIGHT}{answer}{Style.RESET_ALL}'
                  f' is {Fore.MAGENTA}too high{Style.RESET_ALL}!')
            output = 'high'
        elif 'not the right answer' in text:
            print(f'The submission {Style.BRIGHT}{answer}{Style.RESET_ALL}'
                  f' is {Fore.RED}incorrect{Style.RESET_ALL}!')
            output = 'wrong'
        elif "That's the right answer!" in text:
            print(f"The submission {Style.BRIGHT}{answer}{Style.RESET_ALL}"
                  f" was {Fore.GREEN}{Style.BRIGHT}correct{Style.RESET_ALL}!")
            output = 'right'
        elif "You don't seem to be solving the right level" in text:
            print(f"Part {part} was already submitted!")
        if output:
            self.add_submission(answer, output, part)
            if output != 'right':
                print(f'Past responses for part {part}:')
                self.print_past_submissions(part)
        return text

    def add_submission(self, answer, response, part):
        with open(f'day{self.day}.out{part}', 'a') as f:
            f.write(f'[{response}\t]\t{answer}\n')

    def get_past_submissions(self, part):
        assert part in (1, 2), "Part must be either 1 or 2."
        if not os.path.exists(f'day{self.day}.out{part}'):
            return []

        with open(f'day{self.day}.out{part}', 'r') as f:
            return f.read().strip().splitlines()

    def parse_past_submissions(self, part):
        submissions = self.get_past_submissions(part)
        response_list = []
        answer_list = []
        for submission in submissions:
            match = re.fullmatch(r'\[([^]]+)]\s(.*)', submission)
            if match:
                response_list.append(match.group(1).strip())
                answer_list.append(match.group(2).strip())
        return answer_list, response_list

    def get_verbose(self, response):
        if response == 'low':
            return f'This guess was {Fore.BLUE}too low{Style.RESET_ALL}!'
        elif response == 'high':
            return f'This guess was {Fore.MAGENTA}too high{Style.RESET_ALL}!'
        elif response == 'right':
            return f'This guess was {Fore.GREEN}correct{Style.RESET_ALL}!'
        elif response == 'wrong':
            return f'This guess was {Fore.RED}incorrect{Style.RESET_ALL}!'
        return ''

    def print_past_submissions(self, part, sort=False):
        answers, responses = self.parse_past_submissions(part)
        pretty_dict = dict()
        pretty_responses = []
        for answer, response in zip(answers, responses):
            color = Style.RESET_ALL
            if response == 'low':
                color = Fore.BLUE
            elif response == 'high':
                color = Fore.MAGENTA
            elif response == 'right':
                color = Fore.GREEN
            elif response == 'wrong':
                color = Fore.RED
            cur = f'{color}{response}{Style.RESET_ALL}'
            pretty_dict[answer] = cur
            pretty_responses.append(cur)
        if sort:
            output = ''
            try:
                as_int = list(map(int, pretty_dict.keys()))
                output = '\n'.join(map(pretty_dict.get, sorted(as_int)))
            except ValueError:
                output = '\n'.join(
                    map(pretty_dict.get, sorted(pretty_dict.keys())))
        else:
            output = '\n'.join(f'[{response}\t]\t{answer}'
                               for answer, response in
                               zip(answers, pretty_responses)
                               )
        print(output)

