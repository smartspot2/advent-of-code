from IntCode import IntCode


class Chain:
    """
    Chain of IntCode programs, each feeding their outputs into the next.
    """

    def __init__(self, num, data, input_lists=None):
        self.codes = [IntCode(data) for _ in range(num)]
        if input_lists:
            assert len(input_lists) == num, "input lists must match number of programs per chain"
            for code, inp in zip(self.codes, input_lists):
                code.send(inp)
        self.iters = [code.evaluate_step() for code in self.codes]

    def evaluate(self, init=None):
        """
        Runs one loop of the chain.
        :param init:            initial input
        :return:                output of the last IntCode in chain
        :raises StopIteration:  when IntCode program terminates
        """
        res = init
        for code, it in zip(self.codes, self.iters):
            if res is not None:
                code.send(res)
            res = next(it)
        return res

    def evaluate_continuous(self, init=None):
        """
        Runs chain, looping from end to beginning, until a program halts.
        :param init:    inital input
        :return:        output of last IntCode before termination of a program
        """
        res = init
        try:
            while True:
                res = self.evaluate(res)
        except StopIteration:
            return res
