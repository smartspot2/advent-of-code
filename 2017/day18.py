from collections import *

from common.session import AdventSession

session = AdventSession(day=18, year=2017)
data = session.data.strip()
data = data.split('\n')


class Program:
    all_programs = {}

    def __init__(self, _id):
        self.cur = 0
        self.registers = defaultdict(int)
        self.id = _id
        self.registers['p'] = _id
        Program.all_programs[_id] = self
        self.q = []
        self.waiting = False
        self.done = False
        self.sent = 0

    def get(self, arg):
        try:
            return int(arg)
        except ValueError:
            return self.registers[arg]

    def send(self, val, to=None):
        if to is None:
            to = 1 - self.id
        self.sent += 1
        Program.all_programs[to].q.append(val)

    def run(self, part=1):
        if self.q:
            self.waiting = False
        while not self.waiting and self.cur < len(data):
            op, *args = data[self.cur].split()
            if op == 'snd':
                if part == 1:
                    self.sent = self.get(args[0])
                else:
                    self.send(self.get(args[0]))
            elif op == 'set':
                self.registers[args[0]] = self.get(args[1])
            elif op == 'add':
                self.registers[args[0]] += self.get(args[1])
            elif op == 'mul':
                self.registers[args[0]] *= self.get(args[1])
            elif op == 'mod':
                self.registers[args[0]] %= self.get(args[1])
            elif op == 'rcv':
                if part == 1:
                    if self.get(args[0]) != 0:
                        return self.sent
                else:
                    if self.q:
                        self.registers[args[0]] = self.q.pop(0)
                    else:
                        self.waiting = True
                        break
            elif op == 'jgz':
                if self.get(args[0]) > 0:
                    self.cur += self.get(args[1])
                    continue
            self.cur += 1
        if self.cur >= len(data):
            self.done = True


prog = Program(0)
p1 = prog.run(part=1)

prog0 = Program(0)
prog1 = Program(1)

while not (prog0.done and prog1.done):
    prog0.run(part=2)
    prog1.run(part=2)
    if prog0.q:
        continue
    break

p2 = prog1.sent

session.submit(p1, part=1)
session.submit(p2, part=2)
