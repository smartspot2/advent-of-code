from common.session import AdventSession

session = AdventSession(day=11, year=2017)
data = session.data.strip()
data = data.split(',')

p2 = 0

repl = {
    'nw': 1j,
    'ne': 1,
    'sw': -1,
    'se': -1j,
    'n': 1 + 1j,
    's': -1 - 1j
}

seq = []
for step in data:
    seq.append(repl[step])
    cur = sum(seq)
    cur = int(max(abs(cur.imag), abs(cur.real)))
    p2 = max(p2, cur)

p1 = sum(seq)
p1 = int(max(abs(p1.imag), abs(p1.real)))

session.submit(p1, part=1)
session.submit(p2, part=2)
