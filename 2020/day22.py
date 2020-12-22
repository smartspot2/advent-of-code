import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=22, year=2020)
data = session.data.strip()
player1, player2 = data.split('\n\n')

p1deck = [*map(int, player1.split('\n')[1:])]
p2deck = [*map(int, player2.split('\n')[1:])]


def part1(d1, d2):
    while d1 and d2:
        a, b = d1.pop(0), d2.pop(0)
        if a > b:
            d1.extend([a, b])
        elif b > a:
            d2.extend([b, a])
    return d1, d2


@lru_cache(maxsize=None)
def recur(d1, d2):
    rounds = set()
    while d1 and d2:
        if (t := (d1, d2)) in rounds:
            return 1, d1, d2
        rounds.add(t)
        a, d1, b, d2 = d1[0], d1[1:], d2[0], d2[1:]
        if len(d1) >= a and len(d2) >= b:
            winner = recur(d1[:a], d2[:b])[0]
        else:
            winner = (a < b) + 1
        if winner == 1:
            d1 += (a, b)
        elif winner == 2:
            d2 += (b, a)
    return (1, d1, d2) if d1 else (2, d1, d2)


p1res, p2res = part1(p1deck.copy(), p2deck.copy())
deck = p1res or p2res
p1 = sum(map(math.prod, zip(deck, range(len(deck), 0, -1))))

w, p1res, p2res = recur(tuple(p1deck), tuple(p2deck))
deck = [p1res, p2res][w - 1]
p2 = sum(map(math.prod, zip(deck, range(len(deck), 0, -1))))

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
