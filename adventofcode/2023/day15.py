import fileinput
import re

def hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value &= 0xFF
    return value

def part1(lines):
    steps = lines[0].split(',')
    total = sum([hash(s) for s in steps])
    return total

def part2(lines):
    boxes = []
    for i in range(256):
        boxes.append([])

    for num, step in enumerate(lines[0].split(',')):
        result = re.search(r"([a-z]+)([-=])(\d+)?$", step)
        label, op, lens = result.groups()
        h = hash(label)
        if op == '=':
            found = False
            for item in boxes[h]:
                if item[0] == label:
                    item[1] = lens
                    found = True
                    break
            if not found:
                boxes[h].append([label, lens])
        else:
            for item in boxes[h]:
                if item[0] == label:
                    boxes[h].remove(item)
                    found = True
                    break

    focusing_power = 0
    for i in range(256):
        for j, item in enumerate(boxes[i]):
            focusing_power += ((i+1) * (j+1) * int(item[1]))
    return focusing_power



lines = [l[:-1] for l in fileinput.input()]
print(part1(lines))
print(part2(lines))
