def compute(memory):
    idx = 0
    while True:
        opcode = memory[idx]
        if opcode == 99:
            break
        elif opcode == 1:
            data1 = memory[memory[idx+1]]
            data2 = memory[memory[idx+2]]
            target_idx = memory[idx+3]
            memory[target_idx] = data1 + data2
        elif opcode == 2:
            data1 = memory[memory[idx+1]]
            data2 = memory[memory[idx+2]]
            target_idx = memory[idx+3]
            memory[target_idx] = data1 * data2
        idx += 4
    return memory

def part1(code):
    memory = code[:]
    memory[1] = 12
    memory[2] = 2
    return compute(memory)[0]

def part2(code):
    target_output = 19690720
    for noun in range(100):
        for verb in range(100):
            memory = code[:]
            memory[1] = noun
            memory[2] = verb
            output = compute(memory)[0]
            if output == target_output:
                return 100 * noun + verb
    return -1

with open("day2_input.txt") as f:
    chars = f.read()
code = map(int, chars.split(','))

print(part1(code))

# not 460800
print(part2(code))
