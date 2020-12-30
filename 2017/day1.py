from common.session import AdventSession

session = AdventSession(day=1, year=2017)
data = [*map(int, session.data.strip())]


def part1():
    return sum(a for a, b in zip(data, data[1:] + data[:1]) if a == b)


def part2():
    return sum(
        a for a, b in zip(data, data[len(data) // 2:] + data[:len(data) // 2])
        if a == b)


session.submit(part1(), part=1)
session.submit(part2(), part=2)
