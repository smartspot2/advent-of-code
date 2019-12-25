import numpy as np

from IntCode import IntCode, evaluate_until_input

with open("day17.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)

it = code.evaluate_step(init={0: 2})

out = evaluate_until_input(it)

boardstr = ''.join(chr(c) for c in out)
arr = np.array([list(x) for x in boardstr.split()[:-1]])  # convert board to np array
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

MAXLEN = 10


# This doesn't actually always work
def find_segments():
    for endA in range(MAXLEN):
        a = ','.join(instr[:endA + 1])
        b_instr_str = instr_str.replace(a, 'A')
        b_instr = b_instr_str.split(',')

        start_b = b_instr.index(b_instr_str.lstrip('A,').split(',')[0])  # index of first non-A
        endrange_b = min(start_b + MAXLEN, len(b_instr) - 1)  # 10 long or end of string
        if 'A' in b_instr[start_b:]:  # index of first A after first non-A
            endrange_b = min(endrange_b, b_instr.index('A', start_b))

        for endB in range(start_b, endrange_b):  # loop through all B
            b = ','.join(b_instr[start_b:endB + 1])
            c_instr_str = b_instr_str.replace(b, 'B')
            c_instr = c_instr_str.split(',')

            start_c = c_instr.index(c_instr_str.lstrip('AB,').split(',')[0])  # index of first non-A,B
            end_c = min(start_c + MAXLEN, len(c_instr))  # 10 long or end of string
            if 'A' in c_instr[start_c:]:  # index of first A after first non-A,B
                end_c = min(end_c, c_instr.index('A', start_c))
            if 'B' in c_instr[start_c:]:  # index of first B after first non-A,B
                end_c = min(end_c, c_instr.index('B', start_c))
            c = ','.join(c_instr[start_c:end_c])  # C has to be first non-A,B chunk
            main = c_instr_str.replace(c, 'C')

            if set(main) == {'A', 'B', 'C', ','}:  # main can only contain A, B, C
                return main + '\n', a + '\n', b + '\n', c + '\n'  # add line breaks for IntCode


MAIN, A, B, C = find_segments()
FEED = 'n\n'

inp_list = [ord(c) for c in MAIN + A + B + C + FEED]
code.send(inp_list)

out = code.evaluate(init={0: 2})
# print(''.join([chr(c) if c < 256 else str(c) for c in out]))
print(out[-1])
