"""read lines from stdin, split lines on whitespace"""
import fileinput
lines = []
for line in fileinput.input():
    lines.append(int(line))


"""read single number from stdin"""
# num = map(int, raw_input())

"""read one char at a time from named file"""
# with open("dayX_input.txt") as f:
#     for line in f:
#         for ch in line:
#             if ch != '\n':
#                 print ch

""" part1 """
# moves=[0, 3, 0, 1, -3]
moves = lines[:]
i = 0
steps = 0
while i >= 0 and i < len(moves):
    next = moves[i]
    moves[i] += 1
    i += next
    steps += 1
print steps


""" part2 """
moves = lines[:]
i = 0
steps = 0
while i >= 0 and i < len(moves):
    next = moves[i]
    if next >= 3:
        moves[i] -= 1
    else:
        moves[i] += 1
    i += next
    steps += 1
print steps
