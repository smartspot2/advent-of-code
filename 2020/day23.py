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


class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None

    def __repr__(self):
        return repr(self.val)


def simulate(moves, max_val=None):
    nodes = {}

    if max_val:
        # chain to prevent creation of lorge array
        d = chain(data, range(max(data) + 1, max_val + 1))
    else:
        max_val = max(data)
        d = iter(data)

    cur = Node(next(d))
    nodes[1] = cur
    for i in d:
        nxt = Node(i)
        cur.nxt, nodes[i] = nxt, nxt
        cur = nxt
    cur.nxt = nodes[1]

    cur = nodes[1]
    for move in range(moves):
        pick = cur.nxt
        pick_end = pick.nxt.nxt
        dest = cur.val - 1 if cur.val != 1 else max_val
        while dest in (pick.val, pick.nxt.val, pick_end.val):
            dest = dest - 1 if dest > 1 else max_val
        dest_node = nodes[dest]

        dest_node.nxt, pick_end.nxt, cur.nxt = \
            pick, dest_node.nxt, pick_end.nxt

        cur = cur.nxt

    return nodes[1]


p1 = ''
tmp = simulate(100)
for _ in range(len(data)):
    p1 += str(tmp.val)
    tmp = tmp.nxt
p1 = p1[1:]
print(f'Part 1: {p1}')

one = simulate(10_000_000, max_val=1_000_000)
p2 = one.nxt.val * one.nxt.nxt.val
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
