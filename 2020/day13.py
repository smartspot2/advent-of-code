from sympy.ntheory.modular import crt
import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=13, year=2020)
data = session.data.strip()
data = data.split('\n')
times = data[1].split(',')

p1, p2 = 0, 0

start = int(data[0])
while True:
    for i, time in enumerate(times):
        if time == 'x':
            continue
        time = int(time)
        if start % time == 0:
            p1 = time
            break
    else:
        start += 1
        continue
    break

p1 *= start - int(data[0])

prod = 1
mods = []
rems = []
for i, time in enumerate(times):
    if time != 'x':
        mods.append(int(time))
        rems.append(-i)

p2 = crt(mods, rems)[0]

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
