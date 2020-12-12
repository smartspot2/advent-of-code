from copy import deepcopy

import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import re

from common.session import AdventSession

session = AdventSession(day=11, year=2020)
data = session.data.strip()
data = list(map(list, data.split()))

p1, p2 = 0, 0

ADJ = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def simulate(d):
    newd = deepcopy(d)
    for r, row in enumerate(d):
        for c, el in enumerate(row):
            if d[r][c] == '.':
                continue
            occ = 0
            for dr, dc in ADJ:
                if 0 <= r + dr < len(d) and 0 <= c + dc < len(row):
                    if d[r + dr][c + dc] == '#':
                        occ += 1
            if el == 'L' and occ == 0:
                newd[r][c] = '#'
            elif el == '#' and occ >= 4:
                newd[r][c] = 'L'
    return newd


cur = deepcopy(data)
while True:
    nex = simulate(cur)
    if np.all(np.array(cur) == np.array(nex)):
        break
    cur = nex

p1 = sum(cur, []).count('#')


def simulate2(d):
    newd = deepcopy(d)
    for r, row in enumerate(d):
        for c, el in enumerate(row):
            if d[r][c] == '.':
                continue
            occ = 0
            for dr, dc in ADJ:
                origdr, origdc = dr, dc
                while 0 <= r + dr < len(d) and 0 <= c + dc < len(row) \
                        and d[r + dr][c + dc] == '.':
                    dr += origdr
                    dc += origdc
                if 0 <= r + dr < len(d) and 0 <= c + dc < len(row):
                    if d[r + dr][c + dc] == '#':
                        occ += 1
            if el == 'L' and occ == 0:
                newd[r][c] = '#'
            elif el == '#' and occ >= 5:
                newd[r][c] = 'L'
    return newd


cur = deepcopy(data)
while True:
    nex = simulate2(cur)
    if np.all(np.array(cur) == np.array(nex)):
        break
    cur = nex

p2 = sum(cur, []).count('#')

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
