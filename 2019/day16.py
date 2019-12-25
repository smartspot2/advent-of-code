import numpy as np

with open("day16.in", "r") as f:
    data = list(map(int, f.readline()))

base = np.array([0, 1, 0, -1])
offset = int(''.join(map(str, data[:7])))


def fft(inp):
    res = []
    for n in range(len(inp)):
        s = 0
        for i, m in enumerate(range(0, len(inp), 2 * (n + 1))):
            s += (sum(inp[n + m:m + 2 * n + 1])) * (-1) ** i
        res.append(abs(s) % 10)
    return res


def bad_fft(inp):
    res = np.cumsum(inp[::-1])[::-1] % 10
    return res


cur = data
for k in range(100):
    cur = fft(cur)

# Part 1
print(''.join(map(str, cur[:8])))

cur = data * 10000
for k in range(100):
    cur = bad_fft(cur)

# Part 2
print(''.join(map(str, cur[offset:offset + 8])))
