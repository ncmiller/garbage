import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append(l)
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

