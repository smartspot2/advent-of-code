import numpy as np

from IntCode import IntCode

with open("day19.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)


def eval_for(x, y):
    return code.evaluate(input_list=[x, y])[0]


total = 0
for x in range(50):
    for y in range(50):
        total += eval_for(x, y)

# Part 1
print(total)

pos = (4, 5)

while True:
    topright = eval_for(pos[0] + 99, pos[1] - 99)
    if topright == 1:
        break

    pos = pos[0], pos[1] + 1
    while eval_for(*pos) == 0:
        pos = pos[0] + 1, pos[1]

# Part 2
print(pos[0], pos[1] - 99)
