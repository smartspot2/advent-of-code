import numpy as np
# import networkx as nx
from collections import *
from itertools import *

from common.session import AdventSession

session = AdventSession(day=4, year=2020)
data = session.data.strip()
data = data.split('\n\n')
# data = list(map(int, data.split()))

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = []


def part1():
    out = 0
    for passport in data:
        cur = passport.split()
        d = dict()
        present = []
        for key, val in [x.split(':') for x in cur]:
            d[key] = val
            present.append(key)
        p = [x for x in present if x != 'cid']
        if len(set(p)) >= len(set(fields)):
            out += 1
    return out


print(part1())


def part2():
    out = 0
    for passport in data:
        cur = passport.split()
        d = dict()
        present = []
        numvalid = 0
        for key, val in [x.split(':') for x in cur]:
            d[key] = val
            present.append(key)
            key = key.strip()
            val = val.strip()
            if key == 'byr':
                numvalid += 1920 <= int(val) <= 2002
            elif key == 'iyr':
                numvalid += 2010 <= int(val) <= 2020
            elif key == 'eyr':
                numvalid += 2020 <= int(val) <= 2030
            elif key == 'hgt':
                if val.endswith('cm'):
                    numvalid += 150 <= int(val[:-2]) <= 193
                elif val.endswith('in'):
                    numvalid += 59 <= int(val[:-2]) <= 76
            elif key == 'hcl':
                numvalid += val[0] == '#' and all(
                    c in '0123456789abcdef' for c in val[1:])
            elif key == 'ecl':
                numvalid += val in ('amb', 'blu', 'brn', 'gry',
                                    'grn', 'hzl', 'oth')
            elif key == 'pid':
                numvalid += len(val) == 9 and val.isdigit()
        p = [x for x in present if x != 'cid']
        if len(set(p)) >= len(set(fields)) and numvalid >= 7:
            out += 1
    return out


print(part2())

# session.submit(part1(), part=1)
# session.submit(part2(), part=2)

# session.submit(part1(), part=2)
