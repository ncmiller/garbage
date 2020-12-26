import fileinput
import math

# Returns list of (x,y), where 0,0 is top left, and x moves right
def find_asteroids(grid):
    asteroids = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                asteroids.append((x, y))
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

def find_visible_asteroids(grid, location):
    asteroids = find_asteroids(grid)
    visible_asteroids = []
    targets = list(set(asteroids) - set([location]))
    for target in targets:
        slope = sub_coords(target, location)
        lc_slope = get_lcslope(slope)

        coords_to_check = []
        current_coord = location
        while True:
            current_coord = add_coords(current_coord, lc_slope)
            if in_bounds(grid, current_coord):
                coords_to_check.append(current_coord)
                if current_coord == target:
                    break
            else:
                break

        for coord in coords_to_check:
            coord = (int(coord[0]), int(coord[1]))
            hit_asteroid = (grid[coord[1]][coord[0]] == '#')
            if hit_asteroid:
                if coord == target:
                    visible_asteroids.append(coord)
                break
    return visible_asteroids

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
    max_visible_asteroids = []
    max_asteroid = (0,0)

    asteroids = find_asteroids(grid)
    for x in asteroids:
        visible_asteroids = []
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
                coord = (int(coord[0]), int(coord[1]))
                hit_asteroid = (grid[coord[1]][coord[0]] == '#')
                if hit_asteroid:
                    if coord == target:
                        visible_asteroids.append(coord)
                    break
        # print(x, visible_asteroids)
        if len(visible_asteroids) > max_visible:
            max_visible = len(visible_asteroids)
            max_visible_asteroids = list(visible_asteroids)
            max_asteroid = x
    print('best =', max_asteroid, max_visible)
    return (max_asteroid, max_visible_asteroids)

def part2(grid):
    # Find visible (iterate over all, filter by visible)
    # Sort visible by angle (tan theta = dx / dy)
    # Destroy visible
    # Repeat

    location, visible_asteroids = part1(list(grid))

    # assert(find_visible_asteroids(list(grid), location) == visible_asteroids)

    destroyed_asteroids = []

    rotation = 0
    while True:
        visible_asteroids = find_visible_asteroids(list(grid), location)
        if not visible_asteroids:
            break
        # print(location, len(visible_asteroids), visible_asteroids)
        asteroid_angles = []
        for a in visible_asteroids:
            dx = a[0] - location[0]
            dy = a[1] - location[1]
            dy = -dy

            if dy == 0:
                if dx > 0:
                    theta = math.pi/4.0
                else:
                    theta = 7*math.pi/4.0
            elif dx == 0:
                if dy > 0:
                    theta = 0.0
                else:
                    theta = math.pi/2.0
            else:
                theta = math.atan(float(dx) / float(dy))

            # (10,18) --> (1, -5)
            # (12,8) --> (-1, 5), this should come first

            if dy < 0:
                theta += (math.pi/2.0)

            if theta < 0:
                theta += (2 * math.pi)

            # print(a, dx, dy, theta)
            asteroid_angles.append((a,theta,dx,dy))
        sorted_asteroid_angles = sorted(asteroid_angles, key=lambda x: x[1])

        i = 0
        for a in sorted_asteroid_angles:
            # print(rotation, i, a)
            asteroid, angle, dx, dy = a
            destroyed_asteroids.append(asteroid)
            new_row = list(grid[asteroid[1]])
            new_row[asteroid[0]] = '.'
            new_row = ''.join(new_row)
            grid[asteroid[1]] = new_row
            i += 1
        rotation += 1

    # for i in range(len(destroyed_asteroids)):
    #     print(i+1, destroyed_asteroids[i])

    if len(destroyed_asteroids) > 200:
        x,y = destroyed_asteroids[199]
        print(100 * x + y)

    return destroyed_asteroids

lines = []
for line in fileinput.input():
    lines.append(line.rstrip())

part1(lines[:])
part2(lines[:])
