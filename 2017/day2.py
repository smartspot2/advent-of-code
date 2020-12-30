from itertools import *

from common.session import AdventSession

session = AdventSession(2, 2017)
data = session.data.strip()
data = [[*map(int, l.split())] for l in data.strip().splitlines()]

p1 = sum(max(row) - min(row) for row in data)

p2 = sum(val1 // val2 for row in data for val1, val2 in permutations(row, 2)
         if val1 % val2 == 0)

session.submit(p1, 1)
session.submit(p2, 2)
