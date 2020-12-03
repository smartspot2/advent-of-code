import numpy as np
from collections import *
from itertools import *

from common.session import AdventSession

session = AdventSession(day=1, year=2020)
data = session.data.strip()
# data = data
data = list(map(int, data.split()))


def part1():
    out = 0
    for i, val in enumerate(data):
        for val2 in data[i + 1:]:
            if val + val2 == 2020:
                return val * val2
    return out


def part1_optimized():
    s = set(data)
    for val in data:
        if 2020 - val in s:
            return val * (2020 - val)


# print(part1())


def part2():
    for i, val in enumerate(data):
        for j, val2 in enumerate(data[i + 1:]):
            for val3 in data[j + 1:]:
                if val + val2 + val3 == 2020:
                    return val * val2 * val3


# print(part2())

# response = session.submit(part1(), part=1)
# response = session.submit(part2(), part=2)

# response = session.submit(part1(), part=2)
