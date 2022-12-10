import fileinput

def part1(instructions):
    cycle = 0
    next_key_cycle = 20
    sig_strength = 0
    x = 1

    def incr_cycle_and_update_sig_strength():
        nonlocal cycle, next_key_cycle, sig_strength, x
        cycle += 1
        if cycle == next_key_cycle:
            sig_strength += (cycle * x)
            next_key_cycle += 40

    for ins in instructions:
        if ins[0] == 'addx':
            incr_cycle_and_update_sig_strength()
            incr_cycle_and_update_sig_strength()
            x += int(ins[1])
        else:
            incr_cycle_and_update_sig_strength()

    return sig_strength

def print_crt(crt):
    for row in crt:
        print(''.join(row))

def cycle_to_crt_pos(cycle):
    cycle0 = (cycle - 1) % 240
    row = cycle0 // 40
    col = cycle0 % 40
    return (row,col)

def part2(instructions):
    crt = [['.' for _ in range(40)] for _ in range(6)]

    cycle = 0
    x = 1

    def incr_cycle_and_set_pixel():
        nonlocal cycle, x
        cycle += 1
        row, col = cycle_to_crt_pos(cycle)
        if col >= (x - 1) and col <= (x + 1):
            crt[row][col] = '#'
        else:
            crt[row][col] = '.'

    for ins in instructions:
        if ins[0] == 'addx':
            incr_cycle_and_set_pixel()
            incr_cycle_and_set_pixel()
            x += int(ins[1])
        else:
            incr_cycle_and_set_pixel()

    print_crt(crt)

instructions = [l.rstrip().split(' ') for l in fileinput.input()]
print(part1(instructions))
part2(instructions)
