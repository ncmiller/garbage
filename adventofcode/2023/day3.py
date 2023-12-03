import fileinput
from collections import defaultdict
import math

def in_range(grid, i, j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

def has_adjacent_symbol(grid, i, j):
    deltas = [
        (-1,-1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)]
    for d in deltas:
        x = i+d[0]
        y = j+d[1]
        if not in_range(grid, x, y):
            continue
        c = grid[x][y]
        if c != '.' and not c.isnumeric():
            return True, c, (x,y)
    return False, '', (-1,-1)

def part1(grid):
    num_sum = 0
    num = []
    symbol_adjacent = False

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c.isnumeric():
                if not symbol_adjacent:
                    symbol_adjacent, _, _ = has_adjacent_symbol(grid, i, j)
                num.append(c)
            else:
                if num != []:
                    if symbol_adjacent:
                        num_sum += int(''.join(num))
                        symbol_adjacent = False
                    num = []

    return num_sum

def part2(grid):
    num = []
    adjacent_gears = []
    gears = defaultdict(set) # gear_pos: {nums}

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c.isnumeric():
                _, symbol, pos = has_adjacent_symbol(grid, i, j)
                if symbol == '*':
                    adjacent_gears.append(pos)
                num.append(c)
            else:
                if num != []:
                    num_value = int(''.join(num))
                    for ag in adjacent_gears:
                        gears[ag].add(num_value)
                    adjacent_gears = []
                    num = []
    # print(gears.items())

    gear_ratio_sum = 0
    for gear_pos, nums in gears.items():
        l = list(nums)
        if len(l) == 2:
            gear_ratio_sum += (l[0] * l[1])

    return gear_ratio_sum


grid = [line[:-1] for line in fileinput.input()]
print(part1(grid))
print(part2(grid))
