import fileinput
from collections import defaultdict

def has_neighbor_elf(elves, query_pos):
    row,col = query_pos
    neighbor_pos = [
        (row-1,col-1),(row-1,col),(row-1,col+1),
        (row,col-1),(row,col+1),
        (row+1,col-1),(row+1,col),(row+1,col+1),
    ]
    has_neighbor = any([pos in elves for pos in neighbor_pos])
    return has_neighbor

def dir_has_elf(elves, pos, dir):
    row, col = pos
    if dir == 0: # N
        check_pos = [(row-1,col-1),(row-1,col),(row-1,col+1)]
    elif dir == 1: # S
        check_pos = [(row+1,col-1),(row+1,col),(row+1,col+1)]
    elif dir == 2: # W
        check_pos = [(row-1,col-1),(row,col-1),(row+1,col-1)]
    elif dir == 3: # E
        check_pos = [(row-1,col+1),(row,col+1),(row+1,col+1)]
    return any([pos in elves for pos in check_pos]), check_pos[1]

def sim(elves, N):
    dirs = [0, 1, 2, 3] # N S W E
    for round in range(N):
        proposed_positions = defaultdict(list) # new_pos -> [elf]
        for e in elves:
            if not has_neighbor_elf(elves, e):
                continue
            for d in dirs:
                has_elf, new_pos = dir_has_elf(elves, e, d)
                if not has_elf:
                    proposed_positions[new_pos].append(e)
                    break

        num_moves = 0
        for new_pos, es in proposed_positions.items():
            if len(es) == 1:
                # remove old pos, add new pos
                num_moves += 1
                elves.remove(es[0])
                elves.add(new_pos)

        if num_moves == 0:
            # done with sim
            break

        dirs = dirs[1:] + [dirs[0]]
    return elves, round + 1

def part1(elves):
    elves, _ = sim(elves, 10)
    empty = 0
    min_row = min([e[0] for e in elves])
    min_col = min([e[1] for e in elves])
    max_row = max([e[0] for e in elves])
    max_col = max([e[1] for e in elves])
    for row_i in range(min_row, max_row+1):
        for col_i in range(min_col, max_col+1):
            if (row_i,col_i) not in elves:
                empty += 1
    return empty

def part2(elves):
    _, round = sim(elves, 1000000)
    return round

lines = [line.rstrip() for line in fileinput.input()]
elves = set()
for row_i in range(len(lines)):
    for col_i in range(len(lines[row_i])):
        if lines[row_i][col_i] == '#':
            elves.add((row_i, col_i))

print(part1(elves.copy()))
print(part2(elves.copy()))
