import itertools

opcode_nparams = {
    1: 4,  # add
    2: 4,  # mult
    3: 2,  # input
    4: 2,  # output
    5: 3,  # jump-if-true
    6: 3,  # jump-if-false
    7: 4,  # less-than
    8: 4,  # equals
    99: 1, # halt
}

def parse_opcode(opcode):
    opcode_str = str(opcode)
    code = int(opcode_str[-2:])
    nexpected_chars = 2 + opcode_nparams[code] - 1
    diff = nexpected_chars - len(opcode_str)
    padded_opcode_str = "0" * diff + opcode_str
    modes = map(int, padded_opcode_str[:-2][::-1])
    return (code, modes)

def get_data(memory, mode, addr):
    if mode == 0: # position
        return memory[memory[addr]]
    elif mode == 1: # immediate
        return memory[addr]
    else: # unknown
        assert(False)

def compute(state):
    memory, pc, inputs, output = state
    halted = False
    while True:
        jumping = False
        opcode, modes = parse_opcode(memory[pc])
        if opcode == 99:
            halted = True
            break
        elif opcode == 1:
            data1 = get_data(memory, modes[0], pc + 1)
            data2 = get_data(memory, modes[1], pc + 2)
            target_idx = memory[pc+3]
            memory[target_idx] = data1 + data2
        elif opcode == 2:
            data1 = get_data(memory, modes[0], pc + 1)
            data2 = get_data(memory, modes[1], pc + 2)
            target_idx = memory[pc+3]
            memory[target_idx] = data1 * data2
        elif opcode == 3:
            if not inputs: # must yield until inputs available
                break
            target_idx = memory[pc+1]
            memory[target_idx] = inputs[0]
            inputs = inputs[1:]
        elif opcode == 4:
            data1 = get_data(memory, modes[0], pc + 1)
            output = data1
        elif opcode == 5:
            data1 = get_data(memory, modes[0], pc + 1)
            jump_idx = get_data(memory, modes[1], pc + 2)
            if data1 != 0:
                jumping = True
                pc = jump_idx
        elif opcode == 6:
            data1 = get_data(memory, modes[0], pc + 1)
            jump_idx = get_data(memory, modes[1], pc + 2)
            if data1 == 0:
                jumping = True
                pc = jump_idx
        elif opcode == 7:
            data1 = get_data(memory, modes[0], pc + 1)
            data2 = get_data(memory, modes[1], pc + 2)
            target_idx = memory[pc+3]
            if data1 < data2:
                memory[target_idx] = 1
            else:
                memory[target_idx] = 0
        elif opcode == 8:
            data1 = get_data(memory, modes[0], pc + 1)
            data2 = get_data(memory, modes[1], pc + 2)
            target_idx = memory[pc+3]
            if data1 == data2:
                memory[target_idx] = 1
            else:
                memory[target_idx] = 0
        if not jumping:
            pc += opcode_nparams[opcode]
    return (memory, pc, output), halted

def part1(code):
    phase_settings = itertools.permutations(range(5))
    max_output = -1
    for phase_setting in phase_settings:
        (memA, pcA, outputA), ahalted = compute((code[:], 0, [phase_setting[0], 0], 0))
        (memB, pcB, outputB), bhalted = compute((code[:], 0, [phase_setting[1], outputA], 0))
        (memC, pcC, outputC), chalted = compute((code[:], 0, [phase_setting[2], outputB], 0))
        (memD, pcD, outputD), dhalted = compute((code[:], 0, [phase_setting[3], outputC], 0))
        (memE, pcE, outputE), ehalted = compute((code[:], 0, [phase_setting[4], outputD], 0))
        max_output = max(max_output, outputE)
    print(max_output)

def part2(code):
    phase_settings = itertools.permutations(range(5,10))
    max_output = -1

    for phase_setting in phase_settings:
        # print(phase_setting)
        (memA, pcA, outputA), ahalted = compute((code[:], 0, [phase_setting[0]], 0))
        (memB, pcB, outputB), bhalted = compute((code[:], 0, [phase_setting[1]], 0))
        (memC, pcC, outputC), chalted = compute((code[:], 0, [phase_setting[2]], 0))
        (memD, pcD, outputD), dhalted = compute((code[:], 0, [phase_setting[3]], 0))
        (memE, pcE, outputE), ehalted = compute((code[:], 0, [phase_setting[4]], 0))

        # Feed initial 0 into A
        # (memA, pcA, outputA), ahalted = compute((memA, pcA, [0], 0))
        # print(outputA, outputB, outputC, outputD, outputE)

        while not all([ahalted, bhalted, chalted, dhalted, ehalted]):
            # print(pcA, pcB, pcC, pcD, pcE)
            (memA, pcA, outputA), ahalted = compute((memA, pcA, [outputE], outputA))
            (memB, pcB, outputB), bhalted = compute((memB, pcB, [outputA], outputB))
            (memC, pcC, outputC), chalted = compute((memC, pcC, [outputB], outputC))
            (memD, pcD, outputD), dhalted = compute((memD, pcD, [outputC], outputD))
            (memE, pcE, outputE), ehalted = compute((memE, pcE, [outputD], outputE))
            # print(outputA, outputB, outputC, outputD, outputE)

        if outputE > max_output:
            max_output = outputE
            # print(phase_setting)

    print(max_output)

with open("day7_input.txt") as f:
    chars = f.read()
code = map(int, chars.split(','))

part1(code)
part2(code)
