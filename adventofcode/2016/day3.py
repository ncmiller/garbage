def isvalid(t):
    return (t[0]+t[1] > t[2]) and (t[0]+t[2] > t[1]) and (t[1]+t[2] > t[0])

def part1(lines):
    triangles = [map(int, l.split()) for l in lines]
    return sum(map(isvalid, triangles))

with open("day3_input.txt") as f:
    lines = f.readlines()

assert(part1(['5 10 25']) == 0)

print part1(lines)

#-----------------------------------

def part2(lines):
    triangles = [map(int, l.split()) for l in lines]
    s = 0
    for col in range(3):
        for row in range(0, len(triangles), 3):
            t = [triangles[row+i][col] for i in range(3)]
            if isvalid(t): s += 1
    return s

print part2(lines)

