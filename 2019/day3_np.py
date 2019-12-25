import numpy as np

dirs = {"U": np.array((0, 1)), "D": np.array((0, -1)), "L": np.array((-1, 0)), "R": np.array((1, 0))}

wires = [
    [(0, 0)],
    [(0, 0)]
]

with open("day3.in", "r") as f:
    for w, w_data in enumerate(f):
        pos = np.array((0, 0))
        for instr in w_data.split(','):
            d, amt = dirs[instr[0]], int(instr[1:])
            wires[w].extend(tuple(pos + d * i) for i in range(amt))
            pos += d * amt

intersects = set(wires[0]) & set(wires[1])
intersects.remove((0, 0))

print(min(sum(np.abs(p)) for p in intersects))
print(min(wires[0].index(p) + wires[1].index(p) for p in intersects))
