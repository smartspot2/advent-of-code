from collections import *

from common.session import AdventSession

session = AdventSession(day=8, year=2017)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0

registers = defaultdict(int)

for i, line in enumerate(data):
    line = line.replace('inc', '+=').replace('dec', '-=')
    line += 'else 0'
    exec(line, {}, registers)
    p2 = max(p2, max(registers.values()))

p1 = max(registers.values())

session.submit(p1, part=1)
session.submit(p2, part=2)
