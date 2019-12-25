import numpy as np
from scipy.signal import convolve2d

from IntCode import IntCode

with open("day17.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)

# Part 1

out = code.evaluate()
arr = np.array([list(x) for x in ''.join(chr(c) for c in out).split()])

conv = convolve2d(np.isin(arr, list('#<>^v')), [[0, 1, 0], [1, 0, 1], [0, 1, 0]], mode='same')
alignsum = sum(a * b for a, b in np.argwhere(conv == 4))

print(alignsum)

# Part 2

pos = np.argwhere(np.isin(arr, list('<>^v')))[0]  # get pos of robot
instr = [0]
dirs = dict(zip([1j, -1j, 1, -1], map(np.array, [(-1, 0), (1, 0), (0, 1), (0, -1)])))  # map complex to array
curdir = [1j, -1j, 1, -1]['^v><'.index(arr[tuple(pos)])]  # get dir from char
valid_index = lambda p: 0 <= p[0] < arr.shape[0] and 0 <= p[1] < arr.shape[1]
while True:
    if valid_index(pos + dirs[curdir]) and arr[tuple(pos + dirs[curdir])] == '#':  # forward
        instr[-1] += 1
    elif valid_index(pos + dirs[curdir * 1j]) and arr[tuple(pos + dirs[curdir * 1j])] == '#':  # left
        instr.extend(['L', 1])
        curdir *= 1j
    elif valid_index(pos + dirs[curdir * -1j]) and arr[tuple(pos + dirs[curdir * -1j])] == '#':  # right
        instr.extend(['R', 1])
        curdir *= -1j
    else:
        break
    pos += dirs[curdir]

instr = list(map(str, instr if instr[0] != 0 else instr[1:]))
instr_str = ','.join(instr)


# Tweaked a bit from day17p2_prog, still fiddling with it
def find_segments():
    prnt = 1
    for endA in range(10):
        a = ','.join(instr[:endA + 1])
        if len(a) > 20:
            # print(a)
            continue
        b_instr_str = instr_str.replace(a, 'A')
        b_instr = b_instr_str.split(',')

        start_b = b_instr.index(b_instr_str.lstrip('A,').split(',')[0])  # index of first non-A
        endrange_b = min(start_b + 10, len(b_instr))  # 10 long or end of string
        if 'A' in b_instr[start_b:]:  # index of first A after first non-A
            endrange_b = min(endrange_b, b_instr.index('A', start_b))
        for endB in range(start_b, endrange_b):  # loop through all B (first non-A chunk)
            b = ','.join(b_instr[start_b:endB + 1])
            if len(b) > 20:
                print('b long', a, '//', b, '//', c)
                continue
            c_instr_str = b_instr_str.replace(b, 'B')
            c_instr = c_instr_str.split(',')

            # print('c', c_instr_str)
            start_c = c_instr.index(c_instr_str.lstrip('AB,').split(',')[0])  # index of first non-A,B
            endrange_c = min(start_c + 10, len(c_instr))  # 10 long or end of string
            if 'A' in c_instr[start_c:]:  # index of first A after first non-A,B
                endrange_c = min(endrange_c, c_instr.index('A', start_c))
            if 'B' in c_instr[start_c:]:  # index of first B after first non-A,B
                endrange_c = min(endrange_c, c_instr.index('B', start_c))
            # print([start_c + (endrange_c - start_c) >> k for k in range((endrange_c - start_c) // 2)])
            for endC in set([start_c + c_len for k in range((endrange_c - start_c) // 2) if
                             (c_len := (endrange_c - start_c) >> k) != 0]):
                c = ','.join(c_instr[start_c:endC])  # C has to be first non-A,B chunk
                if len(c) > 20:
                    print('c long', a, '//', b, '//', c)
                    continue
                main = c_instr_str.replace(c, 'C')
                # print(main, a, b, c, prnt, sep='\n\t')
                prnt += 1

                if len(main) <= 20 and set(main) == {'A', 'B', 'C', ','}:  # main can only contain A, B, C
                    return main + '\n', a + '\n', b + '\n', c + '\n'  # add line breaks for input


MAIN, A, B, C = find_segments()
FEED = 'n\n'

code.send([ord(c) for c in MAIN + A + B + C + FEED])
out = code.evaluate(init={0: 2})
print(out[-1])
