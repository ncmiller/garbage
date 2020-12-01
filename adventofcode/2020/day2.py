import fileinput

def parse():
    vals = []
    for line in fileinput.input():
        vals.append(int(line))
    return vals

def part1():
    return 0

def part2():
    return 0

vals = parse()
print(vals)
print(part1())
print(part2())
