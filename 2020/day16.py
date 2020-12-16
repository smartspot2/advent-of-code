import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=16, year=2020)
data = session.data.strip()
data = data.split('\n\n')

raw_fields = data[0].split('\n')
myticket = [*map(int, data[1].split('\n')[1].split(','))]
othertickets = [[*map(int, ticket.split(','))]
                for ticket in data[2].split('\n')[1:]]

p1, p2 = 0, 1

fields = dict()

for field in raw_fields:
    name, rest = field.split(': ')
    first, second = rest.split(' or ')
    first = range(int(first.split('-')[0]), int(first.split('-')[1]) + 1)
    second = range(int(second.split('-')[0]), int(second.split('-')[1]) + 1)
    fields[name] = (first, second)

all_values = sum(othertickets, [])

invalid = [val for val in all_values
           if all(val not in field[1] and val not in field[2]
                  for field in fields.values())]
p1 = sum(invalid)

othertickets = [ticket for ticket in othertickets if
                all(v not in ticket for v in invalid)]
pos = defaultdict(list)

for i, group in enumerate(zip(*othertickets)):
    for name, field in fields.items():
        if all(v in field[1] or v in field[2] for v in group):
            pos[i].append(name)

while any(len(f) > 1 for f in pos.values()):
    for i, field in pos.items():
        if len(field) == 1:
            for j in pos:
                if len(pos[j]) > 1 and field[0] in pos[j]:
                    pos[j].remove(field[0])

for i, field in pos.items():
    if field[0].startswith('departure'):
        p2 *= myticket[i]

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
