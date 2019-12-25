from IntCode import IntCode

with open("day9.in", "r") as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)
# Part 1
print(code.evaluate(input_list=[1])[-1])
# Part 2
print(code.evaluate(input_list=[2])[-1])

