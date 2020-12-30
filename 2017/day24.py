from functools import *

from common.session import AdventSession

session = AdventSession(day=24, year=2017)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0

components = set()
for i, line in enumerate(data):
    first, second = line.split('/')
    components.add((int(first), int(second)))


@cache
def strongest(cur, used=None):
    if used is None:
        used = frozenset()
    max_sum = 0
    for c in components:
        if c in used:
            continue
        if cur in c:
            other = c[1] if c[0] == cur else c[0]
            max_sum = max(strongest(other, used=used | {c}), max_sum)
    return cur if max_sum == 0 else max_sum + 2 * cur


@cache
def longest(cur, used=None):
    if used is None:
        used = frozenset()
    max_len, max_sum = 0, 0
    for c in components:
        if c in used:
            continue
        if cur in c:
            other = c[1] if c[0] == cur else c[0]
            next_len, next_sum = longest(other, used=used | {c})
            if next_len > max_len:
                max_len = next_len
                max_sum = next_sum
            elif next_len == max_len:
                max_sum = max(max_sum, next_sum)
    final_sum = cur if max_sum == 0 else max_sum + 2 * cur
    return max_len + 1, final_sum


p1 = strongest(0)
length, p2 = longest(0)

session.submit(p1, part=1)
session.submit(p2, part=2)
