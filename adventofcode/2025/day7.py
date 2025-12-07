import fileinput
import copy

def part1(grid):
    start = grid[0].index('S')
    grid[1][start] = '|'
    splits = 0
    for i in range(1, len(grid)-1):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '|' and (i+1) < len(grid):
                if grid[i+1][j] == '^':
                    splits += 1
                    if j >= 1:
                        grid[i+1][j-1] = '|'
                    if j < len(grid[0])-1:
                        grid[i+1][j+1] = '|'
                else:
                    grid[i+1][j] = '|'
    return splits


def run_timeline(grid, row, col, memo):
    if (row, col) in memo:
        return memo[(row,col)]

    # move down until we hit a ^
    for i in range(row, len(grid)-1):
        if grid[i][col] == '^':
            num_timelines = 0
            if col >= 1:
                num_timelines += run_timeline(grid, i, col-1, memo)
            if col < len(grid[0])-1:
                num_timelines += run_timeline(grid, i, col+1, memo)
            memo[(row,col)] = num_timelines
            return num_timelines

    # didn't hit a splitter, just return 1
    memo[(row, col)] = 1
    return 1

def part2(grid):
    start = grid[0].index('S')
    grid[1][start] = '|'
    memo = dict()
    run_timeline(grid[1:], 1, start, memo)
    return memo[(1,start)]

grid = [list(line[:-1]) for line in fileinput.input()]
print(part1(grid))
print(part2(grid))
