from common.session import AdventSession

session = AdventSession(day=16, year=2017)
data = session.data.strip()
data = data.split(',')

p1 = ''
lst = list('abcdefghijklmnop')

seen = [''.join(lst)]
for dance in range(1_000_000_000):
    for i, instr in enumerate(data):
        move = instr[0]
        if move == 's':
            num = int(instr[1:])
            lst = lst[-num:] + lst[:-num]
        elif move == 'x':
            a, b = map(int, instr[1:].split('/'))
            lst[a], lst[b] = lst[b], lst[a]
        elif move == 'p':
            a, b = instr[1:].split('/')
            a, b = lst.index(a), lst.index(b)
            lst[a], lst[b] = lst[b], lst[a]
    s = ''.join(lst)
    if not p1:
        p1 = s
    if s in seen:
        break
    seen.append(s)

p2 = ''.join(seen[1_000_000_000 % len(seen)])

session.submit(p1, part=1)
session.submit(p2, part=2)
