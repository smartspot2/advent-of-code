from IntCode import IntCode, evaluate_until_input
import itertools

with open("day23.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

codes = [IntCode(data, input_list=[n]) for n in range(50)]
iters = [c.evaluate_step() for c in codes]

NAT = [-1, -1]
SENT1 = [-1, -1]
SENT2 = [-1, -1]

idle_comps = set()
for i, it in itertools.cycle(enumerate(iters)):
    out = evaluate_until_input(it)
    if not out:
        codes[i].send(-1)
        idle_comps.add(i)
    else:
        idle_comps -= {i}
        for outi in range(0, len(out), 3):
            to, x, y = out[outi:outi + 3]
            if to == 255:
                if NAT == [-1, -1]:
                    # Part 1
                    print(x, y)
                NAT = [x, y]
            else:
                codes[to].send([x, y])
    if idle_comps == set(range(50)):
        codes[0].send(NAT)
        idle_comps = set()
        SENT1, SENT2 = SENT2, NAT
    if SENT1 == SENT2 and SENT1 != [-1, -1]:
        # Part 2
        print(*SENT1)
        break
