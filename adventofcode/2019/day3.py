import fileinput

def parse_moves(move_strings):
    moves = []
    for move_string in move_strings:
        moves.append((move_string[0], int(move_string[1:])))
    return moves

def follow_path(wire, grid, start, c):
    crossings = []
    position = list(start)
    moves = parse_moves(wire)
    for move in moves:
        nsteps = move[1]
        if move[0] == 'R':
            for _ in range(nsteps):
                position[1] += 1
                point = (position[0], position[1])
                if point in grid and grid[point] != c:
                    crossings.append(position[:])
                grid[point] = c
        elif move[0] == 'U':
            for _ in range(nsteps):
                position[0] -= 1
                point = (position[0], position[1])
                if point in grid and grid[point] != c:
                    crossings.append(position[:])
                grid[point] = c
        elif move[0] == 'L':
            for _ in range(nsteps):
                position[1] -= 1
                point = (position[0], position[1])
                if point in grid and grid[point] != c:
                    crossings.append(position[:])
                grid[point] = c
        elif move[0] == 'D':
            for _ in range(nsteps):
                position[0] += 1
                point = (position[0], position[1])
                if point in grid and grid[point] != c:
                    crossings.append(position[:])
                grid[point] = c
        else:
            assert(False)
    return crossings

def part1(wire1, wire2):
    # Central port at [0,0]
    center = (0,0)
    grid = {}
    grid[center] = 'O'

    # Follow wire1 path, mark with 1
    crossings = follow_path(wire1, grid, center, '1')

    # Follow wire2 path, if 1 encountered capture
    crossings = follow_path(wire2, grid, center, '2')

    # Compute min distance from crossings to center
    min_distance = 10000000
    min_row_col = (0,0)
    for crossing in crossings:
        row, col = crossing
        dist = abs(row) + abs(col)
        if dist < min_distance:
            min_row_col = (row, col)
            min_distance = dist
    return min_distance

lines = fileinput.input()
wire1 = lines[0].rstrip().split(",")
wire2 = lines[1].rstrip().split(",")

# not 2546
print(part1(wire1, wire2))
