from common.session import AdventSession

session = AdventSession(day=7, year=2017)
data = session.data.strip()
data = data.split('\n')

towers = dict()  # name: what's above name
towers_back = dict()  # anme: what's below name
weights = dict()  # name: weight of program

for i, val in enumerate(data):
    spl = val.split()
    name = spl[0]
    weight = int(spl[1][1:-1])
    if '->' in val:
        towers[name] = [n.strip(',') for n in spl[3:]]
        for tower in towers[name]:  # backwards
            towers_back[tower] = name
    weights[name] = weight

p1 = list(towers.keys())[0]
while p1 in towers_back:
    p1 = towers_back[p1]

stacks = dict()


def weight_sum(t):
    if t in stacks:
        return stacks[t]
    if t not in towers:
        stacks[t] = weights[t]
        return weights[t]
    stacks[t] = sum(map(weight_sum, towers[t])) + weights[t]
    return stacks[t]


unbalanced = [tower for tower in towers
              if len(set(map(weight_sum, towers[tower]))) != 1]

p2 = 0
for tower in unbalanced:
    if all(t not in unbalanced for t in towers[tower]):
        cur_weights = [*map(weight_sum, towers[tower])]
        possible = list(set(cur_weights))
        wrong = possible[0] != 1
        idx = cur_weights.index(possible[wrong])
        wrong_tower = towers[tower][idx]
        diff = possible[1 - wrong] - possible[wrong]
        p2 = weights[wrong_tower] + diff
        break

session.submit(p1, part=1)
session.submit(p2, part=2)
