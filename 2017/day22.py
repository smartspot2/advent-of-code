from common.session import AdventSession
from common.utils.numpy_utils import str_to_array

session = AdventSession(day=22, year=2017)
data = session.data.strip()
data = str_to_array(data)


def simulate(bursts, part1=True):
    weakened = set()
    infected = set()
    flagged = set()

    for r, row in enumerate(data):
        for c, el in enumerate(row):
            if el:
                infected.add(r * 1j + c)

    rows, cols = data.shape
    pos = (rows // 2) * 1j + (cols // 2)
    facing = -1j
    res = 0

    for i in range(bursts):
        if part1:
            if pos in infected:
                facing *= 1j  # flipped because +r is down
                infected.remove(pos)
            else:
                facing *= -1j
                infected.add(pos)
                res += 1
        else:
            if pos in weakened:
                weakened.remove(pos)
                infected.add(pos)
                res += 1
            elif pos in infected:
                infected.remove(pos)
                flagged.add(pos)
                facing *= 1j  # flipped because +r is down
            elif pos in flagged:
                flagged.remove(pos)
                facing *= -1
            else:
                weakened.add(pos)
                facing *= -1j
        pos += facing
    return res


p1 = simulate(10_000, part1=True)
p2 = simulate(10_000_000, part1=False)

session.submit(p1, part=1)
session.submit(p2, part=2)
