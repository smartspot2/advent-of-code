import matplotlib.pyplot as plt
import numpy as np

from IntCode import IntCode

with open("day11.in", "r") as f:
    data = list(map(int, f.read().strip().split(',')))

dirs = {
    "UP": np.array([0, 1]),
    "DOWN": np.array([0, -1]),
    "LEFT": np.array([-1, 0]),
    "RIGHT": np.array([1, 0])
}

dirlist = ["UP", "RIGHT", "DOWN", "LEFT"]

code = IntCode(data)
rpos = np.array([0, 0])
rdir = "UP"
white = {(0, 0), }
painted_pos = set()

it = code.evaluate_step()
try:
    while True:
        code.send(int(tuple(rpos) in white))
        paint_col = next(it)
        turn = next(it)

        tuppos = tuple(rpos)
        if tuppos in white and paint_col == 0:
            painted_pos.add(tuppos)
            white.remove(tuppos)
        elif tuppos not in white and paint_col == 1:
            painted_pos.add(tuppos)
            white.add(tuppos)

        rdir = dirlist[(dirlist.index(rdir) + 2 * turn - 1) % 4]
        rpos += dirs[rdir]
except StopIteration:
    # Part 1
    print(len(painted_pos))

# Part 2
coords = np.array(tuple(white)).T
minx = min(white, key=lambda p: p[0])[0]
maxx = max(white, key=lambda p: p[0])[0]
miny = min(white, key=lambda p: p[1])[1]
maxy = max(white, key=lambda p: p[1])[1]

grid = np.ones((maxy - miny + 1, maxx - minx + 1))
grid[maxy - coords[1] + miny - 1, coords[0] - minx] = 0

plt.ion()
plt.imshow(grid, cmap="binary")
