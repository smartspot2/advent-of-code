import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=17, year=2020)
data = session.data.strip()
data = data.split()


def setup(dim):
    adj = [*product(range(-1, 2), repeat=dim)]
    adj.remove((0,) * dim)

    b = defaultdict(int)
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            b[(i, j, *(0,) * (dim - 2))] = el == '#'
    return b, adj


def getnext(b, adj, *coord):
    occ = 0
    for diff in adj:
        if b[(*map(sum, zip(coord, diff)),)]:
            occ += 1
    return (b[coord] and occ in (2, 3)) or (not b[coord] and occ == 3)


def simulate(b, adj):
    newb = defaultdict(int)
    visited = set()
    for coord in list(b.keys()):
        newb[coord] = getnext(b, adj, *coord)
        visited.add(coord)
        for diff in adj:
            new = (*map(sum, zip(coord, diff)),)
            if new in visited:
                continue
            newb[new] = getnext(b, adj, *new)
            visited.add(new)
    return newb


board, ADJ = setup(3)
for _ in range(6):
    board = simulate(board, ADJ)
p1 = sum(board.values())

board, ADJ = setup(4)
for _ in range(6):
    board = simulate(board, ADJ)
p2 = sum(board.values())

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
