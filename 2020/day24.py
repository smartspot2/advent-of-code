import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=24, year=2020)
data = session.data.strip()
data = data.split('\n')

repl = {
    'nw': 1j,
    'ne': 1 + 1j,
    'sw': -1 - 1j,
    'se': -1j,
    'e': 1,
    'w': -1
}

flipped = set()
for ident in data:
    pos, i = 0, 0
    while i < len(ident):
        r = ident[i]
        i += 1
        if r in ('s', 'n'):
            r += ident[i]
            i += 1
        pos += repl[r]
    flipped ^= {pos}

p1 = len(flipped)

for _ in range(100):
    new = flipped.copy()
    neigh_dict = defaultdict(int)
    for tile in flipped:
        neigh = 0
        for adj in repl.values():
            if tile + adj in flipped:
                neigh += 1
            neigh_dict[tile + adj] += 1
        if neigh == 0 or neigh > 2:
            new.remove(tile)

    for tile in neigh_dict:
        if tile not in flipped and neigh_dict[tile] == 2:
            new.add(tile)
    flipped = new

p2 = len(flipped)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
