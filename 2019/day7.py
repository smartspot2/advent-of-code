from itertools import permutations

from IntCode import IntCode

with open("day7.in", "r") as f:
    data = list(map(int, f.read().strip().split(',')))

# Part 1
maxout = 0
for a, b, c, d, e in permutations([0, 1, 2, 3, 4]):
    aout = IntCode(data).evaluate(input_list=[a, 0])[-1]
    bout = IntCode(data).evaluate(input_list=[b, aout])[-1]
    cout = IntCode(data).evaluate(input_list=[c, bout])[-1]
    dout = IntCode(data).evaluate(input_list=[d, cout])[-1]
    eout = IntCode(data).evaluate(input_list=[e, dout])[-1]
    maxout = max(maxout, eout)

print(maxout)

# Part 2
maxout = 0
for perm in permutations([5, 6, 7, 8, 9]):
    code_list = [IntCode(data, input_list=[phase]) for phase in perm]
    iter_list = [c.evaluate_step() for c in code_list]
    res = 0
    try:
        while True:
            for it, code in zip(iter_list, code_list):
                code.send(res)
                res = next(it)
    except StopIteration:
        maxout = max(maxout, res)

print(maxout)
