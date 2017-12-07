"""read lines from stdin, split lines on whitespace"""
import fileinput
import re
lines = []
is_stower = {}
names = []
towers = {}
for line in fileinput.input():
    fields = [x for x in line.split() if x != '->']
    name = fields[0]
    weight = int(fields[1].replace('(','').replace(')',''))
    stowers = [x.split(',')[0] for x in fields[2:]]
    towers[name] = (weight, stowers)
    for st in stowers:
        is_stower[st] = 1
    names.append(name)

for n in names:
    if n not in is_stower:
        print n

print '\n---\n'

tower_weights = {}
def tower_weight(name):
    weight, stowers = towers[name]
    if name in tower_weights:
        return tower_weights[name]
    if not stowers:
        tower_weights[name] = weight
        return weight
    w = weight
    for st in stowers:
        w += tower_weight(st)
    tower_weights[name] = w
    return w

for t in towers.items():
    name, (weight, stowers) = t
    weights = []
    for st in stowers:
        weights.append(tower_weight(st))

    if weights and len(set(weights)) != 1:
        print name, weights, stowers
        for st in stowers:
            print "   ", st, towers[st][0]
    # From here, can eyeball the answer
