from collections import defaultdict


class IntCode:
    def __init__(self, in_data, *, debug=False, input_list=None):
        # self._data = in_data.copy() + [0] * 1000000
        self._data = defaultdict(int, {i: v for i, v in enumerate(in_data)})
        self.data = self._data.copy()
        self.cur = self.rel_base = 0

        self.debug = debug

        if input_list is None:
            self.input_list = []
        else:
            self.input_list = input_list.copy()

        def op1(a, b, out):
            self.log(f"[1] set {out} (prev {self.data[out]}) to {a + b} ({a} + {b})")
            self.data[out] = a + b

        def op2(a, b, out):
            self.log(f"[2] set {out} (prev {self.data[out]}) to {a * b} ({a} * {b})")
            self.data[out] = a * b

        # -3 in jumps to compensate for moving forward cur
        def op5(a, jump):
            if a:
                self.log(f"[5] jumped to {jump} ({a} != 0)")
                self.cur = jump - 3
            elif debug:
                print(f"[5] didn't jump to {jump} ({a} == 0)")

        def op6(a, jump):
            if not a:
                self.log(f"[6] jumped to {jump} ({a} == 0)")
                self.cur = jump - 3
            elif debug:
                print(f"[6] didn't jump to {jump} ({a} != 0)")

        def op7(a, b, out):
            self.log(f"[7] set {out} (prev {self.data[out]}) to {int(a < b)} ({a} <? {b})")
            self.data[out] = int(a < b)

        def op8(a, b, out):
            self.log(f"[8] set {out} (prev {self.data[out]}) to {int(a == b)} ({a} =? {b})")
            self.data[out] = int(a == b)

        def op9(rel_base):
            self.log(f"[9] shifted relative base by {rel_base} (now {self.rel_base + rel_base})")
            self.rel_base += rel_base

        # (num_args, sets_value, op)
        self.ops = {
            1: (3, True, op1),
            2: (3, True, op2),
            3: (1, True, lambda _: ...),
            4: (1, False, lambda _: ...),
            5: (2, False, op5),
            6: (2, False, op6),
            7: (3, True, op7),
            8: (3, True, op8),
            9: (1, False, op9),
        }

        self.modes = {
            0: lambda pos: self.data[pos],
            1: lambda pos: pos,
            2: lambda pos: self.data[pos + self.rel_base],
        }

    def reset(self):
        self.data = self._data.copy()
        self.cur = self.rel_base = 0

    def log(self, msg):
        if self.debug:
            print(msg)

    def send(self, obj):
        if isinstance(obj, list):
            self.input_list.extend(obj)
        elif isinstance(obj, int):
            self.input_list.append(obj)
        else:
            raise ValueError(f"expected list of ints or int, but got {obj}")

    def evaluate(self, init=None, input_list=None):
        self.data = self._data.copy()
        self.cur = 0
        self.rel_base = 0

        if input_list:
            self.input_list = input_list.copy()

        if init:
            for k, v in init.items():
                self.data[k] = v

        output = []
        for it in self.evaluate_step():
            output.append(it)
        return output

    def evaluate_step(self, init=None):
        if init:
            for k, v in init.items():
                self.data[k] = v
        while True:
            oplist = list(map(int, str(self.data[self.cur]).zfill(2)))
            opcode = oplist[-2] * 10 + oplist[-1]
            # get given parameters
            params = oplist[-3::-1] if len(oplist) > 2 else []

            self.log(f"\ndata: {[self.data[self.cur + i] for i in range(10)]}\n"
                     f"cur={self.cur}, {opcode=}, rel_base={self.rel_base}\n{params=}")
            # halt
            if opcode == 99:
                self.log("[99] halted\n")
                break

            if opcode not in self.ops:
                raise ValueError(f"opcode not valid: {self.data[self.cur]}")

            num_args, sets_value, op = self.ops[opcode]

            params += [0] * (num_args - len(params))  # pad 0s if needed
            args = [self.data[self.cur + 1 + i] for i in range(num_args)]
            out = args[-1]
            op_args = [self.modes[param](k) for param, k in zip(params, args)]

            if sets_value and params[-1] == 2:
                self.log(f"\trelative out: set out to {out + self.rel_base} ({out} + {self.rel_base})")
                out += self.rel_base

            self.log(f"args: {args} -> {op_args}")

            # input
            if opcode == 3:
                while not self.input_list:
                    yield "empty"
                    # raise ValueError("input_list is empty")
                self.log(f"[3] set pos {out} (prev {self.data[out]}) to (input) {self.input_list[0]}")
                self.data[out] = self.input_list.pop(0)
            # output
            elif opcode == 4:
                self.log(f"[4] outputted {op_args[0]}")
                yield op_args[0]

            # if
            if sets_value:
                op(*op_args[:-1], out)
                self.cur += num_args + 1 if out != self.cur else 0
            else:
                op(*op_args)
                self.cur += num_args + 1


def evaluate_until_input(it):
    """
    Evaluates Intcode program until it asks for an input, returning the eoutput
    """
    out = []
    try:
        cur = next(it)
        while cur != 'empty':
            out.append(cur)
            cur = next(it)
    except StopIteration:
        print("StopIteration hit")
    return out
