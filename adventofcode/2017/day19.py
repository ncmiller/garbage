import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)

N = max([len(line) for line in lines])
N = max(N, len(lines))
grid = [[' ' for _ in range(N)] for _ in range(N)]

row = 0
for line in lines:
    col = 0
    for c in line:
        if c != ' ':
            grid[row][col] = c
        col += 1
    row += 1

def next_pos(pos, d):
    if d == 0:
        pos = (pos[0]+1, pos[1])
    elif d == 1:
        pos = (pos[0], pos[1]-1)
    elif d == 2:
        pos = (pos[0]-1, pos[1])
    elif d == 3:
        pos = (pos[0], pos[1]+1)
    return pos

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
found = []
steps = 0
pos = (0, grid[0].index('|'))
d = 0 # 0 = down, 1 = left, 2 = up, 3 = right
while 1:
    # print pos
    c = grid[pos[0]][pos[1]]
    if c in letters:
        found.append(c)
    if c == ' ':
        break
    if d == 0 or d == 2:
        if c == '+':
            if grid[pos[0]][pos[1]-1] != ' ':
                d = 1
            else:
                d = 3
    elif d == 1 or d == 3:
        if c == '+':
            if grid[pos[0]-1][pos[1]] != ' ':
                d = 2
            else:
                d = 0

    steps += 1
    pos = next_pos(pos, d)

print 'found', ''.join(found)
print steps
