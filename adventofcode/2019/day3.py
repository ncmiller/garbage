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
    total_steps = 0
    for move in moves:
        nsteps = move[1]
        if move[0] == 'R':
            for _ in range(nsteps):
                position[1] += 1
                total_steps += 1
                point = (position[0], position[1])
                if point in grid and grid[point][0] != c:
                    crossings.append((position[:], total_steps + grid[point][1]))
                grid[point] = (c, total_steps)
        elif move[0] == 'U':
            for _ in range(nsteps):
                position[0] -= 1
                total_steps += 1
                point = (position[0], position[1])
                if point in grid and grid[point][0] != c:
                    crossings.append((position[:], total_steps + grid[point][1]))
                grid[point] = (c, total_steps)
        elif move[0] == 'L':
            for _ in range(nsteps):
                position[1] -= 1
                total_steps += 1
                point = (position[0], position[1])
                if point in grid and grid[point][0] != c:
                    crossings.append((position[:], total_steps + grid[point][1]))
                grid[point] = (c, total_steps)
        elif move[0] == 'D':
            for _ in range(nsteps):
                position[0] += 1
                total_steps += 1
                point = (position[0], position[1])
                if point in grid and grid[point][0] != c:
                    crossings.append((position[:], total_steps + grid[point][1]))
                grid[point] = (c, total_steps)
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
    # print(crossings)

    # Compute min distance from crossings to center
    min_distance = 10000000
    min_row_col = (0,0)
    for crossing in crossings:
        (row, col), steps = crossing
        dist = abs(row) + abs(col)
        if dist < min_distance:
            min_row_col = (row, col)
            min_distance = dist
    return min_distance

def part2(wire1, wire2):
    # Central port at [0,0]
    center = (0,0)
    grid = {}
    grid[center] = 'O'

    # Follow wire1 path, mark with 1
    crossings = follow_path(wire1, grid, center, '1')

    # Follow wire2 path, if 1 encountered capture
    crossings = follow_path(wire2, grid, center, '2')
    # print(crossings)

    # Compute min latency
    min_latency = 10000000
    min_row_col = (0,0)
    for crossing in crossings:
        (row, col), steps = crossing
        if steps < min_latency:
            min_latency = steps
            min_row_col = (row, col)
    return min_latency

lines = fileinput.input()
wire1 = lines[0].rstrip().split(",")
wire2 = lines[1].rstrip().split(",")

# not 2546
print(part1(wire1, wire2))

print(part2(wire1, wire2))
