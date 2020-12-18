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


def findmatch(expr, i):
    match = 0
    while i < len(expr):
        if expr[i] == '(':
            match += 1
        elif expr[i] == ')':
            match -= 1
            if match == 0:
                return i
        i += 1


def evaluate(expr):
    i = 0
    while i < len(expr) and len(expr) > 1:
        if i - 1 >= 0 and expr[i - 1].isdigit() and expr[i + 1].isdigit() and \
                not expr[i].isdigit():
            expr[i - 1:i + 2] = [str(eval(''.join(expr[i - 1:i + 2])))]
            i = 0
        elif expr[i] == '(':
            end = findmatch(expr, i)
            expr[i:end + 1] = [evaluate(expr[i + 1:end])]
            i = 0
        i += 1
    return expr[0]


def evaluate2(expr):
    for op in ('+', '*'):
        i = 0
        while i < len(expr) and len(expr) > 1:
            if i - 1 >= 0 and expr[i - 1].isdigit() and expr[i] == op and \
                    expr[i + 1].isdigit():
                expr[i - 1:i + 2] = [str(eval(''.join(expr[i - 1:i + 2])))]
                i = 0
            elif expr[i] == '(':
                end = findmatch(expr, i)
                expr[i:end + 1] = [evaluate2(expr[i + 1:end])]
                i = 0
            i += 1
    return expr[0]


for line in data:
    p1 += int(evaluate([c for c in line if c != ' ']))
    p2 += int(evaluate2([c for c in line if c != ' ']))

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
