import numpy as np

from common.session import AdventSession

# import networkx as nx

session = AdventSession(day=21, year=2017)
data = session.data.strip()
# data = session.test_data.strip()
data = data.split('\n')
# data = list(map(int, data.split()))

p1, p2 = 0, 0

rules2 = dict()
rules3 = dict()


def parse(s):
    return np.array([[c == '#' for c in l] for l in s.split('/')], dtype=int)


def encode(arr):
    return '/'.join(''.join('.#'[int(c)] for c in row) for row in arr)


def orientations(s):
    arr = parse(s)
    for _ in range(2):
        arr = np.fliplr(arr)
        for _ in range(4):
            arr = np.rot90(arr)
            yield encode(arr)


for line in data:
    fr, to = line.split(' => ')
    if fr.count('/') == 1:
        for s in orientations(fr):
            rules2[s] = parse(to)
    else:
        for s in orientations(fr):
            rules3[s] = parse(to)


def iteration(arr):
    rows, cols = arr.shape
    if rows % 2 == 0:
        diff = 2
        ruledict = rules2
    else:
        diff = 3
        ruledict = rules3

    nxt = None
    for r in range(0, rows, diff):
        newrow = None
        for c in range(0, cols, diff):
            sub = arr[r:r + diff, c:c + diff]
            new = ruledict[encode(sub)]
            newrow = new if newrow is None else np.hstack([newrow, new])
        nxt = newrow if nxt is None else np.vstack([nxt, newrow])
    return nxt


patt = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
for it in range(18):
    patt = iteration(patt)
    if it == 4:
        p1 = np.sum(patt)

p2 = np.sum(patt)

session.submit(p1, part=1)
session.submit(p2, part=2)
