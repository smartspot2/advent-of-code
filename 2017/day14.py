import networkx as nx

from common.session import AdventSession
from knot_hash import *

session = AdventSession(day=14, year=2017)
data = session.data.strip()

G = nx.Graph()

p1 = 0
prev = ''
for i in range(128):
    h = knot_hash(f'{data}-{i}')
    b = bin(int(h, 16))[2:].zfill(128)
    p1 += b.count('1')
    for j in range(128):
        if b[j] == '1':
            G.add_node(f'({i},{j})')
        if j > 0 and b[j] == '1' and b[j - 1] == '1':
            G.add_edge(f'({i},{j - 1})', f'({i},{j})')
        if prev and b[j] == '1' and prev[j] == '1':
            G.add_edge(f'({i - 1},{j})', f'({i},{j})')
    prev = b

p2 = len([*nx.connected_components(G)])

session.submit(p1, part=1)
session.submit(p2, part=2)
