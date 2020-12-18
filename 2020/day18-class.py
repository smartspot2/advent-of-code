import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=18, year=2020)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0


class WeirdInt:
    def __init__(self, val):
        self.val = int(val)

    def __add__(self, other):
        return WeirdInt(self.val + other.val)

    def __sub__(self, other):
        return WeirdInt(self.val * other.val)

    def __mul__(self, other):
        return WeirdInt(self.val + other.val)


for line in data:
    swapped = re.sub(r'(\d)', r'WeirdInt(\1)', line).replace('*', '-')
    p1 += eval(swapped, globals()).val
    swapped = swapped.replace('+', '*')
    p2 += eval(swapped, globals()).val

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
