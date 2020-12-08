import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        op,num = l.split(' ')
        num = int(num)
        vals.append((op,num))
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
