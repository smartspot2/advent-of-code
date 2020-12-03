import numpy as np
from collections import *
from itertools import *

from common.session import AdventSession

session = AdventSession(day=2, year=2020)
data = session.data.strip()


def part1():
    out = 0
    for i, line in enumerate(data.splitlines()):
        policy, char, pwd = line.split()
        lo, hi = list(map(int, policy.split('-')))
        char = char[:-1]
        if lo <= pwd.count(char) <= hi:
            out += 1
    return out


part1_oneline = sum((lambda lo, hi: lo <= pwd.count(char[:-1]) <= hi)(*map(int, policy.split('-'))) for policy, char, pwd in [line.split() for line in data.splitlines()])

print(part1())
print(part1_oneline)


def part2():
    out = 0
    for i, line in enumerate(data.splitlines()):
        policy, char, pwd = line.split()
        lo, hi = list(map(int, policy.split('-')))
        char = char[:-1]
        if (pwd[lo - 1] == char) ^ (pwd[hi - 1] == char):
            out += 1
    return out


part2_oneline = sum((lambda lo, hi: (pwd[lo - 1] == char[:-1]) ^ (pwd[hi - 1] == char[:-1]))(*map(int, policy.split('-'))) for policy, char, pwd in [line.split() for line in data.splitlines()])


print(part2())
print(part2_oneline)

# session.submit(part1(), part=1)
# session.submit(part2(), part=2)

# session.submit(part1(), part=2)

# part1_short = sum((lambda l, h: l <= w.count(c[:-1]) <= h)(*map(int, p.split('-'))) for p, c, w in [x.split() for x in data.split('\n')])
# part2_short = sum((lambda l, h: (w[l - 1] == c[:-1]) ^ (w[h - 1] == c[:-1]))(*map(int, p.split('-'))) for p, c, w in [line.split() for line in data.split('\n')])
#
# print(*map(sum, zip(*[(lambda l, h: (l <= w.count(c[:-1]) <= h, (w[l - 1] == c[:-1]) ^ (w[h - 1] == c[:-1])))(*map(int, p.split('-'))) for p, c, w in [x.split() for x in data.split('\n')]])))
# print(*map(sum, zip(*[(lambda l, h: (l <= w.count(c[:-1]) <= h, (w[l - 1] == c[:-1]) ^ (w[h - 1] == c[:-1])))(*map(int, p.split('-'))) for p, c, w in [x.split() for x in open('day2.in').readlines()]])))