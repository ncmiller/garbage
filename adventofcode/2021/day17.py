def is_hit(xvel, yvel, target):
    x = y = 0
    highest_y = -100000000
    while True:
        # print(x, y)
        x += xvel
        y += yvel
        highest_y = max(highest_y, y)
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1

        if x >= target[0][0] and x <= target[0][1] and y >= target[1][0] and y <= target[1][1]:
            return (True, highest_y)
        elif x > target[0][1] or y < target[1][0]:
            return (False, highest_y)
    return (False, highest_y)

def part1(target):
    highest_y = -10000000
    for xvel in range(1,1000):
        for yvel in range(-abs(target[1][0]), abs(target[1][0])):
            hit, hy = is_hit(xvel, yvel, target)
            if hit:
                if hy > highest_y:
                    highest_y = hy
                    # print(hy, xvel, yvel)
    return highest_y

def part2(target):
    hits = []
    for xvel in range(1,1000):
        for yvel in range(-abs(target[1][0]), abs(target[1][0])):
            hit, _ = is_hit(xvel, yvel, target)
            if hit:
                hits.append((xvel, yvel))
    # print(hits)
    return len(hits)

# (small, big)
# target = [(20,30),(-10,-5)] # sample
target = [(211,232),(-124,-69)] # input
# print(is_hit(7, 2, target)[0])
# print(is_hit(6, 3, target)[0])
# print(is_hit(9, 0, target)[0])
# print(is_hit(17, -4, target)[0])
print(part1(target))
print(part2(target))
