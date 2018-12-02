import fileinput
from collections import Counter
#----------------------
# File IO
#----------------------
# for line in fileinput.input():

# with open("day9_input.txt") as f:
#     chars = f.read()

# vals = map(int, fileinput.input())

# weight = int(fields[1].replace('(','').replace(')',''))
# stowers = [x.split(',')[0] for x in fields[2:]]
#----------------------

lines = [l.rstrip() for l in fileinput.input()]

def part1():
    twos = set()
    threes = set()
    for l in lines:
        counts = Counter(l)
        for k,v in counts.most_common():
            if v == 2:
                twos.add(l)
            if v == 3:
                threes.add(l)
    print len(twos) * len(threes)

def part2():
    slines = sorted(lines)
    for i in range(0,len(slines)-1):
        a = slines[i]
        b = slines[i+1]
        matching = []
        for j in range(len(a)): # assume same len for both
            if a[j] == b[j]:
                matching.append(a[j])
        if len(matching) == len(a) - 1:
            print ''.join(matching)
            return

part1()
part2()
