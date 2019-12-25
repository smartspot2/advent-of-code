import networkx as nx

with open("day6.in", "r") as f:
    graph = nx.Graph([l.strip().split(")")[::-1] for l in f.readlines()])

# Part 1
print(sum(p[1] for p in nx.single_target_shortest_path_length(graph, "COM")))
# Part 2
print(nx.shortest_path_length(graph, "YOU", "SAN") - 2)
