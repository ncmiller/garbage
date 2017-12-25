def turn(face, d):
    allmoves = "NESW"
    current = allmoves.index(face)
    if d == 'R': return allmoves[(current + 1) % len(allmoves)]
    else: return allmoves[(current - 1) % len(allmoves)]

def move(p, face, steps):
    if face == 'N': return (p[0] - steps, p[1])
    if face == 'E': return (p[0], p[1] + steps)
    if face == 'S': return (p[0] + steps, p[1])
    if face == 'W': return (p[0], p[1] - steps)

def dist(p):
    return sum(map(abs, p))

def part1(chars):
    moves = chars.split(', ')
    p = (0, 0)
    face = 'N'

    for m in moves:
        face = turn(face, m[0])
        p = move(p, face, int(m[1:]))

    return dist(p)


assert(part1('R2, L3') == 5)
assert(part1('R2, R2, R2') == 2)
assert(part1('R5, L5, R5, R3') == 12)

with open("day1_input.txt") as f:
    chars = f.read()

print part1(chars)

#-----------------------------------------------

def part2(chars):
    moves = chars.split(', ')
    p = (0, 0)
    face = 'N'

    visited = set()
    visited.add(p)

    for m in moves:
        face = turn(face, m[0])
        for step in range(int(m[1:])):
            p = move(p, face, 1)
            if p in visited: return dist(p)
            else: visited.add(p)

    assert(False)

assert(part2('R8, R4, R4, R8') == 4)

print part2(chars)
