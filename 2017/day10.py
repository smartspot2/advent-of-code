from common.session import AdventSession
from knot_hash import *

session = AdventSession(day=10, year=2017)
data = session.data.strip()
data = [*map(int, data.split(','))]

seq, *_ = knot_hash_round(data, list(range(256)), 0, 0)
p1 = seq[0] * seq[1]
p2 = knot_hash(session.data.strip())

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

session.submit(p1, part=1)
session.submit(p2, part=2)
