import math
import fractions
from collections import defaultdict

from sympy import lcm

with open("day14.in", "r") as f:
    lines = [[chem.split(', ') for chem in line.split(' => ')] for line in f.read().splitlines()]

# key = product, value = (amt created, inputs req)
d = dict()
ore = []
for reactants, product in lines:
    inp = tuple([(int(item.split(' ')[0]), item.split(' ')[1]) for item in reactants])
    out = (int(product[0].split(' ')[0]), product[0].split(' ')[1])
    if inp[0][1] == "ORE":
        ore.append((inp[0][0], out))
    else:
        d[out[1]] = (out[0], inp)

print(d["FUEL"])
q = [*d["FUEL"][1]]
ore_needed = 0
# loop until all left is ORE
while len(q) > 0:
    amt_needed, item = q.pop(0)
    if item == "ORE":
        q.append((amt_needed, item))
        continue
    if item in d:
        num_produced, needed = d[item]
    else:
        # look for in ore, get amt needed
        for num_ore, ore_output in ore:
            if ore_output[1] == item:
                num_rxns = fractions.Fraction(amt_needed, ore_output[0])
                ore_needed += num_rxns * num_ore
                break
        else:
            raise ValueError(f"{item} not in ore!")

        continue

    num_rxns = fractions.Fraction(amt_needed, num_produced)

    for k, name in needed:
        k *= num_rxns
        q.append((k, name))

# Part 1
print(ore_needed)

