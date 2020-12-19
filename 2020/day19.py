import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=19, year=2020)
data = session.data.strip()
data, messages = map(lambda s: s.split('\n'), data.split('\n\n'))

p1, p2 = 0, 0

rules = dict()

for i, line in enumerate(data):
    num, rule = line.split(': ')
    if '|' in rule:
        sub = rule.split(' | ')
        rules[num] = [[*map(int, r.split(' '))] for r in sub]
    elif '"' in rule:
        rules[num] = rule[1:-1]
    else:
        rules[num] = [[*map(int, rule.split(' '))]]


def matches(query, num):
    rule = rules[str(num)]
    poss_matches = []
    if isinstance(rule, list):
        for sub in rule:
            cur_poss = [query]
            for r in sub:
                new = []
                for q in cur_poss:
                    new += matches(q, r)
                cur_poss = new
            poss_matches += cur_poss
        return poss_matches
    elif isinstance(rule, str):
        if query.startswith(rule):
            return [query[len(rule):]]
        return []


for message in messages:
    possibilities = matches(message, 0)
    p1 += '' in possibilities

rules['8'] = [[42], [42, 8]]
rules['11'] = [[42, 31], [42, 11, 31]]

for message in messages:
    possibilities = matches(message, 0)
    p2 += '' in possibilities

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
