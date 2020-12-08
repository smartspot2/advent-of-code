import numpy as np
# import networkx as nx
from collections import *
from itertools import *
import re

from common.session import AdventSession

session = AdventSession(day=8, year=2020)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0


def part1():
    acc = 0
    idx = 0

    visited = set()

    while idx < len(data):
        if idx in visited:
            return acc
        visited.add(idx)
        line = data[idx]
        instr, arg = line.split()
        arg = int(arg)
        if instr == 'acc':
            acc += arg
            idx += 1
        elif instr == 'jmp':
            idx += arg
        else:
            idx += 1


def try_val(i):
    acc = 0
    idx = 0

    visited = set()

    while idx < len(data):
        if idx in visited:
            break
        visited.add(idx)
        line = data[idx]
        instr, arg = line.split()
        arg = int(arg)
        if idx == i:
            if instr == 'jmp':
                instr = 'nop'
            elif instr == 'nop':
                instr = 'jmp'
            else:
                return False
        if instr == 'acc':
            acc += arg
            idx += 1
        elif instr == 'jmp':
            idx += arg
        else:
            idx += 1
    else:
        return acc


def part2():
    for i in range(len(data)):
        res = try_val(i)
        if res:
            return res


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
