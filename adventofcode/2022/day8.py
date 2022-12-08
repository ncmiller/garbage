import fileinput
import math

def part1(grid):
    visible = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        # left to right
        lr = range(len(grid[0])) # left-to-right
        rl = reversed(lr)
        max_height = -1
        for col in range(len(grid[0])):
            if grid[row][col] > max_height:
                visible[row][col] = 1
                max_height = grid[row][col]

        # right to left
        max_height = -1
        for col in reversed(range(len(grid[0]))):
            if grid[row][col] > max_height:
                visible[row][col] = 1
                max_height = grid[row][col]

    for col in range(len(grid[0])):
        # top to bottom
        max_height = -1
        for row in range(len(grid)):
            if grid[row][col] > max_height:
                visible[row][col] = 1
                max_height = grid[row][col]

        # bottom to top
        max_height = -1
        for row in reversed(range(len(grid))):
            if grid[row][col] > max_height:
                visible[row][col] = 1
                max_height = grid[row][col]

    total_visible = 0
    for row in range(len(visible)):
        for col in range(len(visible[0])):
            total_visible += visible[row][col]
    return total_visible

def view_dists(grid, row, col):
    # (dx,dy) [down, left, up, right]
    directions = [(0,1), (-1,0), (0,-1), (1,0)]
    my_height = grid[row][col]
    dists = [] # view distance in each direction
    for dx,dy in directions:
        new_row = row
        new_col = col
        view_dist = 0
        while True:
            new_row += dy
            new_col += dx
            if new_row < 0 or new_row >= len(grid):
                break
            if new_col < 0 or new_col >= len(grid[0]):
                break
            view_dist += 1
            if grid[new_row][new_col] >= my_height:
                break
        dists.append(view_dist)
    return dists

def part2(grid):
    max_score = -1
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            score = math.prod(view_dists(grid, row, col))
            max_score = max(max_score, score)
    return max_score

grid = [list(map(int, list(l.rstrip()))) for l in fileinput.input()]
# print(grid)
print(part1(grid))
print(part2(grid))
