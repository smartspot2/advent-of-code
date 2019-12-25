import numpy as np
from sympy import lcm

moons = []

with open("day12.in", "r") as f:
    pos_arr = np.array([[int(p[2:]) for p in line.strip("<>").split(', ')] for line in f.read().splitlines()])
    vel_arr = np.zeros_like(pos_arr)

curstate = np.hstack([pos_arr.T, vel_arr.T])
states = [{tuple(s)} for s in curstate]
repeats = [None] * 3
steps = 0

while not all(repeats):
    vel_arr += np.sum(np.sign(pos_arr - pos_arr[:, np.newaxis]), axis=1)
    pos_arr += vel_arr
    steps += 1

    curstate = np.hstack([pos_arr.T, vel_arr.T])
    for i in range(3):
        if tuple(curstate[i]) in states[i] and repeats[i] is None:
            repeats[i] = steps
        else:
            states[i].add(tuple(curstate[i]))

    if steps == 1000:
        E = np.sum(np.sum(np.abs(pos_arr), axis=1) * np.sum(np.abs(vel_arr), axis=1))
        # Part 1
        print(E)

# Part 2
print(lcm(repeats))

# X: 286332
# Y: 193052
# Z: 102356
