import sys

with open("day2.in", "r") as f:
    data = list(map(int, f.read().split(',')))


class IntCode:
    def __init__(self):
        self.ops = {
            1: (2, lambda a, b: a + b),
            2: (2, lambda a, b: a * b)
        }

    def evaluate(self, in_data, init=None):
        cur_data = in_data.copy()

        if init:
            for k, v in init.items():
                cur_data[k] = v

        cur = 0
        while cur_data[cur] != 99:
            opcode = cur_data[cur]
            if opcode not in self.ops:
                raise ValueError(f"opcode not valid: {cur_data[cur]}")

            num_args, op = self.ops[opcode]

            *args, out = cur_data[cur + 1: cur + num_args + 2]
            op_args = [cur_data[pos] for pos in args]

            cur_data[out] = op(*op_args)
            cur += num_args + 2
        return cur_data[0]


code = IntCode()
# Part 1
print(code.evaluate(data, init={1: 12, 2: 2}))

# Part 2
for i in range(100):
    for j in range(100):
        if code.evaluate(data, init={1: i, 2: j}) == 19690720:
            print(i * 100 + j)
