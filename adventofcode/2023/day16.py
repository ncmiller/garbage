import fileinput

def oob(grid, x, y):
    return x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])

def num_energized(grid, x, y, d):
    #        x,  y,  dir ('NESW')
    beams = [[x, y, d]]
    dstep = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    forward_slash = {'N': 'E', 'E': 'N', 'S': 'W', 'W': 'S'}
    back_slash = {'N': 'W', 'E': 'S', 'S': 'E', 'W': 'N'}
    is_energized = set()
    visited = set()
    steps = 0
    while beams:
        beam = beams[0]
        while True:
            x, y, d = beam
            dx, dy = dstep[d]
            x += dx
            y += dy
            if (x,y,d) in visited or oob(grid, x, y):
                # print('done')
                break
            steps += 1
            # if steps == 100:
            #     exit(1)
            visited.add((x,y,d))
            is_energized.add((x,y))
            # print(x,y)
            if grid[x][y] == '.':
                pass
            elif grid[x][y] == '/':
                d = forward_slash[d]
            elif grid[x][y] == '\\':
                d = back_slash[d]
            elif grid[x][y] == '-':
                if d == 'N' or d == 'S':
                    d = 'E'
                    beams.append([x, y, 'W'])
            elif grid[x][y] == '|':
                if d == 'E' or d == 'W':
                    d = 'N'
                    beams.append([x, y, 'S'])
            beam = [x, y, d]
        beams = beams[1:]
    return len(is_energized)

def part1(grid):
    return num_energized(grid[:], 0, -1, 'E')

def part2(grid):
    max_n = -1
    for j in range(len(grid[0])):
        n = num_energized(grid[:], -1, j, 'S')
        max_n = max(max_n, n)
    for j in range(len(grid[0])):
        n = num_energized(grid[:], len(grid), j, 'N')
        max_n = max(max_n, n)
    for i in range(len(grid)):
        n = num_energized(grid[:], i, -1, 'E')
        max_n = max(max_n, n)
    for i in range(len(grid)):
        n = num_energized(grid[:], i, len(grid[0]), 'W')
        max_n = max(max_n, n)
    return max_n

grid = [l[:-1] for l in fileinput.input()]
print(part1(grid))
print(part2(grid))
