import fileinput

def parse_line(line):
    charmap = { '.': 0, '#': 1, '?': 2 }
    springs, vals = line.split()
    springs = [charmap[c] for s in springs for c in s]
    vals = list(map(int, [v for v in vals.split(',')]))
    return springs, vals

def expand(lines):
    expanded = []
    for l in lines:
        springs, vals = l
        new_springs = springs[:]
        new_vals = vals[:]
        for i in range(4):
            new_springs.append(2)
            new_springs += springs[:]
            new_vals += vals[:]
        expanded.append((new_springs, new_vals))
    return expanded

def process(springs, goal, in_group):
    new_goal = goal[:]
    i = 0
    while i < len(springs):
        c = springs[i]
        if c == 2:
            break
        elif c == 1:
            in_group = True
            if not new_goal or new_goal[0] == 0: # underflow of goal
                # print('underflow')
                return (False, springs, goal, False)
            new_goal[0] -= 1
            pass
        else: # c == 0
            if in_group:
                in_group = False
                if new_goal[0] != 0: # didn't finish this group in goal
                    # print('didn\'t finish')
                    return (False, springs, goal, False)
                new_goal = new_goal[1:]

        i += 1
    return (True, springs[i:], new_goal, in_group)

memo = {}
def arrangements(springs, goal, in_group):
    key = (tuple(springs), tuple(goal), in_group)
    # print(springs, goal, in_group)

    if key in memo:
        return memo[key]

    # Process characters from left until ? encountered,
    # updating springs and goal in the process
    #
    # If processing is valid (consistent with goal), then
    # returns (True, new_springs, new_goal).
    #
    # Otherwise, returns (False, springs, goal).
    is_valid, new_springs, new_goal, new_in_group = process(springs, goal, in_group)
    # print((is_valid, new_springs, new_goal, new_in_group))
    if not is_valid:
        memo[key] = 0
        return 0

    # if new springs and goal empty, then it's a completed arrangement
    if not new_springs and not new_goal:
        # print('valid complete', springs, goal, in_group)
        memo[key] = 1
        return 1

    # if one empty but not the other, then it's an invalid springs
    if not new_goal and new_springs:
        if 1 in new_springs:
            # print('invalid, underflow goal in future')
            memo[key] = 0
            return 0
        else:
            # print('valid, assume rest are 0s')
            memo[key] = 1
            return 1
    elif not new_springs and new_goal:
        # print('invalid, springs empty and goal remaining')
        memo[key] = 0
        return 0

    a0 = arrangements([0] + new_springs[1:], new_goal, new_in_group)
    a1 = arrangements([1] + new_springs[1:], new_goal, new_in_group)
    answer = a0 + a1
    # print('valid recurse', springs, goal, answer, in_group)
    memo[key] = answer
    return answer

def part1(lines):
    total = 0
    for row,goal in lines:
        r = row + [0] # add a . at the end, to normalize handling of last group
        val = arrangements(r, goal, False)
        # print(r, val)
        total += val
    return total

lines = [parse_line(line[:-1]) for line in fileinput.input()]
print(part1(lines))
print(part1(expand(lines)))
