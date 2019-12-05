import fileinput
import string
#----------------------
# File IO
#----------------------
# for line in fileinput.input():

# with open("day9_input.txt") as f:
#     chars = f.read()

# vals = map(int, fileinput.input())

# weight = int(fields[1].replace('(','').replace(')',''))
# stowers = [x.split(',')[0] for x in fields[2:]]
#----------------------

# observation: if touching edge of known grid, then infinite

coords = []
for line in fileinput.input():
    coords.append(map(int, line.split(',')))

def print_grid(g, vals_only=False):
    for row in g:
        if vals_only:
            print ['{}'.format(str(p)) for p in row]
        else:
            print ['({},{})'.format(str(p),p.dist) for p in row]

def set_coord(grid, x, y, val, dist):
    grid[y][x].val = val
    grid[y][x].dist = dist

def grid_label_coord(grid, px, py, val):
    grid[py][px].val = val
    grid[py][px].dist = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            dist = abs(y - py) + abs(x - px)
            p = grid[y][x]
            if dist < p.dist:
                p.val = val
                p.dist = dist
            elif dist == p.dist and dist != 0 and val != p.val:
                p.val = '.'

class Point:
    def __init__(self, val, dist):
        self.val = val
        self.dist = dist
    def __str__(self):
        return str(self.val)

def noninfinite(grid, set_of_vals):
    noninf_set = set_of_vals

    # check borders of grid, remove val from set
    for p in grid[0]:
        if p.val in noninf_set:
            noninf_set.remove(p.val)
    for p in [row[0] for row in grid]:
        if p.val in noninf_set:
            noninf_set.remove(p.val)
    for p in grid[-1]:
        if p.val in noninf_set:
            noninf_set.remove(p.val)
    for p in [row[-1] for row in grid]:
        if p.val in noninf_set:
            noninf_set.remove(p.val)

    return noninf_set

def largest_area(grid, set_of_vals):
    vals = noninfinite(grid, set_of_vals)
    counts = {}
    for c in vals:
        counts[c] = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c = grid[y][x].val
            if c in counts:
                counts[c] += 1
    return max(counts.values())

def part1():
    max_x = max(c[0] for c in coords) + 1
    max_y = max(c[1] for c in coords) + 1
    grid = []
    for y in range(max_y):
        grid_x = []
        for x in range(max_x):
            grid_x.append(Point('-', 10000))
        grid.append(grid_x)

    next_val = 0
    all_vals = set()
    for c in coords:
        all_vals.add(next_val)
        set_coord(grid, c[0], c[1], next_val, 0)
        next_val += 1

    next_val = 0
    for c in coords:
        grid_label_coord(grid, c[0], c[1], next_val)
        next_val += 1

    print largest_area(grid, all_vals)

def total_distance(x, y, coords):
    tdist = 0
    for c in coords:
        tdist += abs(x - c[0]) + abs(y - c[1])
    return tdist


def part2():
    max_x = max(c[0] for c in coords) + 1
    max_y = max(c[1] for c in coords) + 1

    in_region = 0
    for y in range(max_y):
        for x in range(max_x):
            tdist = total_distance(x, y, coords)
            if tdist < 10000:
                in_region += 1
    print in_region

part1()
part2()
