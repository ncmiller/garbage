import fileinput

N = 1001
grid = [['.' for _ in range(N)] for _ in range(N)]

lines = []
for line in fileinput.input():
    lines.append(line.strip())
size = len(lines)

x, y = (N//2 - size//2, N//2 - size//2)
for row in range(size):
    for col in range(size):
        grid[y+row][x+col] = lines[row][col]

row, col = (N//2, N//2)
facing = 0 # 0 = up, 1 = right, 2 = down, 3 = left

def turn(facing, turn): # turn 0 = left, 1 = right
    if facing == 0 and turn == 0: return 3
    if facing == 0 and turn == 1: return 1
    if facing == 1 and turn == 0: return 0
    if facing == 1 and turn == 1: return 2
    if facing == 2 and turn == 0: return 1
    if facing == 2 and turn == 1: return 3
    if facing == 3 and turn == 0: return 2
    if facing == 3 and turn == 1: return 0

def move(row, col, facing):
    if facing == 0: return row-1, col
    if facing == 1: return row, col+1
    if facing == 2: return row+1, col
    if facing == 3: return row, col-1


# PART 1
# steps = 10000
# num_infections = 0
# for i in range(steps):
#     if grid[row][col] == '#':
#         facing = turn(facing, 1)
#         grid[row][col] = '.'
#         row, col = move(row, col, facing)
#     elif grid[row][col] == '.':
#         facing = turn(facing, 0)
#         grid[row][col] = '#'
#         num_infections += 1
#         row, col = move(row, col, facing)

# print num_infections

# clean .
# weak /
# infected #
# flagged *

def nextstate(s):
    if s == '.': return '/'
    if s == '/': return '#'
    if s == '#': return '*'
    if s == '*': return '.'

# PART 2
steps = 10000000
num_infections = 0
for i in range(steps):
    if grid[row][col] == '.':
        facing = turn(facing, 0)
    elif grid[row][col] == '#':
        facing = turn(facing, 1)
    elif grid[row][col] == '*':
        facing = turn(facing, 1)
        facing = turn(facing, 1)

    next = nextstate(grid[row][col])
    if next == '#':
        num_infections += 1
    grid[row][col] = next

    row, col = move(row, col, facing)

print num_infections
