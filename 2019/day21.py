from IntCode import IntCode

with open("day21.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)
it = code.evaluate_step()


def send_ascii(text):
    if text[-1] != '\n':
        text += '\n'
    code.send([ord(c) for c in text])


prog1 = """
NOT A J
AND D J
NOT C T
AND D T
OR T J
WALK
"""

prog2 = """
OR H J
OR E J
NOT C T
AND D T
AND T J
NOT A T
AND D T
OR T J
OR B T
OR E T
NOT T T
AND D T
OR T J
RUN
"""

send_ascii(prog1.strip())
out = code.evaluate()

# print(''.join((chr(c) if c < 255 else str(c)) + ' ' for c in out))
print(out[-1])

send_ascii(prog2.strip())
out = code.evaluate()

# print(''.join((chr(c) if c < 255 else str(c)) + ' ' for c in out))
print(out[-1])
