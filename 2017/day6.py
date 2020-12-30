from common.session import AdventSession

session = AdventSession(day=6, year=2017)
data = session.data.strip()
data = data
data = list(map(int, data.split()))


def serialize(lst):
    return '|'.join(map(str, lst))


banks = data.copy()
seen = {}

out = 0
while (ser := serialize(banks)) not in seen:
    seen[ser] = out
    idx = banks.index(max(banks))
    left, banks[idx] = banks[idx], 0
    idx = (idx + 1) % len(banks)
    out += 1
    while left > 0:  # distribute
        banks[idx] += 1
        left -= 1
        idx = (idx + 1) % len(banks)

p1 = out
p2 = out - seen[ser]

session.submit(p1, part=1)
session.submit(p2, part=2)
