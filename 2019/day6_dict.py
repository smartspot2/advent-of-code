with open("day6.in", "r") as f:
    data = [l.strip().split(")") for l in f.readlines()]

orbits = dict()
for p, c in data:
    orbits[c] = p

# Part 1
cnt = 0
for n in orbits:
    while n in orbits:
        n = orbits[n]
        cnt += 1

print(cnt)

# Part 2
you_node = orbits["YOU"]
san_node = orbits["SAN"]

you_path = [you_node]
while you_node in orbits:
    you_node = orbits[you_node]
    you_path.append(you_node)
san_path = [san_node]
while san_node in orbits:
    san_node = orbits[san_node]
    san_path.append(san_node)

for you_i, n in enumerate(you_path):
    if n in san_path:
        san_i = san_path.index(n)
        print(you_i + san_i)
        break
