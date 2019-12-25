import numpy as np

with open('day24.in', 'r') as f:
    data = np.array([list(l) for l in f.read().splitlines()])

board = np.array(data == '#', dtype=int)


boards = dict()
boards[0] = board
ADJ = [(0, -1), (0, 1), (1, 0), (-1, 0)]

LOOKDOWNDICT = {
    (-1, 0): [(4, k) for k in range(5)],
    (1, 0): [(0, k) for k in range(5)],
    (0, -1): [(k, 4) for k in range(5)],
    (0, 1): [(k, 0) for k in range(5)]
}

LOOKUPDICT = {
    (-1, 0): (1, 2),
    (1, 0): (3, 2),
    (0, -1): (2, 1),
    (0, 1): (2, 3)
}


def newboard():
    return np.zeros((5, 5), dtype=int)


for _ in range(200):
    new_boards = dict()
    if np.sum(boards[max(boards.keys())]):
        boards[max(boards.keys()) + 1] = newboard()
    if np.sum(boards[min(boards.keys())]):
        boards[min(boards.keys()) - 1] = newboard()
    for level in range(min(boards.keys()), max(boards.keys()) + 1):
        new_boards[level] = newboard()
        if level not in boards:
            boards[level] = newboard()
        for r, c in np.ndindex(*board.shape):
            if (r, c) == (2, 2):
                continue
            count = 0
            for dr, dc in ADJ:
                newr, newc = r + dr, c + dc
                if (newr, newc) == (2, 2):
                    lookpos_list = LOOKDOWNDICT[dr, dc]
                    if level - 1 not in boards:
                        boards[level - 1] = np.zeros((5, 5), dtype=int)
                    count += sum(boards[level - 1][lookpos] for lookpos in lookpos_list)
                elif newr < 0 or newr >= 5 or newc < 0 or newc >= 5:
                    lookpos = LOOKUPDICT[dr, dc]
                    if level + 1 not in boards:
                        boards[level + 1] = np.zeros((5, 5), dtype=int)
                    count += boards[level + 1][lookpos]
                else:
                    count += boards[level][newr, newc]
            if boards[level][r, c] and count != 1:
                new_boards[level][r, c] = 0
            elif not boards[level][r, c] and count in (1, 2):
                new_boards[level][r, c] = 1
            else:
                new_boards[level][r, c] = boards[level][r, c]
    boards = new_boards

s = 0
for b in boards.values():
    s += np.sum(b)
print(s)
