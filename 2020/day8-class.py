from common.session import AdventSession
from GameConsole import GameConsole

session = AdventSession(day=8, year=2020)
data = session.data.strip()
game = GameConsole(data)

game.evaluate(detect_infinite_loops=True)
p1 = game.acc

p2 = 0
for i in range(len(game.data)):
    game.reset()
    game.swap_instr_at(i, {'jmp': 'nop', 'nop': 'jmp'})
    normal_exit = game.evaluate(detect_infinite_loops=True)
    if normal_exit:
        p2 = game.acc
        break

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

# session.submit(p1, part=1)
# session.submit(p2, part=2)

# session.submit(p1, part=2)
