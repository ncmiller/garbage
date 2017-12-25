def button(current, seq):
    buttons = [[1,2,3],[4,5,6],[7,8,9]]
    row = current // 3
    col = current % 3
    for step in seq:
        if step == 'L' and col > 0: col -= 1
        if step == 'R' and col < 2: col += 1
        if step == 'U' and row > 0: row -= 1
        if step == 'D' and row < 2: row += 1
    return buttons[row][col]

def part1(sequences):
    b = 5
    pw = []
    for s in sequences:
        b = button(b-1, s)
        pw.append(b)
    return ''.join(map(str, pw))

with open("day2_input.txt") as f:
    sequences = f.readlines()

print part1(sequences)

#----------------------------------------

def button2(current, seq):
    buttons = [
        [0,0,1,0,0],
        [0,2,3,4,0],
        [5,6,7,8,9],
        [0,'A','B','C',0],
        [0,0,'D',0,0]
    ]

    buttonmap = {
        1: (0, 2),
        2: (1, 1),
        3: (1, 2),
        4: (1, 3),
        5: (2, 0),
        6: (2, 1),
        7: (2, 2),
        8: (2, 3),
        9: (2, 4),
        'A': (3, 1),
        'B': (3, 2),
        'C': (3, 3),
        'D': (4, 2),
    }

    row, col = buttonmap[current]

    for step in seq:
        if step == 'L' and col > 0 and buttons[row][col-1] != 0: col -= 1
        if step == 'R' and col < 4 and buttons[row][col+1] != 0: col += 1
        if step == 'U' and row > 0 and buttons[row-1][col] != 0: row -= 1
        if step == 'D' and row < 4 and buttons[row+1][col] != 0: row += 1

    return buttons[row][col]

def part2(sequences):
    b = 5
    pw = []
    for s in sequences:
        b = button2(b, s)
        pw.append(b)
    return ''.join(map(str, pw))

print part2(sequences)
