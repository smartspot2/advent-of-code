import numpy as np
from scipy.signal import convolve

with open('day24.in', 'r') as f:
    data = np.array([list(l) for l in f.read().splitlines()])

board = np.array(data == '#', dtype=int)


prevboards = set()
while str(board) not in prevboards:
    prevboards.add(str(board))
    ADJ = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    counts = convolve(board, ADJ, mode='same')
    new_board = np.zeros_like(board)
    for r, c in np.ndindex(*counts.shape):
        if board[r, c] and counts[r, c] != 1:
            new_board[r, c] = 0
        elif not board[r, c] and counts[r, c] in (1, 2):
            new_board[r, c] = 1
        elif board[r, c]:
            new_board[r, c] = 1
    board = new_board

rating = 0
p = 1
for r, c in np.ndindex(*board.shape):
    rating += p * board[r, c]
    p *= 2
print(rating)
