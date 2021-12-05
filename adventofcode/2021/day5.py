import fileinput
import copy

def is_horiz(a, b):
    return (a[1] == b[1])

def is_vert(a, b):
    return (a[0] == b[0])

def part1(lines):
    max_x = -1
    max_y = -1
    for line in lines:
        a,b = line
        max_x = max(max_x, a[0], b[0])
        max_y = max(max_y, a[1], b[1])

    counts = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

    for line in lines:
        a,b = line
        if is_horiz(a, b):
            if a[0] > b[0]: # normalize
                a,b = b,a
            y = a[1]
            for x in range(a[0],b[0]+1):
                counts[y][x] += 1
        elif is_vert(a, b):
            if a[1] > b[1]: # normalize
                a,b = b,a
            x = a[0]
            for y in range(a[1],b[1]+1):
                counts[y][x] += 1
    # print(counts)

    twos = 0
    for c in counts:
        twos += len([val for val in c if val >= 2])

    # WA: 6247 (too low, was missing "at least 2" from problem statement)
    return twos

def part2(lines):
    max_x = -1
    max_y = -1
    for line in lines:
        a,b = line
        max_x = max(max_x, a[0], b[0])
        max_y = max(max_y, a[1], b[1])
    counts = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

    for line in lines:
        a,b = line
        if is_horiz(a, b):
            if a[0] > b[0]: # normalize
                a,b = b,a
            y = a[1]
            for x in range(a[0],b[0]+1):
                counts[y][x] += 1
        elif is_vert(a, b):
            if a[1] > b[1]: # normalize
                a,b = b,a
            x = a[0]
            for y in range(a[1],b[1]+1):
                counts[y][x] += 1
        else: # diagonal
            if a[0] > b[0]: # normalize
                a,b = b,a

            if a[1] > b[1]:
                nsteps = a[1] - b[1] + 1
                # print(a,b,nsteps)
                for step in range(nsteps):
                    x = a[0] + step
                    y = a[1] - step
                    counts[y][x] += 1
            else:
                nsteps = b[1] - a[1] + 1
                for step in range(nsteps):
                    x = a[0] + step
                    y = a[1] + step
                    counts[y][x] += 1

    # print(counts)

    twos = 0
    for c in counts:
        twos += len([val for val in c if val >= 2])

    return twos

textlines = list(fileinput.input())
lines = []
for tl in textlines:
    a,_,b = tl.split()
    a = [int(x) for x in a.split(',')]
    b = [int(x) for x in b.split(',')]
    lines.append([a,b])

print(part1(copy.deepcopy(lines)))
print(part2(copy.deepcopy(lines)))

