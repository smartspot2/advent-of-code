from common.session import AdventSession

session = AdventSession(day=9, year=2017)
data = session.data.strip()

p1, p2 = 0, 0

garbage = False
depth = 0
i = 0
while i < len(data):
    char = data[i]
    if not garbage:
        if char == '<':
            garbage = True
        elif char == '{':
            depth += 1
        elif char == '}':
            p1 += depth
            depth -= 1
    else:
        if char == '!':
            i += 2
            continue
        elif char == '>':
            garbage = False
        else:
            p2 += 1
    i += 1

session.submit(p1, part=1)
session.submit(p2, part=2)
