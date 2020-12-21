import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=21, year=2020)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0

items = []
all_ings = set()
poss = defaultdict(set)

for i, line in enumerate(data):
    ingredients, allergens = line.split('(')
    ingredients = ingredients.strip().split()
    allergens = allergens[len('contains '):-1].split(', ')
    items.append((ingredients, allergens))
    all_ings |= set(ingredients)
    for ing in ingredients:
        poss[ing] |= set(allergens)

for ing in all_ings:
    for pos_allergen in poss[ing].copy():
        for cur_ings, cur_allergens in items:
            if pos_allergen in cur_allergens and ing not in cur_ings:
                poss[ing] -= {pos_allergen}

impossible = set(ing for ing in poss if not poss[ing])
p1 = sum(session.data.split().count(ing) for ing in impossible)

certain = dict()

while any(poss.values()):
    for ing in poss:
        if len(poss[ing]) == 1:
            certain[ing], = poss[ing]
            for other in poss:
                poss[other] -= {certain[ing]}

p2 = ','.join(sorted(certain, key=certain.get))

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
