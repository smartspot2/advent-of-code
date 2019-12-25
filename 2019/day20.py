from collections import defaultdict
from string import ascii_uppercase

import networkx as nx
import numpy as np

AROUND = [(-1, 0), (1, 0), (0, -1), (0, 1)]

with open("day20.in", "r") as f:
    data = np.array([list(line.strip('\n').ljust(119)) for line in f])

adj = dict()
portals = []
# Maze adj
for r, c in np.ndindex(*data.shape):
    if data[r, c] == '.':
        cur_adj = []
        for dr, dc in AROUND:
            if data[r + dr, c + dc] == '.':
                cur_adj.append((r + dr, c + dc))
        if any(data[r + dr, c + dc] in ascii_uppercase for dr, dc in AROUND):
            portals.append((r, c))
        adj[(r, c)] = cur_adj

G = nx.Graph(adj)

portal_labels = defaultdict(list)
outside_portals = []
inside_portals = []
for r, c in portals:
    # check around to see what label is
    for dr, dc in AROUND:
        if data[r + dr, c + dc] in ascii_uppercase:
            label = (data[r + dr, c + dc] + data[r + 2 * dr, c + 2 * dc])
            if dr < 0 or dc < 0:
                label = label[::-1]
            portal_labels[label].append((r, c))
            if (r < 5 or r > data.shape[0] - 5) or (c < 5 or c > data.shape[1] - 5):
                outside_portals.append((r, c))
            else:
                inside_portals.append((r, c))

start = end = (0, 0)
for value, pair in portal_labels.items():
    if len(pair) == 2:
        G.add_edge(pair[0], pair[1])
    else:
        if value == 'AA':
            start = pair[0]
        elif value == 'ZZ':
            end = pair[0]


def dijkstra(source):
    from heapq import heappush, heappop
    inf = float("inf")
    pq = []
    cur_costs = defaultdict(lambda: inf)
    cur_costs[source, 0] = 0
    heappush(pq, (0, 0, tuple(source)))

    while pq:
        _, cur_level, u = heappop(pq)
        for v in G.adj[u].keys():
            new_level = cur_level
            if (u in outside_portals and v in inside_portals) or (v in outside_portals and u in inside_portals):
                new_level = cur_level - 2 * int(u in outside_portals) + 1
                if new_level < 0:
                    continue
            new_cost = cur_costs[u, cur_level] + 1
            if new_cost < cur_costs[v, new_level]:
                cur_costs[v, new_level] = new_cost
                if not (new_level == 0 and v == end):
                    heappush(pq, (new_cost, new_level, v))
                else:
                    return new_cost

    return None


# Part 1
print(nx.shortest_path_length(G, start, end))
# Part 2
print(dijkstra(start))
