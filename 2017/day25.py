from collections import *

from common.session import AdventSession

session = AdventSession(day=25, year=2017)
data = session.data.strip()
data = data.split('\n\n')

states = {}

preamble = data[0].split('\n')
BEGIN_STATE = preamble[0].split()[-1][:-1]
MAX_STEPS = int(preamble[1].split()[-2])

movement = {'right': 1, 'left': -1}
for desc in data[1:]:
    (state, if0, write_if0, move_if0, continue_if0,
     if1, write_if1, move_if1, continue_if1) = \
        [line.strip('.') for line in desc.split('\n')]

    states[state[-2]] = [
        (int(write_if0[-1]), movement[move_if0.split()[-1]], continue_if0[-1]),
        (int(write_if1[-1]), movement[move_if1.split()[-1]], continue_if1[-1])
    ]


class Turing:
    def __init__(self, init_state):
        self.state = init_state
        self.ptr = 0
        self.tape = defaultdict(int)

    def run(self, steps):
        for _ in range(steps):
            cur = self.tape[self.ptr]
            write, move, cont = states[self.state][cur]
            self.tape[self.ptr] = write
            self.ptr += move
            self.state = cont
        return sum(self.tape.values())


t = Turing(BEGIN_STATE)
p1 = t.run(MAX_STEPS)

session.submit(p1, part=1)
