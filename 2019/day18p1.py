from collections import defaultdict

import networkx as nx
import numpy as np

ALLNODES = 'abcdefghijklmnopqrstuvwxyz'

with open('day18p1.in', 'r') as f:
    data = np.array([list(row) for row in f.read().splitlines()])

adj_mat = defaultdict(list)

for r in range(data.shape[0]):
    for c in range(data.shape[1]):
        if data[r, c] == '#':
            continue
        cur = (r, c) if data[r, c] == '.' else data[r, c]
        if data[r + 1, c] != '#':
            if data[r + 1, c] != '.':
                adj_mat[cur].append(data[r + 1, c])
            else:
                adj_mat[cur].append((r + 1, c))
        if data[r - 1, c] != '#':
            if data[r - 1, c] != '.':
                adj_mat[cur].append(data[r - 1, c])
            else:
                adj_mat[cur].append((r - 1, c))
        if data[r, c + 1] != '#':
            if data[r, c + 1] != '.':
                adj_mat[cur].append(data[r, c + 1])
            else:
                adj_mat[cur].append((r, c + 1))
        if data[r, c - 1] != '#':
            if data[r, c - 1] != '.':
                adj_mat[cur].append(data[r, c - 1])
            else:
                adj_mat[cur].append((r, c - 1))

G = nx.Graph(adj_mat)
for e in G.edges:
    G.edges[e]['weight'] = 1

# Prune graph
while any(len(G.adj[n]) == 2 and not isinstance(n, str) for n in G.nodes):
    for n in list(G.nodes.keys()):
        if isinstance(n, str) or n not in G.adj:
            continue
        adj = G.adj[n]
        if len(adj) <= 1:
            G.remove_node(n)
        elif len(adj) == 2:
            n1, n2 = tuple(adj.keys())
            w = adj[n1]['weight'] + adj[n2]['weight']
            G.remove_node(n)
            G.add_edge(n1, n2, weight=w)


def dijkstra(source):
    from heapq import heappush, heappop
    inf = float("inf")
    pq = []
    cur_costs = defaultdict(lambda: inf)
    cur_costs[source, frozenset()] = 0
    heappush(pq, (0, frozenset(), tuple(source)))
    finished_costs = []

    while pq:
        collected, u = heappop(pq)[1:]
        if len(u) == 1:
            u = u[0]
        else:
            u = int(u[0]), int(u[1])
        for v in G.adj[u].keys():
            if isinstance(v, str) and v.isupper() and v.lower() not in collected:
                continue  # can't go if haven't gotten key yet
            # print(f"{u} -- {v}, weight {G.edges[(u, v)]['weight']}")
            new_cost = cur_costs[u, collected] + G.edges[(u, v)]['weight']
            new_collected = collected.union(frozenset(v)) if isinstance(v, str) and v.islower() else collected
            if new_cost < cur_costs[v, new_collected]:
                cur_costs[v, new_collected] = new_cost
                if new_collected != frozenset(ALLNODES):
                    if isinstance(v, str):  # convert to tuple for comparisons
                        v = tuple(v)
                    else:
                        v = tuple(map(str, v))
                    # print(f"pushed {v} with cost {new_cost}, with {new_collected}")
                    heappush(pq, (new_cost, new_collected, v))
                else:
                    # print(new_cost)
                    finished_costs.append(new_cost)
            # else:
            #     print(f"\tcost too much ({new_cost}); already had {cur_costs[v, new_collected]}")

    return finished_costs


costs = dijkstra('@')
print(min(costs))
