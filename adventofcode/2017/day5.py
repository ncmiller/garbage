"""read lines from stdin, split lines on whitespace"""
import fileinput
lines = []
for line in fileinput.input():
    lines.append(int(line))


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
