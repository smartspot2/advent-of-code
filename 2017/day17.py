from common.session import AdventSession

session = AdventSession(day=17, year=2017)
step = int(session.data.strip())

p1, p2 = 0, 0

cur = 0
lst = [0]
for val in range(1, 2018):
    cur = (cur + step) % val + 1
    lst.insert(cur, val)

p1 = lst[(cur + 1) % len(lst)]

cur = 0
nxt = 0
for val in range(1, 50000001):
    cur = (cur + step) % val + 1
    if cur == 1:
        nxt = val

p2 = nxt

session.submit(p1, part=1)
session.submit(p2, part=2)
