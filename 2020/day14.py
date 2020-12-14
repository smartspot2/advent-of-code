import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=14, year=2020)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0

mem = dict()

curmask = ''
for i, line in enumerate(data):
    if line.startswith('mask'):
        curmask = line.split(' = ')[1]
    else:
        _, addr, _, curwrite = re.split(r'[\[\]=]', line)
        curwrite = f"{int(curwrite):036b}"
        res = ''.join(write if mask == 'X' else mask
                      for mask, write in zip(curmask, curwrite))
        mem[int(addr)] = int(res, 2)

p1 = sum(mem.values())

mem = dict()

curmask = ''
for i, line in enumerate(data):
    if line.startswith('mask'):
        curmask = line.split(' = ')[1]
    else:
        _, addr, _, curwrite = re.split(r'[\[\]=]', line)
        addr = f"{int(addr):036b}"
        res = ''.join(mask if mask in '1X' else write
                      for mask, write in zip(curmask, addr)).replace('X', '{}')
        cnt = curmask.count('X')
        for b in range(2 ** cnt):
            mem[int(res.format(*f'{b:0{cnt}b}'), 2)] = int(curwrite)

p2 = sum(mem.values())

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
