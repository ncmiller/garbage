import fileinput

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def print_grid_n(grid, n):
    for r in range(n):
        row = grid[r][:n]
        print(''.join(row))

def count_hashes(grid):
    count = 0
    for row in grid:
        count += sum([1 for c in row if c == '#'])
    return count

lines = list(fileinput.input())
dot_coords = []
folds = []
for i in range(len(lines)):
    l = lines[i]
    if l[0] == 'f':
        words = l.split(' ')
        axis = (0 if words[2][0] == 'x' else 1) # 0 == x, 1 == y
        loc = int(words[2].rstrip().split('=')[1])
        folds.append((axis, loc))
    elif l == '\n':
        pass
    else:
        dot_coords.append(list(map(int, l.rstrip().split(','))))

maxX = max([x for x, y in dot_coords])
maxY = max([y for x, y in dot_coords])

# print(dot_coords)
# print(maxX, maxY)

grid = [['.'] * (maxX + 1) for _ in range(maxY + 1)]
# print_grid(grid)

for c in dot_coords:
    x,y = c
    grid[y][x] = '#'

# print_grid(grid)
# print()

# print(len(grid))
# print(len(dot_coords))
# print(len(folds))

for fold in folds:
    axis, loc = fold
    print(axis, loc)
    if axis == 0: # x
        for c in range(loc+1, len(grid[0])):
            for r in range(len(grid)):
                dist_from_fold = c - loc
                reflect = loc - dist_from_fold
                if reflect < 0:
                    break
                if grid[r][c] == '#':
                    grid[r][c] = '.'
                    grid[r][reflect] = '#'
    else: # y
        for r in range(loc+1, len(grid)):
            for c in range(len(grid[0])):
                dist_from_fold = r - loc
                reflect = loc - dist_from_fold
                if reflect < 0:
                    break
                if grid[r][c] == '#':
                    grid[r][c] = '.'
                    grid[reflect][c] = '#'
    # print_grid(grid)
    # print()

print_grid_n(grid, 100)
print(count_hashes(grid))

# part 1
#    799, too high
#    748, too high
