from itertools import permutations

from Chain import Chain

with open("day7.in", "r") as f:
    data = list(map(int, f.read().strip().split(',')))

# Part 1
outlist = [Chain(5, data, perm).evaluate(init=0) for perm in permutations([0, 1, 2, 3, 4])]
print(max(outlist))

# Part 2
outlist = [Chain(5, data, perm).evaluate_continuous(init=0) for perm in permutations([5, 6, 7, 8, 9])]
print(max(outlist))
