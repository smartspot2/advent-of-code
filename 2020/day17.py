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

    b = set()
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el == '#':
                b.add((i, j, *(0,) * (dim - 2)))
    return b, adj


def getnext(b, adj, coord):
    occ = sum((*map(sum, zip(coord, diff)),) in b for diff in adj)
    return (coord in b and occ in (2, 3)) or (coord not in b and occ == 3)


def simulate(b, adj):
    newb = set()
    visited = set()
    for coord in b:
        if coord not in visited:
            if getnext(b, adj, coord):
                newb.add(coord)
            visited.add(coord)
        for diff in adj:
            new = (*map(sum, zip(coord, diff)),)
            if new not in visited:
                if getnext(b, adj, new):
                    newb.add(new)
                visited.add(new)
    return newb


board, ADJ = setup(3)
for _ in range(6):
    board = simulate(board, ADJ)
p1 = len(board)

board, ADJ = setup(4)
for _ in range(6):
    board = simulate(board, ADJ)
p2 = len(board)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
