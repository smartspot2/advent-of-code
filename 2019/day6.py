import anytree

with open("day6.in", "r") as f:
    data = [l.strip().split(")") for l in f.readlines()]

node_dict = dict()
for p, c in data:
    if c not in node_dict:
        node_dict[c] = anytree.Node(c)
    if p not in node_dict:
        node_dict[p] = anytree.Node(p)

    node_dict[c].parent = node_dict[p]

orbits = dict()
for p, c in data:
    orbits[c] = p

# Part 1
cnt = 0
for node_name in node_dict.keys():
    node = node_dict[node_name]
    if node_name == "COM":
        continue
    cnt += len(node.path)
print(cnt)

# Part 2
up, comm, down = anytree.Walker().walk(node_dict["YOU"].parent, node_dict["SAN"].parent)
print(len(up) + len(down))
