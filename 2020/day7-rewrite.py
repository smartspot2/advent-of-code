import numpy as np
# import networkx as nx
from collections import *
from itertools import *
import re

from common.session import AdventSession

session = AdventSession(day=7, year=2020)
data = session.data.strip()
data = data.split('\n')

rules = dict()

for line in data:
    adj, col, bags, contain, *rest = line.strip('.').split()
    inner = [(int((s := w.split())[0]), ' '.join(s[1:3]))
             for w in ' '.join(rest).split(', ')] if rest[0] != 'no' else []
    rules[adj + ' ' + col] = inner


def recur(b):
    return b == 'shiny gold' or any(recur(o[1]) for o in rules[b])


def recur2(b):
    return sum(c + c * recur2(o) for c, o in rules[b]) if rules[b] else 0


p1 = sum(recur(bag) for bag in rules if bag != 'shiny gold')
p2 = recur2('shiny gold')

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

(lambda p, q, r: print(sum(p(p, r, b) for b in r)-1, q(q, r, 'shinygold')))(lambda p, r, b: b == 'shinygold' or any(p(p, r, o) for c, o in r[b]), lambda q, r, b: sum(c + c * q(q, r, o) for c, o in r[b]) if r[b] else 0, {a+c: [(int((s := w.split())[0]), ''.join(s[1:3])) for w in r.split(', ')] if r[0] != 'n' else [] for a, c, _, _, r in [l.strip('.').split(' ', 4) for l in open('day7.in')]})
# (lambda p,q,r:print(sum(p(p,r,b)for b in r)-1,q(q,r,'shinygold')))(lambda p,r,b:b=='shinygold'or any(p(p,r,o)for c,o in r[b]),lambda q,r,b:sum(c+c*q(q,r,o)for c,o in r[b])if r[b]else 0,{a+c:[(int((s:=w.split())[0]),''.join(s[1:3]))for w in r.split(', ')]if r[0]!='n'else[]for a,c,_,_,r in[l.strip('.').split(' ',4)for l in open('day7.in')]})
