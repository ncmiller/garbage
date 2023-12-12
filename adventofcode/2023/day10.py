import fileinput

pipe_connection_map = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)],
}

def print_rows(rows):
    for r in rows:
        print(r)

def char_at(rows, pos):
    return rows[pos[0]][pos[1]]

def set_char(rows, pos, new_char):
    new_rows = rows[:]
    pos_row = pos[0]
    new_rows[pos_row] = rows[pos_row].replace('S', new_char)
    return new_rows

def in_bounds(rows, pos):
    return pos[0] >= 0 and pos[0] < len(rows) and pos[1] >= 0 and pos[1] < len(rows[0])

def is_pipe(rows, pos):
    return char_at(rows, pos) != '.'

def add_coords(a, b):
    return (a[0] + b[0], a[1] + b[1])

# returns next
def find_next(rows, current, prev):
    row_diff = current[0] - prev[0]
    col_diff = current[1] - prev[1]
    c = char_at(rows, current)
    n = None
    if c == '|':
        if row_diff == 1:
            n = (current[0] + 1, current[1]) # down
        elif row_diff == -1:
            n = (current[0] - 1, current[1]) # up
    elif c == '-':
        if col_diff == 1:
            n = (current[0], current[1] + 1) # right
        elif col_diff == -1:
            n = (current[0], current[1] - 1) # left
    elif c == 'L':
        if row_diff == 1:
            n = (current[0], current[1] + 1) # right
        elif col_diff == -1:
            n = (current[0] - 1, current[1]) # up
    elif c == 'J':
        if row_diff == 1:
            n = (current[0], current[1] - 1) # left
        elif col_diff == 1:
            n = (current[0] - 1, current[1]) # up
    elif c == '7':
        if col_diff == 1:
            n = (current[0] + 1, current[1]) # down
        elif row_diff == -1:
            n = (current[0], current[1] - 1) # left
    elif c == 'F':
        if col_diff == -1:
            n = (current[0] + 1, current[1]) # down
        elif row_diff == -1:
            n = (current[0], current[1] + 1) # right

    return n if n and in_bounds(rows, n) and is_pipe(rows, n) else None

def find_s_pipe(rows, s):
    for pipe in '|-LJ7F':
        a,b = pipe_connection_map[pipe]
        na = add_coords(s, a)
        nb = add_coords(s, b)
        # print(pipe, na, nb)
        if not in_bounds(rows, na) or not in_bounds(rows, nb):
            continue
        if find_next(rows, na, s) and find_next(rows, nb, s):
            return pipe
        # if is_pipe(rows, na) and is_pipe(rows, nb):

def part1(rows, start):
    s_pipe = find_s_pipe(rows, start)
    new_rows = set_char(rows, start, s_pipe)
    # print_rows(new_rows)
    steps = 0
    current = start
    prev = add_coords(start, pipe_connection_map[s_pipe][0])
    while current != start or steps == 0:
        n = find_next(new_rows, current, prev)
        # print(current, char_at(new_rows, current), n)
        steps += 1
        current, prev = n, current
    return steps//2

def flood_fill_size(rows, to_visit):
    to_visit = list(to_visit)
    print(len(to_visit), to_visit)
    visited = set()
    sz = 0
    for v in to_visit:
        if v in visited:
            continue
        visited.add(v)
        sz += 1
        neighbors = [
            add_coords(v, (-1, 0)),
            add_coords(v, (0, 1)),
            add_coords(v, (-1, 0)),
            add_coords(v, (0, -1))
        ]
        neighbors = [n for n in neighbors if in_bounds(rows, n) and char_at(rows, n) == '.' and n not in visited]
        for n in neighbors:
            to_visit.append(n)
    return sz

def part2(rows, start):
    # F: if were outside, toggle. if were inside, then it's bottom edge, otherwise top edge
    # J: if is bottom edge, toggle, otherwise do nothing
    # L: if were outside, toggle. if were inside, it's top edge, else bottom edge
    # 7: if is top edge, toggle, otherwise do nothing
    # -: ignore
    # |: toggle

    s_pipe = find_s_pipe(rows, start)
    new_rows = set_char(rows, start, s_pipe)
    # print_rows(new_rows)
    steps = 0
    current = start
    prev = add_coords(start, pipe_connection_map[s_pipe][0])
    loop_coords = []
    while current != start or steps == 0:
        loop_coords.append(current)
        n = find_next(new_rows, current, prev)
        # print(current, char_at(new_rows, current), n)
        steps += 1
        current, prev = n, current

    # print(loop_coords)

    is_outside = True
    is_top = False
    inside_coords = []
    for i, row in enumerate(new_rows):
        for j, col in enumerate(row):
            if col == 'F' and (i,j) in loop_coords:
                if is_outside:
                    is_outside = False
                    is_top = True
                else:
                    is_top = False
            elif col == 'J' and (i,j) in loop_coords:
                if not is_top:
                    is_outside = not is_outside
            elif col == 'L' and (i,j) in loop_coords:
                if is_outside:
                    is_outside = False
                    is_top = False
                else:
                    is_top = True
            elif col == '7' and (i,j) in loop_coords:
                if is_top:
                    is_outside = not is_outside
            elif col == '-' and (i,j) in loop_coords:
                pass
            elif col == '|' and (i,j) in loop_coords:
                is_outside = not is_outside
            elif (i,j) not in loop_coords and not is_outside:
                # print('found one', (i,j))
                inside_coords.append((i,j))
            # print((i,j), col, 0 if is_outside else 1, 'T' if is_top else 'B', (i,j) in loop_coords)

    # print(inside_coords)
    return len(inside_coords)

rows = [line[:-1] for line in fileinput.input()]
for i, row in enumerate(rows):
    if 'S' in row:
        start = (i, row.index('S'))
        break

# for row in rows:
#     print(row)
# print(start)

print(part1(rows, start)) # 6603 (too low)
print(part2(rows, start))
