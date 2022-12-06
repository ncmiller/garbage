import fileinput
import copy

def parse_input():
    lines = [l for l in list(fileinput.input())]

    num_stacks = len(lines[0]) // 4

    stacks = [[] for _ in range(num_stacks)]
    moves = []
    parsing_stacks = True

    for line in lines:
        if line == '\n':
            continue
        if line[1] == '1':
            parsing_stacks = False
            continue

        if parsing_stacks:
            for stack_index in range(num_stacks):
                if line[stack_index*4] == '[':
                    # index 0 is bottom of stack
                    stacks[stack_index].insert(0, line[stack_index*4+1])
        else: # parsing moves
            words = line.rstrip().split(' ')
            moves.append([int(words[1]), int(words[3]), int(words[5])])

    return stacks, moves

def part1(stacks, moves):
    for move in moves:
        num, src, dst = move
        src -= 1
        dst -= 1
        for i in range(num):
            stacks[dst].append(stacks[src].pop())
    return ''.join([s[-1] for s in stacks])

def part2(stacks, moves):
    for move in moves:
        num, src, dst = move
        src -= 1
        dst -= 1
        stacks[dst] += stacks[src][-num:]
        stacks[src] = stacks[src][:-num]
    return ''.join([s[-1] for s in stacks])

stacks, moves = parse_input()
print(part1(copy.deepcopy(stacks), copy.deepcopy(moves)))
print(part2(copy.deepcopy(stacks), copy.deepcopy(moves)))
