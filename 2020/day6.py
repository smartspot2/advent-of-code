import numpy as np
# import networkx as nx
from collections import *
from itertools import *
import re

from common.session import AdventSession

session = AdventSession(day=6, year=2020)
data = session.data.strip()
data = data.split('\n\n')


def part1():
    out = 0
    for i, group in enumerate(data):
        questions = defaultdict(int)
        for line in group.split():
            for q in line:
                questions[q] += 1
        out += len(questions.items())
    return out


print(part1())


def part2():
    out = 0
    for i, group in enumerate(data):
        questions = defaultdict(int)
        for line in group.split():
            for q in line:
                questions[q] += 1
        out += sum([1 for q in questions if questions[q] == len(group.split())])
    return out


print(part2())

# session.submit(part1(), part=2)
# session.submit(part2(), part=2)

# session.submit(part1(), part=2)

print(*(lambda d: (sum(len(set(g) - {'\n'}) for g in d), sum(len(set.intersection(*map(set, g.split()))) for g in d)))(session.data.split('\n\n')))
print(*(lambda d: (map(sum, zip(*[(len(set(g) - {'\n'}), len(set.intersection(*map(set, g.split())))) for g in d]))))(session.data.split('\n\n')))
