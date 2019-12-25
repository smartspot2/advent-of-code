from sympy import symbols

with open("day22.in", "r") as f:
    instructions = f.read().splitlines()

LEN = 10007
pos = 2019
# shuffle
for instr in instructions:
    if 'deal with increment' in instr:
        inc = int(instr.split()[-1])
        pos = inc * pos
    elif 'cut' in instr:
        amt = int(instr.split()[-1])
        pos = pos - amt
    elif instr == 'deal into new stack':
        pos = LEN - pos - 1

# Part 1
print(pos % LEN)

LEN = 119315717514047
REPT = 101741582076661

x = symbols('x')
pos = x
# reverse shuffle
for instr in instructions[::-1]:
    if 'deal with increment' in instr:
        inc = int(instr.split()[-1])
        pos = pow(inc, -1, LEN) * pos
    elif 'cut' in instr:
        amt = int(instr.split()[-1])
        pos = pos + amt
    elif instr == 'deal into new stack':
        pos = LEN - pos - 1

a, b = pos.coeff(x, 1) % LEN, pos.coeff(x, 0) % LEN
# Part 2
print((pow(a, REPT, LEN) * 2020 + b * (1 - pow(a, REPT, LEN)) * pow(1 - a, -1, LEN)) % LEN)
