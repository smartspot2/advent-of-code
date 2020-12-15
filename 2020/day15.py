import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=15, year=2020)
data = session.data.strip()
data = list(map(int, data.split(',')))

p1, p2 = 0, 0

spoken = set(data[:-1])
last = {v: i for i, v in enumerate(data, 1)}

prev = data[-1]
times = 30000000
for i in range(len(data) + 1, times + 1):
    if prev in spoken:
        new = i - 1 - last[prev]
        last[prev] = i - 1
        prev = new
    else:
        last[prev] = i - 1
        spoken.add(prev)
        prev = 0

    if i == 2020:
        p1 = prev
p2 = prev

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
