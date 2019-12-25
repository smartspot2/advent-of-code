from collections import Counter
with open("day4.in", "r") as f:
    a, b = map(int, f.readline().strip().split('-'))

cnt1 = cnt2 = 0
for k in range(a, b+1):
    s = str(k)
    if ''.join(sorted(list(s))) == s:
        if max(Counter(s).values()) != 1:
            cnt1 += 1
        if 2 in Counter(s).values():
            cnt2 += 1

print(cnt1)
print(cnt2)
