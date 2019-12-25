from collections import defaultdict

from IntCode import IntCode, evaluate_until_input
from Screen import Screen

with open("day15.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)

board = Screen()
board[0, 0] = 0

dirs = {(0, 1): 1,
        (0, -1): 2,
        (-1, 0): 3,
        (1, 0): 4}

it = code.evaluate_step()

children = defaultdict(list)
children[(0, 0)] = []
to_visit = [(0, 0)]
next_tovisit = []
pos = (0, 0)
visited = []


def move_to(new_pos, send_code=True):
    global pos
    print(pos, "MOVING TO", new_pos)

    # move from new_pos to root
    new_pos_path = [new_pos]
    while True:
        for d in dirs.keys():
            if new_pos in children[(new_pos[0] + d[0], new_pos[1] + d[1])]:
                new_pos = (new_pos[0] + d[0], new_pos[1] + d[1])
                new_pos_path.insert(0, new_pos)
                break
        else:
            break

    print("NEWPATH", new_pos_path)
    path = []
    while pos not in new_pos_path:
        for d in dirs.keys():
            print("LOOKING AT", (pos[0] + d[0], pos[1] + d[1]))
            print(children[(pos[0] + d[0], pos[1] + d[1])])
            if pos in children[(pos[0] + d[0], pos[1] + d[1])]:
                if send_code:
                    code.send(dirs[d])
                    o = evaluate_until_input(it)
                    assert o == [0], o
                path.append(pos)
                pos = (pos[0] + d[0], pos[1] + d[1])
                break
        else:
            raise ValueError(f"can't get to {new_pos}")
    for coord in new_pos_path[new_pos_path.index(pos) + 1:]:
        d = (coord[0] - pos[0], coord[1] - pos[1])
        if send_code:
            print(f"\t moving to {coord}")
            code.send(dirs[d])
            o = evaluate_until_input(it)
            assert o == [0], o
        path.append(coord)
        pos = coord
    return path


BREAK = False
while not BREAK:
    print(to_visit)
    for node in to_visit:
        move_to(node)
        assert pos == node
        if node in visited:
            continue
        visited.append(node)
        old_pos = pos
        for diff, send_val in dirs.items():
            if pos != old_pos:
                move_to(old_pos)
                assert pos == old_pos

            next_pos = (pos[0] + diff[0], pos[1] + diff[1])
            if pos in children[next_pos]:
                # don't go if we can get back to where we are
                continue
            code.send(send_val)
            out = evaluate_until_input(it)
            if out[0] == 0:  # clear
                next_tovisit.append(next_pos)
                children[pos].append(next_pos)
                pos = next_pos
            elif out[0] == 1:
                pass
            elif out[0] == 2:
                path = move_to((0, 0), send_code=False)
                print(path, len(path), sep="\n")
                BREAK = True
                break

    to_visit = next_tovisit
    next_tovisit = []

