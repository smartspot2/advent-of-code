from common.session import AdventSession

session = AdventSession(day=15, year=2017)
data = session.data.strip()
gen1, gen2 = data.split('\n')

p1, p2 = 0, 0

gen1, gen2 = int(gen1.split()[-1]), int(gen2.split()[-1])
gen1_factor, gen2_factor = 16807, 48271
div_factor = 2147483647
last_16 = 0xffff


def generator(start, mult_factor, mod=None):
    while True:
        start *= mult_factor
        start = (start & div_factor) + (start >> 31)
        if start >> 31:
            start -= div_factor
        if mod is None or not (start & mod):
            yield start


gens = zip(generator(gen1, gen1_factor), generator(gen2, gen2_factor))
for i, (a, b) in enumerate(gens):
    if i == 40_000_000:
        break
    if a & last_16 == b & last_16:
        p1 += 1

session.submit(p1, part=1)

gens = zip(generator(gen1, gen1_factor, 0b11),
           generator(gen2, gen2_factor, 0b111))
for i, (a, b) in enumerate(gens):
    if i == 5_000_000:
        break
    if a & last_16 == b & last_16:
        p2 += 1

session.submit(p2, part=2)
