import fileinput
import regex

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

def identity(pos, N): return pos
def swap_reflect(pos, N): return (N-pos[1]-1, N-pos[0]-1)
def swap(pos, N): return (pos[1],pos[0])
def reflect_y(pos, N): return (N-pos[0]-1, pos[1])
def reflect_x(pos, N): return (pos[0], N-pos[1]-1)

# Manually constructed tables for part 2, mapping portals at outside edges for sample and input
# (square_y, square_x, facing) -> (square_y, square_x, function, facing)
SAMPLE_N = 4
sample_portals = {
        (0, 2, UP): (1, 0, identity, DOWN),
        (0, 2, RIGHT): (2, 3, identity, LEFT),
        (1, 2, RIGHT): (2, 3, swap_reflect, DOWN),
        (2, 3, UP): (1, 2, swap_reflect, LEFT),
        (2, 3, RIGHT): (0, 2, identity, LEFT),
        (2, 3, DOWN): (1, 0, swap_reflect, RIGHT),
        (2, 2, DOWN): (1, 0, reflect_x, UP),
        (2, 2, LEFT): (1, 1, swap_reflect, UP),
        (1, 1, DOWN): (2, 2, swap_reflect, RIGHT),
        (1, 0, DOWN): (2, 2, identity, UP),
        (1, 0, LEFT): (2, 3, swap_reflect, UP),
        (1, 0, UP): (0, 2, identity, DOWN),
        (1, 1, UP): (0, 2, swap, RIGHT),
        (0, 2, LEFT): (1, 1, swap),
}

INPUT_N = 50
input_portals = {
        (0,1,UP): (3,0,swap,RIGHT),
        (0,2,UP): (3,0,reflect_y,UP),
        (0,2,RIGHT): (2,1,reflect_y,LEFT),
        (1,1,RIGHT): (0,2,swap,UP),
        (2,1,RIGHT): (0,2,reflect_y,LEFT),
        (2,1,DOWN): (3,0,swap,LEFT),
        (3,0,RIGHT): (2,1,swap,UP),
        (3,0,LEFT): (0,1,swap,DOWN),
        (2,0,LEFT): (0,1,reflect_y,RIGHT),
        (2,0,UP): (1,1,swap,RIGHT),
        (1,1,LEFT): (2,0,swap, DOWN),
        (0,1,LEFT): (2,0,reflect_y,RIGHT),
        (0,2,DOWN): (1,1, swap, LEFT),
        (3,0,DOWN): (0,2,reflect_y, DOWN),
}

def get_edges(grid):
    # indexed by column
    tops = []
    bottoms = []
    for col_i in range(len(grid[0])):
        for row_i in range(len(grid)):
            if grid[row_i][col_i] != ' ':
                tops.append((row_i, col_i))
                break
        for row_i in reversed(range(len(grid))):
            if grid[row_i][col_i] != ' ':
                bottoms.append((row_i, col_i))
                break

    # indexed by row
    lefts = []
    rights = []
    for row_i in range(len(grid)):
        for col_i in range(len(grid[0])):
            if grid[row_i][col_i] != ' ':
                lefts.append((row_i, col_i))
                break
        for col_i in reversed(range(len(grid[0]))):
            if grid[row_i][col_i] != ' ':
                rights.append((row_i, col_i))
                break
    return tops, bottoms, lefts, rights

def step_part1(pos, facing, dpos, nsteps, grid, edges):
    dp = dpos[facing]
    tops, bottoms, lefts, rights = edges

    for _ in range(nsteps):
        # print(pos, facing)
        next_pos = [pos[0]+dp[0], pos[1]+dp[1]]
        if facing == UP and (next_pos[0] < tops[next_pos[1]][0] or next_pos[0] == ' '):
            next_pos[0] = bottoms[next_pos[1]][0]
        elif facing == DOWN and (next_pos[0] > bottoms[next_pos[1]][0] or next_pos[0] == ' '):
            next_pos[0] = tops[next_pos[1]][0]
        elif facing == RIGHT and (next_pos[1] > rights[next_pos[0]][1] or next_pos[1] == ' '):
            next_pos[1] = lefts[next_pos[0]][1]
        elif facing == LEFT and (next_pos[1] < lefts[next_pos[0]][1] or next_pos[1] == ' '):
            next_pos[1] = rights[next_pos[0]][1]

        next_char = grid[next_pos[0]][next_pos[1]]
        assert(next_char != ' ')
        if next_char == '#':
            break
        pos = next_pos
    return pos

def part1(grid, moves):
    #       right, down,  left    up
    dpos = ((0,1), (1,0), (0,-1), (-1,0))
    facing = RIGHT
    pos = (0, grid[0].index('.'))
    edges = get_edges(grid)
    for nsteps,turn in moves:
        pos = step_part1(pos, facing, dpos, nsteps, grid, edges)
        if turn == 'R':
            facing = (facing + 1) % len(dpos)
        elif turn == 'L':
            facing = (facing - 1) % len(dpos)
    # print(pos)
    return 1000*(pos[0]+1) + 4*(pos[1]+1) + facing

def step_part2(pos, facing, dpos, nsteps, grid, N, portals):
    for _ in range(nsteps):
        # print(pos, facing)
        dp = dpos[facing]
        next_facing = facing
        pos_square = (pos[0] // N, pos[1] // N)
        pos_offset = (pos[0] % N, pos[1] % N)
        next_pos_offset = [pos_offset[0]+dp[0], pos_offset[1]+dp[1]]
        portal_key = (pos_square[0], pos_square[1], facing)
        if ((portal_key in portals) and
            ((facing == UP and next_pos_offset[0] < 0) or
             (facing == RIGHT and next_pos_offset[1] >= N) or
             (facing == DOWN and next_pos_offset[0] >= N) or
             (facing == LEFT and next_pos_offset[1] < 0))):
            next_square_y, next_square_x, fn, next_facing = portals[portal_key]
            next_pos_offset = fn(pos_offset, N)
            next_pos = [next_square_y * N + next_pos_offset[0], next_square_x * N + next_pos_offset[1]]
            next_facing = next_facing
        else:
            next_pos = [pos[0]+dp[0], pos[1]+dp[1]]

        next_char = grid[next_pos[0]][next_pos[1]]
        assert(next_char != ' ')
        if next_char == '#':
            break
        pos = next_pos
        facing = next_facing
    return pos, facing

def part2(grid, moves, N, portals):
    dpos = ((0,1), (1,0), (0,-1), (-1,0))
    facing = RIGHT
    pos = (0, grid[0].index('.'))
    for nsteps,turn in moves:
        pos, facing = step_part2(pos, facing, dpos, nsteps, grid, N, portals)
        if turn == 'R':
            facing = (facing + 1) % len(dpos)
        elif turn == 'L':
            facing = (facing - 1) % len(dpos)
    return 1000*(pos[0]+1) + 4*(pos[1]+1) + facing

lines = [line.rstrip() for line in fileinput.input()]
moves = regex.findall(r'(\d+)([RL]?)', lines[-1])
moves = [(int(n), turn) for n, turn in moves]
width = max(len(l) for l in lines[:-2])
grid = [l + ' ' * (width - len(l)) for l in lines[:-2]]
print(part1(grid, moves))

# sample
# N = SAMPLE_N
# portals = sample_portals
# input
N = INPUT_N
portals = input_portals
print(part2(grid, moves, N, portals))
