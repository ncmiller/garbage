import fileinput

def part1(lines):
    pos = 50
    total_zeros = 0
    for line in lines:
        dir, amount = line[0], int(line[1:])
        if dir == 'L':
            pos = (pos - amount) % 100
        elif dir == 'R':
            pos = (pos + amount) % 100
        else:
            print('invalid')

        if pos == 0:
            total_zeros += 1

    return total_zeros

def part2(lines):
    pos = 50
    total_zero_clicks = 0
    for line in lines:
        dir = -1 if line[0] == 'L' else 1
        amount = int(line[1:])
        while amount != 0:
            pos = (pos + dir) % 100
            if pos == 0:
                total_zero_clicks += 1
            amount -= 1
    return total_zero_clicks

lines = list(fileinput.input())
print(part1(lines))
print(part2(lines))
