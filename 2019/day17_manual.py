import numpy as np
from scipy.signal import convolve2d

from IntCode import IntCode
from Screen import Screen

with open("day17.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)
board = Screen()

out = code.evaluate()
boardstr = ''.join(chr(c) for c in out)
arr = np.array([list(x) for x in boardstr.split()])
conv = convolve2d(np.isin(arr, list('#<>^v')), [[0, 1, 0], [1, 0, 1], [0, 1, 0]], mode='same')
alignsum = sum(a * b for a, b in np.argwhere(conv == 4))

arr[np.nonzero(conv == 4)] = 'O'
print('\n'.join(''.join(row) for row in arr))

# Part 1
print(alignsum)

MAIN = 'A,B,A,C,A,A,C,B,C,B\n'
A = 'L,12,L,8,R,12\n'
B = 'L,10,L,8,L,12,R,12\n'
C = 'R,12,L,8,L,10\n'
FEED = 'n\n'

code.send([ord(c) for c in MAIN + A + B + C + FEED])

out = code.evaluate(init={0: 2})
# Part 2
# print(''.join([chr(c) if c < 256 else str(c) for c in out]))
print(out[-1])
