import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=23, year=2020)
data = session.data.strip()
data = list(map(int, data))


def simulate(moves, max_val=None):
    nxt = {}

    if max_val:
        # chain to prevent creation of lorge array
        d = chain(data, range(max(data) + 1, max_val + 1))
    else:
        max_val = max(data)
        d = iter(data)

    cur = next(d)
    for i in d:
        nxt[cur], cur = i, i
    nxt[cur] = data[0]

    cur = data[0]
    for move in range(moves):
        pick = nxt[cur]
        pick_end = nxt[nxt[pick]]
        dest = cur - 1 if cur != 1 else max_val
        while dest in (pick, nxt[pick], pick_end):
            dest = dest - 1 if dest > 1 else max_val

        nxt[dest], nxt[pick_end], nxt[cur] = \
            pick, nxt[dest], nxt[pick_end]

        cur = nxt[cur]
    return nxt


p1 = ''
link = simulate(100)
tmp = 1
for _ in range(len(data) - 1):
    p1 += str(link[tmp])
    tmp = link[tmp]
print(f'Part 1: {p1}')

link = simulate(10_000_000, max_val=1_000_000)
p2 = link[1] * link[link[1]]
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
