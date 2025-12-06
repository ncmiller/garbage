import fileinput
import re
import math

def part1(lines):
    nums, ops = lines[:-1], re.sub('\s+', '', lines[-1])
    nums = [re.findall(r'\d+', n) for n in nums]
    nums = [list(map(int, n)) for n in nums]

    total = 0
    for i in range(len(ops)):
        values = [n[i] for n in nums]
        op = ops[i]
        if op == '+':
            total += sum(values)
        else:
            total += math.prod(values)

    return total

def part2(lines):
    max_length = 0
    for l in lines:
        max_length = max(max_length, len(l))
    padded_lines = []
    for l in lines:
        padded_lines.append(l + ' ' * (max_length - len(l)))
    # print(padded_lines)

    height = len(padded_lines)
    width = len(padded_lines[0])
    # print(height, width)
    new_lines = []
    for col in reversed(range(width)):
        new_line = ''
        for row in range(height):
            new_line += padded_lines[row][col]
        new_lines.append(new_line.strip())
    # print(new_lines)

    values = []
    total = 0
    for l in new_lines:
        if l == '':
            continue
        elif l[-1] == '+':
            values.append(int(l[:-1]))
            total += sum(values)
            values = []
        elif l[-1] == '*':
            values.append(int(l[:-1]))
            total += math.prod(values)
            values = []
        else:
            values.append(int(l))
    return total

lines = [l[:-1] for l in fileinput.input()]
print(part1(lines))
print(part2(lines))
