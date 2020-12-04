import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        vals.append(line[:-1])
    return vals

def part1(vals):
    return 0

def part2(vals):
    return 0

vals = parse()
# print(vals)
# print(len(vals))
print(part1(vals))
print(part2(vals))


