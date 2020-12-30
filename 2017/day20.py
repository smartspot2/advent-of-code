from collections import *

import numpy as np

from common.session import AdventSession

session = AdventSession(day=20, year=2017)
data = session.data.strip()
data = data.split('\n')

p1, p2 = 0, 0


class Particle:
    def __init__(self, p, v, a, _id):
        self.p = np.array(p)
        self.v = np.array(v)
        self.a = np.array(a)
        self.p_sum = np.abs(p).sum()
        self.v_sum = np.abs(v).sum()
        self.a_sum = np.abs(a).sum()
        self.id = _id

    def update(self):
        self.v += self.a
        self.p += self.v


particles = []
for i, line in enumerate(data):
    line = line.replace('<', '(').replace('>', ')')
    particles.append(eval(f'Particle({line}, _id={i})'))

sorted_particles = sorted(particles, key=lambda p: (
    p.a_sum, p.v_sum, p.p_sum))

p1 = sorted_particles[0].id

for _ in range(1000):
    positions = defaultdict(list)
    for p in particles:
        positions[tuple(p.p)].append(p)
    for parts in positions.values():
        if len(parts) > 1:
            for part in parts:
                particles.remove(part)

    for p in particles:
        p.update()

p2 = len(particles)

session.submit(p1, part=1)
session.submit(p2, part=2)
