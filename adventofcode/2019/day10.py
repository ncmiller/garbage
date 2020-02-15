import fileinput

# Returns list of (x,y), where 0,0 is top left, and x moves right
def find_asteroids(grid):
    asteroids = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                asteroids.append((col, row))
    return asteroids

def gcd(x, y):
    x = abs(x)
    y = abs(y)
    if x == 0:
        return y
    if y == 0:
        return x

    d = 0
    while x % 2 == 0 and y % 2 == 0:
        x /= 2
        y /= 2
        d += 1
    while x != y:
        if x % 2 == 0:
            x /= 2
        elif y % 2 == 0:
            y /= 2
        elif x > y:
            x = (x - y) / 2
        else:
            y = (y - x) / 2
    g = x
    return g * 2**d

# slope = (run, rise)
# find greatest common divisor of each
def get_lcslope(slope):
    divisor = gcd(slope[0], slope[1])
    return (slope[0] / divisor, slope[1] / divisor)

def add_coords(x, y):
    return (x[0] + y[0], x[1] + y[1])

def sub_coords(x, y):
    return (x[0] - y[0], x[1] - y[1])

def in_bounds(grid, x):
    row = x[1]
    col = x[0]
    return (
        row >= 0 and
        col >= 0 and
        row < len(grid) and
        col < len(grid[0])
    )

def part1(grid):
    # capture asteroid locations
    # for each asteroid x
    #   asteroids_visible = 0
    #   for each other asteroid target
    #     compute slope from x to target
    #     find least common slope
    #       e.g. 2,4 --> 1,2
    #     for each multiple of least common slope:
    #       if asteroid == target:
    #         asteroids_visible += 1
    #       else:
    #         break # ran into asteroid before reaching target

    max_visible = 0
    max_asteroid = (0,0)

    asteroids = find_asteroids(grid)
    for x in asteroids:
        visible_asteroids = 0
        targets = list(set(asteroids) - set([x]))
        # print(x, targets)
        for target in targets:
            # print(x, target)
            slope = sub_coords(target, x)
            lc_slope = get_lcslope(slope)
            # print(x, target, lc_slope)

            coords_to_check = []
            current_coord = x
            while True:
                current_coord = add_coords(current_coord, lc_slope)
                if in_bounds(grid, current_coord):
                    coords_to_check.append(current_coord)
                    if current_coord == target:
                        break
                else:
                    break

            # print(x,target,coords_to_check)
            for coord in coords_to_check:
                hit_asteroid = (grid[coord[1]][coord[0]] == '#')
                if hit_asteroid:
                    if coord == target:
                        visible_asteroids += 1
                    break
        # print(x, visible_asteroids)
        if visible_asteroids > max_visible:
            max_visible = visible_asteroids
            max_asteroid = x
    print('best =', max_asteroid, max_visible)

def part2(grid):
    # Find visible (iterate over all, filter by visible)
    # Sort visible by angle (tan theta = dx / dy)
    # Destroy visible
    # Repeat
    pass

lines = []
for line in fileinput.input():
    lines.append(line.rstrip())

# part1(lines[:])
part2(lines[:])
