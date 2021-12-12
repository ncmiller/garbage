import fileinput
import copy

def part1(crabs):
    mn = min(crabs)
    mx = max(crabs)
    best_i = -1
    min_fuel = 1e10
    for i in range(mn, mx+1):
        align = i
        fuel = sum(map(lambda c: abs(align - c), crabs))
        if fuel < min_fuel:
            best_i = i
            min_fuel = fuel
    # print(best_i, min_fuel)
    return min_fuel


def additive_fuel_cost(align, crab):
    diff = abs(align - crab)
    return int(diff * (diff + 1) / 2)

def part2(crabs):
    mn = min(crabs)
    mx = max(crabs)
    best_i = -1
    min_fuel = 1e10
    for i in range(mn, mx+1):
        align = i
        fuel = sum(map(lambda c: additive_fuel_cost(i, c), crabs))
        if fuel < min_fuel:
            best_i = i
            min_fuel = fuel
    # print(best_i, min_fuel)
    return min_fuel

crabs = list(map(int, list(fileinput.input())[0].split(',')))
print(part1(copy.deepcopy(crabs)))
print(part2(copy.deepcopy(crabs)))
