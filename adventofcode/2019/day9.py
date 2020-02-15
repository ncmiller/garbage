import itertools

# nparams includes the opcode itself
# actual num params is nparams - 1
opcode_nparams = {
    1: 4,  # add
    2: 4,  # mult
    3: 2,  # input
    4: 2,  # output
    5: 3,  # jump-if-true
    6: 3,  # jump-if-false
    7: 4,  # less-than
    8: 4,  # equals
    9: 2,  # set-rbo (relative base offset)
    99: 1, # halt
}

# ABCDE
#
# DE: opcode
# C: param 0 mode
# B: param 1 mode
# A: param 2 mode
# ...
def parse_opcode(opcode):
    opcode_str = str(opcode)
    code = int(opcode_str[-2:])
    nexpected_chars = 2 + opcode_nparams[code] - 1
    diff = nexpected_chars - len(opcode_str)
    padded_opcode_str = "0" * diff + opcode_str
    modes = map(int, padded_opcode_str[:-2][::-1])
    return (code, modes)

def get_data(memory, mode, addr, rbo):
    if mode == 1: # immediate
        return memory[addr]
    else: # position or relative mode, need to lookup addr
        return memory[get_addr(memory, mode, addr, rbo)]

def get_addr(memory, mode, addr, rbo):
    val = memory[addr]
    if mode == 0: # position
        return val
    elif mode == 2: # relative
        return rbo + val
    else: # unknown
        assert(False)

# input: (memory, pc, rbo, inputs, output)
# returns: (memory, pc, rbo, output), halted
def compute(state):
    memory, pc, rbo, inputs, output = state
    halted = False
    while True:
        jumping = False
        opcode, modes = parse_opcode(memory[pc])
        if opcode == 99:
            halted = True
            break
        elif opcode == 1:
            data1 = get_data(memory, modes[0], pc + 1, rbo)
            data2 = get_data(memory, modes[1], pc + 2, rbo)
            target_idx = get_addr(memory, modes[2], pc + 3, rbo)
            memory[target_idx] = data1 + data2
        elif opcode == 2:
            data1 = get_data(memory, modes[0], pc + 1, rbo)
            data2 = get_data(memory, modes[1], pc + 2, rbo)
            target_idx = get_addr(memory, modes[2], pc + 3, rbo)
            memory[target_idx] = data1 * data2
        elif opcode == 3:
            if not inputs: # must yield until inputs available
                break
            target_idx = get_addr(memory, modes[0], pc + 1, rbo)
            memory[target_idx] = inputs[0]
            inputs = inputs[1:]
        elif opcode == 4:
            data1 = get_data(memory, modes[0], pc + 1, rbo)
            output = data1
            print(data1)
        elif opcode == 5:
            data1 = get_data(memory, modes[0], pc + 1, rbo)
            jump_idx = get_data(memory, modes[1], pc + 2, rbo)
            if data1 != 0:
                jumping = True
                pc = jump_idx
        elif opcode == 6:
            data1 = get_data(memory, modes[0], pc + 1, rbo)
            jump_idx = get_data(memory, modes[1], pc + 2, rbo)
            if data1 == 0:
                jumping = True
                pc = jump_idx
        elif opcode == 7:
            data1 = get_data(memory, modes[0], pc + 1, rbo)
            data2 = get_data(memory, modes[1], pc + 2, rbo)
            target_idx = get_addr(memory, modes[2], pc + 3, rbo)
            if data1 < data2:
                memory[target_idx] = 1
            else:
                memory[target_idx] = 0
        elif opcode == 8:
            data1 = get_data(memory, modes[0], pc + 1, rbo)
            data2 = get_data(memory, modes[1], pc + 2, rbo)
            target_idx = get_addr(memory, modes[2], pc + 3, rbo)
            if data1 == data2:
                memory[target_idx] = 1
            else:
                memory[target_idx] = 0
        elif opcode == 9:
            data1 = get_data(memory, modes[0], pc + 1, rbo)
            rbo += data1
        if not jumping:
            pc += opcode_nparams[opcode]
    return (memory, pc, rbo, output), halted

def part1(code):
    memsize = 2**16
    mempad = memsize - len(code)

    mem = code[:] + [0] * mempad
    rbo = 0
    pc = 0
    inputs = [2]
    output = 0
    halted = False
    while not halted:
        (mem, pc, rbo, output), halted = compute((mem, pc, rbo, inputs, output))

def part2(code):
    pass

with open("day9_input.txt") as f:
    chars = f.read()
code = map(int, chars.split(','))

part1(code)
part2(code)
