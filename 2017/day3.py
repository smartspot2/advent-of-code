from itertools import *
from math import *

from common.session import AdventSession

session = AdventSession(day=3, year=2017)
data = int(session.data.strip())


def get_x(n):
    s, prev = 0, 0
    for k in range(1, n + 1):
        nxt = int(sin((int(sqrt(4 * (k - 1) + 1)) % 4) * pi / 2))
        s, prev = s + nxt, nxt
    return s


def get_y(n):
    s, prev = 0, 0
    for k in range(1, n + 1):
        nxt = int(cos((int(sqrt(4 * (k - 1) + 1)) % 4) * pi / 2))
        s, prev = s + nxt, nxt
    return s


def part1_short():
    return abs(get_x(data - 1)) + abs(get_y(data - 1))


def sum_neighbors(cur_pos, val_dict):
    s = 0
    for dx, dy in product((-1, 0, 1), repeat=2):
        if dx == dy == 0: continue
        neigh = cur_pos + dx + dy * 1j
        if neigh in val_dict:
            s += val_dict[neigh]
    return s


p2, p2_vals = 0, {0: 1}
cur, direction = 0, -1j
for _ in range(data - 1):
    if cur + (left := direction * 1j) not in p2_vals:  # try going left
        direction = left
    cur += direction
    if p2 == 0:
        p2_vals[cur] = sum_neighbors(cur, p2_vals)
        if p2_vals[cur] > data:
            p2 = p2_vals[cur]
    else:
        p2_vals[cur] = 0  # to keep values from blowing up

p1 = int(abs(cur.real) + abs(cur.imag))

session.submit(p1, part=1)
session.submit(p2, part=2)
