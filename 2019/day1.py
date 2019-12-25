with open('day1.in', 'r') as f:
    data = list(map(int, f.read().splitlines()))

# Part 1
print(sum(n // 3 - 2 for n in data))


def calc_fuel(n):
    fuel = 0
    while n > 0:
        n = max(0, n // 3 - 2)
        fuel += n
    return fuel


def recur_fuel(n):
    return (recur_fuel(fuel) if (fuel := n // 3 - 2) > 0 else 0) + max(0, fuel)


# Part 2
print(sum(calc_fuel(n) for n in data))
# print(sum(recur_fuel(n) for n in data))
