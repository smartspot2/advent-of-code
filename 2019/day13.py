import numpy as np

from IntCode import IntCode, evaluate_until_input
from Screen import Screen
# import curses
# import time
# screen = curses.initscr()

with open("day13.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)

board = Screen()

it = code.evaluate_step(init={0: 2})

step = None
out = evaluate_until_input(it)
cur_score = 0

for x, y, t in np.array(out).reshape((-1, 3)):
    if (x, y) == (-1, 0):
        cur_score = t
    else:
        board[x, y] = t

# Part 1
print(np.sum(board.to_arr() == 2))

try:
    while np.sum(board.to_arr() == 2) > 0:
        out = evaluate_until_input(it)

        ball_pos, paddle_pos = (-1, -1), (-1, -1)
        for x, y, t in np.array(out).reshape((-1, 3)):
            if (x, y) == (-1, 0):
                cur_score = t
            else:
                board[x, y] = t
            if t == 3:
                paddle_pos = (x, y)
            elif t == 4:
                ball_pos = (x, y)

        code.send(int(np.sign(ball_pos[0] - paddle_pos[0])))
        # board.print(" #+-O")
        # screen.clear()
        # screen.addstr(0, 0, '\n'.join(' '.join(' #+-O'[int(c)] for c in row) for row in board) + '\n\n\n')
        # screen.refresh()
        # time.sleep(0.01)
except StopIteration:
    for x, y, t in np.array(out).reshape((-1, 3)):
        if (x, y) == (-1, 0):
            cur_score = t

print(cur_score)
