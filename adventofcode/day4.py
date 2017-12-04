"""read lines from stdin, split lines on whitespace"""
import fileinput
lines = []
for line in fileinput.input():
    lines.append([x for x in line.split()])


"""read single number from stdin"""
# num = map(int, raw_input())

"""read one char at a time from named file"""
# with open("dayX_input.txt") as f:
#     for line in f:
#         for ch in line:
#             if ch != '\n':
#                 print ch

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
