import numpy as np
# import networkx as nx
from collections import *
from itertools import *
import re

from common.session import AdventSession

session = AdventSession(day=5, year=2020)
data = session.data.strip()
# data = data
data = data.split('\n')
# data = list(map(int, data.split()))


def getids():
    ids = []
    for line in data:
        row = int(''.join(map(str, map(int, [c == 'B' for c in line[:7]]))), 2)
        col = int(''.join(map(str, map(int, [c == 'R' for c in line[-3:]]))), 2)
        ids.append(row * 8 + col)
    return ids


def part1():
    return max(getids())


print(part1())


def part2():
    ids = getids()
    for k in range(min(ids), max(ids)+1):
        if k not in ids:
            return k


print(part2())

# session.submit(part1(), part=1)
# session.submit(part2(), part=2)

# session.submit(part1(), part=2)

(lambda d: print(max(d), *set(range(min(d), max(d))) - d))({int(l.translate(str.maketrans('FBLR', '0101')), 2) for l in data})
