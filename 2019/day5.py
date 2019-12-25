from IntCode import IntCode

with open("day5.in", "r") as f:
    data = list(map(int, f.read().split(',')))

# Part 1
print(IntCode(data).evaluate(input_list=[1]))
# Part 2
print(IntCode(data).evaluate(input_list=[5]))
