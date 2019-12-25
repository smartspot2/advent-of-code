from IntCode import IntCode

with open("day2.in", "r") as f:
    data = list(map(int, f.read().split(',')))

code = IntCode(data)
# Part 1
code.evaluate(init={1: 12, 2: 2})
print(code.data[0])

# Part 2
for i in range(100):
    for j in range(100):
        code.evaluate(init={1: i, 2: j})
        if code.data[0] == 19690720:
            print(i * 100 + j)
