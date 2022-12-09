import fileinput

def sign(num):
    return 1 if num >= 0 else -1

def move_tail(h, t):
    same_x = h[0] == t[0]
    same_y = h[1] == t[1]
    dx = h[0] - t[0]
    dy = h[1] - t[1]
    is_adjacent = abs(dx) <= 1 and abs(dy) <= 1

    if is_adjacent: return t
    elif same_x:    return (t[0], t[1] + sign(dy))
    elif same_y:    return (t[0] + sign(dx), t[1])
    else:           return (t[0] + sign(dx), t[1] + sign(dy))

def part1(moves):
    visited = set()
    h = (0,0)
    t = (0,0)
    visited.add(t)
    for m in moves:
        h_step = int(m[1])
        h_dir = (0,0)
        if   m[0] == 'R': h_dir = ( 1, 0)
        elif m[0] == 'U': h_dir = ( 0,-1)
        elif m[0] == 'D': h_dir = ( 0, 1)
        elif m[0] == 'L': h_dir = (-1, 0)

        # move head one step at a time
        for _ in range(h_step):
            h = (h[0] + h_dir[0], h[1] + h_dir[1])
            t = move_tail(h, t)
            visited.add(t)

    # print(visited)
    return len(visited)

def part2(moves):
    visited = set()
    knots = [(0,0) for _ in range(10)] # index 0 is head
    visited.add(knots[-1])
    for m in moves:
        h_step = int(m[1])
        h_dir = (0,0)
        if   m[0] == 'R': h_dir = ( 1, 0)
        elif m[0] == 'U': h_dir = ( 0,-1)
        elif m[0] == 'D': h_dir = ( 0, 1)
        elif m[0] == 'L': h_dir = (-1, 0)

        # move head one step at a time
        for _ in range(h_step):
            knots[0] = (knots[0][0] + h_dir[0], knots[0][1] + h_dir[1])
            for i in range(1, len(knots)):
                knots[i] = move_tail(knots[i-1], knots[i])
            visited.add(knots[-1])

    # print(visited)
    return len(visited)

moves = [l.rstrip().split(' ') for l in fileinput.input()]
# print(moves)
print(part1(moves))
print(part2(moves))
