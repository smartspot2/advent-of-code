from common.session import AdventSession

session = AdventSession(day=13, year=2017)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0

lengths = {}
for i, line in enumerate(data):
    depth, length = map(int, line.split(': '))
    severity = depth * length
    lengths[depth] = length
    cycle = 2 * length - 2
    if depth % cycle == 0:
        p1 += severity

delay = 1
while True:
    for depth, length in lengths.items():
        cycle = length + length - 2
        if (depth + delay) % cycle == 0:
            break
    else:
        p2 = delay
        break
    delay += 1

session.submit(p1, part=1)
session.submit(p2, part=2)
