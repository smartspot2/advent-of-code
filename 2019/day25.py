from IntCode import IntCode, evaluate_until_input

with open("day25.in", 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

code = IntCode(data)
it = code.evaluate_step()


def send_ascii(text):
    if text[-1] != '\n':
        text += '\n'
    code.send([ord(c) for c in text])


while True:
    out = evaluate_until_input(it)
    print(''.join(chr(c) for c in out))
    send_instr = input()
    send_ascii(send_instr.strip())
