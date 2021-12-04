import fileinput

def part1(vals):
    prev = -1
    increased = 0
    for i in range(1, len(vals)):
        if (i > 0) and (vals[i] > prev):
            increased += 1
        prev = vals[i]
    return increased

def part2(vals):
    prev = -1
    increased = 0
    for i in range(2, len(vals)):
        window = sum(vals[i-2:i+1])
        # print(i, window)
        if (i > 2) and (window > prev):
            increased += 1
        prev = window
    return increased

vals = list(map(int, fileinput.input()))
print(part1(vals))
print(part2(vals))

