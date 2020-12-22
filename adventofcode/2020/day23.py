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
print(part1(list(vals)))
print(part2(list(vals)))
