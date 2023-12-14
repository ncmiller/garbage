import fileinput

def prettyprint(lines):
    print('------------')
    for l in lines:
        print(''.join(l))

def part1(lines):
    total = 0
    for j in range(len(lines[0])):
        top = 0
        for i in range(len(lines)):
            if lines[i][j] == 'O':
                # print(i, j, top, 10 - top)
                total += (len(lines) - top)
                top += 1
            elif lines[i][j] == '#':
                top = i + 1
    return total

def north_load(lines):
    total = 0
    for j in range(len(lines[0])):
        for i in range(len(lines)):
            if lines[i][j] == 'O':
                total += len(lines) - i
    return total

def north(lines):
    for j in range(len(lines[0])):
        top = 0
        for i in range(len(lines)):
            if lines[i][j] == 'O':
                lines[top][j] = 'O'
                if top != i:
                    lines[i][j] = '.'
                top += 1
            elif lines[i][j] == '#':
                top = i + 1

def west(lines):
    for i in range(len(lines)):
        left = 0
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                lines[i][left] = 'O'
                if left != j:
                    lines[i][j] = '.'
                left += 1
            elif lines[i][j] == '#':
                left = j + 1

def south(lines):
    for j in range(len(lines[0])):
        bottom = len(lines) - 1
        for i in reversed(range(len(lines))):
            if lines[i][j] == 'O':
                lines[bottom][j] = 'O'
                if bottom != i:
                    lines[i][j] = '.'
                bottom -= 1
            elif lines[i][j] == '#':
                bottom = i - 1

def east(lines):
    for i in range(len(lines)):
        right = len(lines[0]) - 1
        for j in reversed(range(len(lines[0]))):
            if lines[i][j] == 'O':
                lines[i][right] = 'O'
                if right != j:
                    lines[i][j] = '.'
                right -= 1
            elif lines[i][j] == '#':
                right = j - 1

def part1_alt(lines):
    lines = [[c for c in line] for line in lines]
    # prettyprint(lines)
    north(lines)
    # prettyprint(lines)
    return north_load(lines)

def part2(lines):
    lines = [[c for c in line] for line in lines]
    n = 1000
    # prettyprint(lines)
    north_loads = []
    for cycle in range(n):
        north(lines)
        west(lines)
        south(lines)
        east(lines)
        north_loads.append(north_load(lines))

    # To find the cycle
    # for i, nl in enumerate(north_loads[:1000]):
    #     print(i+1, nl)

    # sample: 1-based index 38, length 7
    # (1000000000 - 38) % 7 = 3

    # Manually inspected input. There is a cycle starting
    # at 1-based index 923 with length 52
    #
    # (1000000000 - 923) % 52 = 25
    #
    # This index corresponds to value 100310
    # 100294 (too low)
    # 100299 (too low)
    # 100306 (too low)
    # 100317 (WA)

lines = [l[:-1] for l in fileinput.input()]
print(part1_alt(lines))
print(part2(lines))
