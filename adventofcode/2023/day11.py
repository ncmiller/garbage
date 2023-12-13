import fileinput

def prettyprint(rows):
    for r in rows:
        print(''.join(r))

def expand(rows):
    for i in reversed(range(len(rows))):
        if all([c == '.' for c in rows[i]]):
            rows = rows[:i] + [rows[i]] + rows[i:]
    return rows

def transpose(rows):
    return [list(i) for i in zip(*rows)]

def part1(rows):
    rows = expand(rows)
    rows = transpose(rows)
    rows = expand(rows)
    rows = transpose(rows)
    galaxies = []
    for i,r in enumerate(rows):
        for j,c in enumerate(r):
            if c == '#':
                galaxies.append((i,j))

    total_steps = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            total_steps += abs(x1 - x2) + abs(y1 - y2)
    return total_steps

def empty_rows(rows):
    empty_rows = []
    for i,r in enumerate(rows):
        if all([c == '.' for c in rows[i]]):
            empty_rows.append(i)
    return empty_rows

def part2(rows, expansion):
    ers = empty_rows(rows)
    rows = transpose(rows)
    ecs = empty_rows(rows)
    rows = transpose(rows)
    # print(ers, ecs)
    galaxies = []
    for i,r in enumerate(rows):
        for j,c in enumerate(r):
            if c == '#':
                # count number of empty rows inserted before i, add to i
                # count number of empty cols inserted before j, add to j
                ers_before_i = len([er for er in ers if er < i])
                ecs_before_j = len([ec for ec in ecs if ec < j])
                galaxies.append((i + (expansion - 1) * ers_before_i, j + (expansion - 1) * ecs_before_j))
    # print(galaxies)

    total_steps = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            total_steps += abs(x1 - x2) + abs(y1 - y2)
    return total_steps

rows = [[c for c in line[:-1]] for line in fileinput.input()]
print(part1(rows))
# prettyprint(rows)
print(part2(rows, 1000000))
