import fileinput
from collections import Counter

def parse():
    groups = []
    group = []
    for line in fileinput.input():
        l = line.rstrip()
        if l != '':
            group.append(l)
        else:
            groups.append(group)
            group = []
    groups.append(group)
    return groups

def part1(vals):
    count = 0
    for group in vals:
        all_answers = ''.join(group)
        c = len(set(all_answers))
        count += c
    return count

def part1_oneliner(vals):
    return sum([len(set(''.join(group))) for group in vals])

def part2(vals):
    count = 0
    for group in vals:
        all_answers = ''.join(group)
        s = set(all_answers)
        for answers in group:
            s = s.intersection(answers)
        count += len(s)
    return count

vals = parse()
# print(vals)
# print(len(vals))
print(part1(vals))
print(part2(vals))
