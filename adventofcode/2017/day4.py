"""read lines from stdin, split lines on whitespace"""
import fileinput
lines = []
for line in fileinput.input():
    lines.append([x for x in line.split()])

""" part1 """
valid = 0
for line in lines:
    d = {}
    is_valid = True
    for word in line:
        if word in d:
            is_valid = False
            break
        d[word] = 1
    if is_valid:
        valid += 1
print valid

""" part2 """
valid = 0
for line in lines:
    d = {}
    is_valid = True
    for word in line:
        w = ''.join(sorted(word))
        if w in d:
            is_valid = False
            break
        d[w] = 1
    if is_valid:
        valid += 1
print valid
