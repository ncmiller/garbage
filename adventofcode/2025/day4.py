import fileinput

def neighbors(grid, row, col):
    neighbors = []
    coords = [
        (row-1,col-1),(row-1,col),(row-1,col+1),
        (row,col-1),(row,col+1),
        (row+1,col-1),(row+1,col),(row+1,col+1)
    ]
    for coord in coords:
        r,c = coord
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
            neighbors.append(grid[r][c])
    return neighbors

def part1(lines):
    accessible = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '@' and neighbors(lines, row, col).count('@') <= 3:
                # print(row,col)
                accessible += 1
    return accessible

def part2(lines):
    removed = 0
    while True:
        prev_removed = removed
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                if lines[row][col] == '@' and neighbors(lines, row, col).count('@') <= 3:
                    # print(row,col)
                    removed += 1
                    lines[row] = lines[row][:col] + '.' + lines[row][col+1:]
        if prev_removed == removed:
            break
    return removed

lines = list(fileinput.input())
lines = [l[:-1] for l in lines]
print(part1(lines))
print(part2(lines))
