import numpy as np

from common.session import AdventSession

session = AdventSession(day=19, year=2017)
data = session.data.strip('\n')
data = data.split('\n')

maxlen = max(len(l) for l in data)
data = np.array([list(f'{l:{maxlen}s}') for l in data])

ROWS, COLS = data.shape
r, c = 0, 0

# find start
for _c in range(COLS):
    if data[r, _c] == '|':
        c = _c
        break

direction = (1, 0)
ADJ = ((0, 1), (0, -1), (1, 0), (-1, 0))
p1, p2 = '', 1
while True:
    if data[r, c].isalpha():
        p1 += data[r, c]
    dr, dc = direction
    if 0 <= r + dr < ROWS and 0 <= c + dc < COLS \
            and data[r + dr, c + dc] != ' ':
        r += dr
        c += dc
        p2 += 1
    else:  # look for turn
        for adjr, adjc in ADJ:
            if dr == -adjr and dc == -adjc:
                continue
            if 0 <= r + adjr < ROWS and 0 <= c + adjc < COLS and \
                    data[r + adjr, c + adjc] != ' ':
                direction = (adjr, adjc)
                break
        else:  # no possible turns left
            break

session.submit(p1, part=1)
session.submit(p2, part=2)
