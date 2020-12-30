import networkx as nx

from common.session import AdventSession

session = AdventSession(day=12, year=2017)
data = session.data.strip()
data = data.split('\n')

d = {}
for i, line in enumerate(data):
    fr, to = line.split(' <-> ')
    fr = int(fr)
    to = [*map(int, to.split(', '))]
    d[fr] = to

G = nx.from_dict_of_lists(d)

p1 = len(nx.algorithms.components.node_connected_component(G, 0))
p2 = nx.number_connected_components(G)

session.submit(p1, part=1)
session.submit(p2, part=2)
