import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import re

from common.session import AdventSession

session = AdventSession(day=12, year=2020)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0

pos = np.array((0, 0))
direction = 0

dirs = ['E', 'N', 'W', 'S']
dirdict = {
    'E': np.array((1, 0)),
    'N': np.array((0, 1)),
    'W': np.array((-1, 0)),
    'S': np.array((0, -1)),
}

for i, line in enumerate(data):
    d = line[0]
    amt = int(line[1:])

    if d == 'L':
        direction = (direction + amt) % 360
    elif d == 'R':
        direction = (direction - amt) % 360
    else:
        if d == 'F':
            d = dirs[direction // 90]
        pos += dirdict[d] * amt

p1 = abs(pos[0]) + abs(pos[1])

pos = np.array((0, 0))
way = np.array((10, 1))

for i, line in enumerate(data):
    d = line[0]
    amt = int(line[1:])

    if d == 'L':
        for _ in range(amt // 90):
            diff = way - pos
            way = pos + diff[::-1] * (-1, 1)
    elif d == 'R':
        for _ in range(amt // 90):
            diff = way - pos
            way = pos + diff[::-1] * (1, -1)
    elif d == 'F':
        diff = way - pos
        pos += amt * diff
        way += amt * diff
    else:
        way += dirdict[d] * amt

p2 = abs(pos[0]) + abs(pos[1])

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
