import fileinput

def prettyprint(rows):
    print('------------')
    for r in rows:
        print(''.join(r))
    print('------------')

def transpose(rows):
    return [list(i) for i in zip(*rows)]

def find_row_reflect(pattern):
    found_splits = []
    for split in range(1,len(pattern)):
        a, b = pattern[:split], pattern[split:]
        if len(a) < len(b):
            b = b[:len(a)]
        else:
            a = a[-len(b):]
        # print(split, [''.join(x) for x in a], [''.join(y) for y in b])
        # print(list(reversed(a)), b)
        if list(reversed(a)) == b:
            # print('found', split)
            found_splits.append(split)
    return found_splits

def part1(patterns):
    total = 0
    for p in patterns:
        # prettyprint(p)
        row_reflects = find_row_reflect(p)
        if not row_reflects:
            row_reflects = find_row_reflect(transpose(p))
            total += row_reflects[0]
        else:
            total += (100 * row_reflects[0])
    return total

def flip(c):
    if c == '#':
        return '.'
    else:
        return '#'

def find_row_or_col_reflect(p):
    row_reflects = find_row_reflect(p)
    col_reflects = find_row_reflect(transpose(p))
    return row_reflects, col_reflects

def part2(patterns):
    total = 0
    for p in patterns:
        orig_rows, orig_cols = find_row_or_col_reflect(p)
        orig_reflections = set()
        for r in orig_rows:
            orig_reflections.add((r, 0))
        for c in orig_cols:
            orig_reflections.add((c, 1))


        # try mutating each character in pattern
        found_reflections = set()
        for i in range(len(p)):
            for j in range(len(p[0])):
                p[i][j] = flip(p[i][j])
                # if i == 6 and j == 4:
                #     prettyprint(transpose(p))
                new_rows, new_cols = find_row_or_col_reflect(p)
                p[i][j] = flip(p[i][j])
                if new_rows:
                    for nr in new_rows:
                        if (nr, 0) in orig_reflections:
                            continue
                        found_reflections.add((nr, 0))
                if new_cols:
                    for nc in new_cols:
                        if (nc, 1) in orig_reflections:
                            continue
                        found_reflections.add((nc, 1))
        # print(patterns.index(p), 'orig', orig_reflections, 'new', found_reflections)

        for val, is_col in found_reflections:
            if is_col:
                total += val
            else:
                total += (100 * val)

    return total

lines = [l[:-1] for l in fileinput.input()]
patterns = []
pattern = []
for l in lines:
    if l == '':
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append([c for c in l])
patterns.append(pattern)
# prettyprint(patterns[0])
# prettyprint(transpose(patterns[0]))

print(part1(patterns))
print(part2(patterns))
