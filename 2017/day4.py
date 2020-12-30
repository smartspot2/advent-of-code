from common.session import AdventSession

session = AdventSession(4, 2017)
data = session.data.strip()
data = data.splitlines()

p1, p2 = 0, 0

for i, line in enumerate(data):
    split = line.strip().split()
    anagram_split = [''.join(sorted(word)) for word in split]
    p1 += len(set(split)) == len(split)
    p2 += len(set(anagram_split)) == len(anagram_split)

session.submit(p1, part=1)
session.submit(p2, part=2)
