import numpy as np

with open("day10.in", "r") as f:
    data = np.array([[1 if c == '#' else 0 for c in row] for row in f.read().splitlines()])

pos = np.argwhere(data == 1)
sees = {tuple(a): 0 for a in pos}
sees_pos = {(x, y): [] for x, y in pos}
slopes = {(x, y): [] for x, y in pos}

for c1 in pos:
    for c2 in pos:
        if tuple(c1) == tuple(c2):
            continue
        diff = c2 - c1
        diff = diff / np.math.gcd(*diff)
        tuplediff = tuple(diff)
        if tuplediff not in slopes[tuple(c1)]:
            slopes[tuple(c1)].append(tuplediff)
            sees[tuple(c1)] += 1

print(sorted(sees.items(), key=lambda p: p[1])[-1])
