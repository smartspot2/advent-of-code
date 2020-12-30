from common.session import AdventSession

session = AdventSession(day=5, year=2017)
data = session.data.strip()
data = list(map(int, data.split()))


def part1():
    jmps = data.copy()
    idx, total = 0, 0
    while 0 <= idx < len(jmps):
        to = jmps[idx]
        jmps[idx] += 1
        idx += to
        total += 1
    return total


def part2():
    jmps = data.copy()
    idx, total = 0, 0
    while 0 <= idx < len(jmps):
        to = jmps[idx]
        jmps[idx] += -1 if to >= 3 else 1
        idx += to
        total += 1
    return total


session.submit(part1(), part=1)
session.submit(part2(), part=2)
