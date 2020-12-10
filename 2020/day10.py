import numpy as np
# import networkx as nx
from collections import *
from itertools import *
import re
from functools import lru_cache

from common.session import AdventSession

session = AdventSession(day=10, year=2020)
data = session.data.strip()
data = [0] + sorted(map(int, data.split()))

p1, p2 = 0, 0

diffs = {1: 0, 2: 0, 3: 1}
for v1, v2 in zip(data, data[1:]):
    diffs[v2 - v1] += 1

p1 = diffs[1] * diffs[3]

possible = dict()

for v in data:
    possible[v] = [v + dv for dv in (1, 2, 3) if v + dv in data]


@lru_cache(maxsize=None)
def recur(v):
    if v == data[-1]:
        return 1
    return sum(recur(x) for x in possible[v])


p2 = recur(0)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)

(lambda f,g,d:print(f(d,1)*(f(d,3)+1),g(g,d,0)))(lambda d,k:sum(b-a==k for a,b in zip(d,d[1:])),lambda g,d,k,v={}:sum(j in v and v[j]or j==d[-1]or v.update({j:(e:=g(g,d,j,v))})or e for x in(1,2,3)if(j:=k+x)in d),[0,*sorted(map(int,open('day10.in')))])
