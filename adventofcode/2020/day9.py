import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append(int(l))
    return vals

def find_sum(n, vals):
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            if (vals[i]+vals[j]) == n:
                return True
    return False

def part1(vals):
    preamble_len = 25
    for i in range(preamble_len, len(vals)):
        prior = vals[i-preamble_len:i]
        n = vals[i]
        if not find_sum(n, prior):
            return n
    return 0

def part2(vals):
    inval_num = part1(vals)
    for i in range(len(vals)):
        for j in range(i+2, len(vals)):
            r = vals[i:j]
            s = sum(r)
            if s == inval_num:
                return min(r) + max(r)
            elif s > inval_num:
                break
    return 0

vals = parse()
# print(vals)
# print(len(vals))
print(part1(vals))
print(part2(vals))
