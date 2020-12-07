import numpy as np
# import networkx as nx
from collections import *
from itertools import *
import re

from common.session import AdventSession

session = AdventSession(day=7, year=2020)
data = session.data.strip()
data = data.split('\n')

rules = dict()

for i, line in enumerate(data):
    outer, inner = line.split(' bags contain ')
    if 'no other bags' in inner:
        rules[outer] = []
        continue
    inner = inner.strip('.').split(', ')
    rules[outer] = []
    for _type in inner:
        count, *bag_type = _type.split(' ')
        bag_type = ' '.join(bag_type[:-1])
        rules[outer].append((int(count), bag_type))


def recur(bag):
    if bag == 'shiny gold':
        return True
    for other in rules[bag]:
        if recur(other[1]):
            return True
    return False


def recur2(bag):
    if not rules[bag]:
        return 0
    total = 0
    for cnt, bag_type in rules[bag]:
        total += cnt + cnt * recur2(bag_type)
    return total


p1, p2 = 0, 0

for bag in rules:
    if bag != 'shiny gold':
        p1 += recur(bag)

p2 = recur2('shiny gold')

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
