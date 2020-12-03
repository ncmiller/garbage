import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        vals.append(line[:-1])
    return vals

def part1(vals):
    pos = [0,0] # x,y
    tree_count = 0
    while pos[1] < len(vals):
        pos_x = pos[0] % len(vals[0])
        if vals[pos[1]][pos_x] == '#':
            tree_count += 1
        pos[0] += 3
        pos[1] += 1
    return tree_count

def part2(vals):
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    prod = 1
    for slope in slopes:
        pos = [0,0] # x,y
        tree_count = 0
        while pos[1] < len(vals):
            pos_x = pos[0] % len(vals[0])
            if vals[pos[1]][pos_x] == '#':
                tree_count += 1
            pos[0] += slope[0]
            pos[1] += slope[1]
        prod *= tree_count
    return prod

vals = parse()
# print(vals)
# print(len(vals))
print(part1(vals))
print(part2(vals))

