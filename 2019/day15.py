from collections import defaultdict

from matplotlib import pyplot as plt

from IntCode import IntCode, evaluate_until_input
from Screen import Screen

with open("day15.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)
it = code.evaluate_step()

dirs = {(-1, 0): 3,
        (0, 1): 1,
        (0, -1): 2,
        (1, 0): 4}
start_pos = (0, 0)
pos = (0, 0)
board = Screen(default_factory=lambda: -1)
board[0, 0] = 1

path = [(0, 0)]
dirs_to_visit = {(0, 0): [p for p in dirs]}
dirs_to_visit = defaultdict(list, dirs_to_visit)

# plt.ion()
while True:
    if dirs_to_visit[pos]:
        curdir = dirs_to_visit[pos].pop(0)
        code.send(dirs[curdir])
        out = evaluate_until_input(it)
        nextpos = (pos[0] + curdir[0], pos[1] + curdir[1])

        if out[0] == 1:
            pos = nextpos
            board[pos] = 1
            path.append(pos)
            dirs_to_visit[pos] = [p for p in dirs if p != (-curdir[0], -curdir[1])]
        elif out[0] == 0:
            board[nextpos] = 0
        elif out[0] == 2:
            pos = nextpos
            board[pos] = 2
            path.append(pos)
            start_pos = pos
            # Part 1
            print(len(path) - 1)
    else:
        path.pop(-1)
        if len(path) == 0:
            break
        prev = path[-1]
        diff = (prev[0] - pos[0], prev[1] - pos[1])
        code.send(dirs[diff])
        out = evaluate_until_input(it)
        assert out[0] == 1
        pos = prev

    # Visualization
    # plt.cla()
    # plt.imshow(board.to_arr(highlight=path, highlightval=3))
    # plt.pause(0.001)

# screen.print("# O")
to_visit = [(start_pos[0] + d[0], start_pos[1] + d[1]) for d in dirs]
next_tovisit = []
visited = set()
iterations = 0
while to_visit:
    for coord in to_visit:
        if board[coord] == 1 and coord not in visited:  # clear
            next_tovisit.extend([(coord[0] + d[0], coord[1] + d[1]) for d in dirs])
            board[coord] = 3
        visited.add(coord)
    to_visit = next_tovisit
    next_tovisit = []
    iterations += 1
    # print(f"iteration {iterations}")
    # screen.print("#.O ", flip=False)

    # Visualization
    # plt.cla()
    # plt.imshow(board.to_arr())
    # plt.pause(0.02)

# Part 2
print(iterations - 1)


