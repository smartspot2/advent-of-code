import numpy as np
# import networkx as nx
from collections import *
from itertools import *

from common.session import AdventSession

session = AdventSession(day=3, year=2020)
data = session.data.strip()
data = [[1 if x == '#' else 0 for x in line] for line in data.splitlines()]
# data = list(map(int, data.split()))

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]


def part1():
    out = 0
    pos = np.array([0, 0])
    for r in range(len(data)):  # # rows
        c = 3 * r
        out += data[r][c % len(data[0])] == 1
    return out


print(part1())


def part2():
    prod = 1
    for dr, dc in slopes:
        out = 0
        pos = np.array([0, 0])
        while pos[0] < len(data) - 1:
            pos += (dr, dc)
            r, c = pos
            out += data[r][c % len(data[0])] == 1
        prod *= out
    return prod


print(part2())

# session.submit(part1(), part=1)
# session.submit(part2(), part=2)

# session.submit(part1(), part=2)
