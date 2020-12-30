from collections import *

from sympy import isprime

from common.session import AdventSession

session = AdventSession(day=23, year=2017)
data = session.data.strip()
data = data.split('\n')


class Program:
    def __init__(self):
        self.cur = 0
        self.registers = defaultdict(int)
        self.sent = 0

    def get(self, arg):
        try:
            return int(arg)
        except ValueError:
            return self.registers[arg]

    def run(self):
        mul_count = 0
        while self.cur < len(data):
            op, *args = data[self.cur].split()
            if op == 'set':
                self.registers[args[0]] = self.get(args[1])
            elif op == 'sub':
                self.registers[args[0]] -= self.get(args[1])
            elif op == 'mul':
                self.registers[args[0]] *= self.get(args[1])
                mul_count += 1
            elif op == 'jnz':
                if self.get(args[0]) != 0:
                    self.cur += self.get(args[1])
                    continue
            self.cur += 1
        return mul_count


p1 = Program().run()

B = 106500
C = 123500

p2 = sum(not isprime(b) for b in range(B, C + 1, 17))

session.submit(p1, part=1)
session.submit(p2, part=2)
