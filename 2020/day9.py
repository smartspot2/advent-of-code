import numpy as np
# import networkx as nx
from collections import *
from itertools import *
import re

from common.session import AdventSession

session = AdventSession(day=9, year=2020)
data = session.data.strip()
data = list(map(int, data.split()))

p1, p2 = 0, 0

for i, val in enumerate(data[25:], 25):
    sub = data[max(0, i-25):i]
    for k in sub:
        if val - k in sub:
            break
    else:
        p1 = val
        break

prefixes = [data[0]]

for k in data[1:]:
    prefixes.append(prefixes[-1] + k)

for i, val1 in enumerate(prefixes):
    for j, val2 in enumerate(prefixes[i+1:],i+1):
        if val2 - val1 == p1:
            p2 = max(data[i+1:j+1]) + min(data[i+1:j+1])
            break
    else:
        continue
    break

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
