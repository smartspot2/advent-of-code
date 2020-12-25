import numpy as np
# import networkx as nx
from collections import *
from itertools import *
from functools import *
import math
import re

from common.session import AdventSession

session = AdventSession(day=25, year=2020)
door_pub, card_pub = map(int, session.data.strip().split())

door_loop = card_loop = 0
cur = 1
loop_size = 1
while True:
    cur = (cur * 7) % 20201227
    if cur == door_pub:
        door_loop = loop_size
    if cur == card_pub:
        card_loop = loop_size
    if loop := door_loop or card_loop:
        break
    loop_size += 1

key = card_pub if door_loop == loop else door_pub
p1 = pow(key, loop, 20201227)

print(f'Part 1: {p1}')

# session.submit(p1, part=1)
