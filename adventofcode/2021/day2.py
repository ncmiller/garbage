import fileinput

def part1(vals):
    depth = 0
    pos = 0
    for val in vals:
        d,v = val.split(' ')
        v = int(v)
        if d == 'forward':
            pos += v
        elif d == 'down':
            depth += v
        elif d == 'up':
            depth -= v
    return depth * pos

def part2(vals):
    depth = 0
    pos = 0
    aim = 0
    for val in vals:
        d,v = val.split(' ')
        v = int(v)
        if d == 'forward':
            pos += v
            depth += (v * aim)
        elif d == 'down':
            aim += v
        elif d == 'up':
            aim -= v
    return depth * pos

vals = list(fileinput.input())
print(part1(vals))
print(part2(vals))
