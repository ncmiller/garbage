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

def get_data(memory, mode, idx):
    if mode == 0: # position
        return memory[memory[idx]]
    elif mode == 1: # immediate
        return memory[idx]
    else: # unknown
        assert(False)

def compute(memory, input_val):
    idx = 0

    while True:
        jumping = False
        # print(memory)
        # print(idx)
        opcode, modes = parse_opcode(memory[idx])
        # print(opcode, modes)
        if opcode == 99:
            break
        elif opcode == 1:
            data1 = get_data(memory, modes[0], idx + 1)
            data2 = get_data(memory, modes[1], idx + 2)
            target_idx = memory[idx+3]
            memory[target_idx] = data1 + data2
        elif opcode == 2:
            data1 = get_data(memory, modes[0], idx + 1)
            data2 = get_data(memory, modes[1], idx + 2)
            target_idx = memory[idx+3]
            memory[target_idx] = data1 * data2
        elif opcode == 3:
            target_idx = memory[idx+1]
            memory[target_idx] = input_val
        elif opcode == 4:
            data1 = get_data(memory, modes[0], idx + 1)
            print("output = {}".format(data1))
        elif opcode == 5:
            data1 = get_data(memory, modes[0], idx + 1)
            jump_idx = get_data(memory, modes[1], idx + 2)
            if data1 != 0:
                jumping = True
                idx = jump_idx
        elif opcode == 6:
            data1 = get_data(memory, modes[0], idx + 1)
            jump_idx = get_data(memory, modes[1], idx + 2)
            if data1 == 0:
                jumping = True
                idx = jump_idx
        elif opcode == 7:
            data1 = get_data(memory, modes[0], idx + 1)
            data2 = get_data(memory, modes[1], idx + 2)
            target_idx = memory[idx+3]
            if data1 < data2:
                memory[target_idx] = 1
            else:
                memory[target_idx] = 0
        elif opcode == 8:
            data1 = get_data(memory, modes[0], idx + 1)
            data2 = get_data(memory, modes[1], idx + 2)
            target_idx = memory[idx+3]
            if data1 == data2:
                memory[target_idx] = 1
            else:
                memory[target_idx] = 0
        if not jumping:
            idx += opcode_nparams[opcode]
    return memory

with open("day5_input.txt") as f:
    chars = f.read()
code = map(int, chars.split(','))

memory = code[:]
input_val = 5
compute(memory, input_val)
