import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        rule,c,pwd = line.split(' ')
        min_max = rule.split('-')
        vals.append([
            int(min_max[0]),
            int(min_max[1]),
            c[0],
            pwd[:-1]])
    return vals

def part1(vals):
    valid_count = 0
    for mn,mx,c,pwd in vals:
        counts = Counter(pwd)
        if counts[c] >= mn and counts[c] <= mx:
            valid_count += 1
    return valid_count

def part2(vals):
    valid_count = 0
    for p1,p2,c,pwd in vals:
        c1 = pwd[p1-1]
        c2 = pwd[p2-1]
        if (c1 == c) ^ (c2 == c):
            valid_count += 1
    return valid_count

vals = parse()
# print(vals)
# print(len(vals))
print(part1(vals))

# print(part2([[1,3,'a','abcde']]))
# print(part2([[1,3,'b','cdefg']]))
# print(part2([[2,9,'c','ccccccccc']]))
print(part2(vals))
