import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        op,num = l.split(' ')
        num = int(num)
        vals.append((op,num))
    return vals

def part1(program):
    acc = 0
    pc = 0
    pc_hit = set()
    for _ in range(100000):
        if pc in pc_hit:
            return acc
        pc_hit.add(pc)
        op,n = program[pc]
        if op == 'acc':
            acc += n
            pc += 1
        elif op == 'jmp':
            pc += n
        else:
            pc += 1
    return None # should get here

def run_program(program):
    acc = 0
    pc = 0
    pc_hit = set()
    for _ in range(100000):
        # infinite loop
        if pc in pc_hit:
            return None

        # program termintes
        if pc >= len(program): # program terminated
            return acc

        pc_hit.add(pc)
        op,n = program[pc]
        if op == 'acc':
            acc += n
            pc += 1
        elif op == 'jmp':
            pc += n
        else:
            pc += 1
    return None


def part2(program):
    val = run_program(program)
    if val:
        return val

    for i in range(len(program)):
        op,n = program[i]
        alt_program = list(program)
        if op == 'jmp':
            alt_program[i] = ('nop',n)
        elif op == 'nop':
            alt_program[i] = ('jmp',n)
        val = run_program(alt_program)
        if val:
            return val
    return None # Should not get here

vals = parse()
# print(vals)
# print(len(vals))
print(part1(vals))
print(part2(vals))
