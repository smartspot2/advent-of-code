import numpy as np
from math import pi as PI
with open("day10.in", "r") as f:
    data = np.array([[1 if c == '#' else 0 for c in row] for row in f.read().splitlines()])

pos: list = np.argwhere(data == 1).tolist()
sees = {tuple(a): 0 for a in pos}
sees_pos = []
slopes = []
alllist = []
v = 0
c1 = np.array([29, 28])
while len(pos) > 1:
    for c2 in sorted(pos, key=lambda a: np.math.hypot(*(c1 - a))):
        if tuple(c1) == tuple(c2):
            continue
        diff = c2 - c1
        diff = diff / np.math.gcd(*diff)
        tuplediff = tuple(diff)
        if tuplediff not in slopes:
            slopes.append(tuplediff)
            sees_pos.append(tuple(c2))
    for p in sorted(sees_pos, key=lambda a: (-np.math.atan2(a[1] - c1[1], a[0] - c1[0]) - PI) % (2 * PI)):
        v += 1
        if v == 200:
            print(p)
            break
        pos.remove(list(p))
        alllist.append(list(p))
    sees_pos = []
    slopes = []

print(max(sees.items(), key=lambda p: p[1]))
