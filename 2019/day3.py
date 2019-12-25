from numpy import *

with open("day3.in", "r") as f:
    wire1 = f.readline().strip().split(',')
    wire2 = f.readline().strip().split(',')

dirs = {
    "D": (0, -1),
    "U": (0, 1),
    "R": (1, 0),
    "L": (-1, 0)
}

wire1_points = [(0, 0)]
for instr in wire1:
    x, y = wire1_points[-1]
    dx, dy = dirs[instr[0]]
    amt = int(instr[1:])
    wire1_points.append((x + amt * dx, y + amt * dy))

wire2_points = [(0, 0)]
for instr in wire2:
    x, y = wire2_points[-1]
    dx, dy = dirs[instr[0]]
    amt = int(instr[1:])
    wire2_points.append((x + amt * dx, y + amt * dy))


from shapely.geometry import LineString
from shapely.ops import split

line1 = LineString(wire1_points)
line2 = LineString(wire2_points)

intsct = (line1.intersection(line2))

l = []
for pt in intsct:
    seg1 = split(line1, pt)
    seg2 = split(line2, pt)
    l.append(seg1[0].length + seg2[0].length)

print(sorted(l))

# all_intscts = []
# for i in range(len(wire1_points) - 1):
#     for j in range(len(wire2_points) - 1):
#         intsct = seg_intersect(array(wire1_points[i]), array(wire1_points[i + 1]),
#                                array(wire2_points[j]), array(wire2_points[j + 1]))
#         if intsct:
#             all_intscts.append(intsct)
