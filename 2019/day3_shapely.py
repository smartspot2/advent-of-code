from shapely.geometry import LineString
from shapely.ops import split

wires = [[(0, 0)], [(0, 0)]]
dirs = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
with open("day3.in", "r") as f:
    for w, w_data in enumerate(f):
        for instr in w_data.split(','):
            wires[w].append((wires[w][-1][0] + dirs[instr[0]][0] * int(instr[1:]),
                            (wires[w][-1][1] + dirs[instr[0]][1] * int(instr[1:]))))

line1, line2 = LineString(wires[0]), LineString(wires[1])
intersect = line1.intersection(line2)

dists = sorted(abs(p.x) + abs(p.y) for p in intersect)
print(dists[1])
lengths = [split(line1, pt)[0].length + split(line2, pt)[0].length for pt in intersect]
print(min(lengths))
