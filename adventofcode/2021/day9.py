import fileinput
import copy
import itertools

def adjacent(height_map, i, j, nrows, ncols):
    adj = []
    if i != 0:
        adj.append((height_map[i-1][j], i-1, j)) # up
    if i != (nrows-1):
        adj.append((height_map[i+1][j], i+1, j)) # down
    if j != 0:
        adj.append((height_map[i][j-1], i, j-1)) # left
    if j != (ncols-1):
        adj.append((height_map[i][j+1], i, j+1)) # right
    return adj

def low_points(height_map):
    nrows = len(height_map)
    ncols = len(height_map[0])
    low_points = []
    for i in range(nrows):
        for j in range(ncols):
            h = height_map[i][j]
            adj = adjacent(height_map, i, j, nrows, ncols)
            if h < min([a[0] for a in adj]):
                low_points.append((h,i,j))
    return low_points

def part1(height_map):
    return sum([(lp[0]+1) for lp in low_points(height_map)])

def part2(height_map):
    nrows = len(height_map)
    ncols = len(height_map[0])
    basin_sizes = []
    for lp in low_points(height_map):
        basin_size = 1
        queue = [lp] # list of (height, i, j)
        seen = set()
        seen.add(lp)
        while queue:
            p = queue[0]
            queue = queue[1:]
            adj = adjacent(height_map, p[1], p[2], nrows, ncols)
            h = p[0]
            for a in adj:
                if a[0] > h and a[0] != 9:
                    if a not in seen:
                        seen.add(a)
                        queue.append(a)
                        basin_size += 1
        # print(lp, basin_size)
        basin_sizes.append(basin_size)
    top3 = sorted(basin_sizes)[-3:]
    return (top3[0] * top3[1] * top3[2])

lines = list(fileinput.input())
height_map = [list(map(int, line.rstrip())) for line in lines]
# print(height_map)
print(part1(copy.deepcopy(height_map)))
print(part2(copy.deepcopy(height_map)))
