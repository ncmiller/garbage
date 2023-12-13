import fileinput

def parse_line(line):
    charmap = { '.': 0, '#': 1, '?': 2 }
    springs, vals = line.split()
    springs = [charmap[c] for s in springs for c in s]
    vals = list(map(int, [v for v in vals.split(',')]))
    return springs, vals

def matches(springs, vals):
    computed_vals = []
    qs = 0
    for s in springs:
        if s == 1:
            qs += 1
        else:
            if qs != 0:
                computed_vals.append(qs)
                qs = 0
    if qs != 0:
        computed_vals.append(qs)
    # print(springs, computed_vals, vals)
    return computed_vals == vals


def fill(springs, num):
    filled = springs[:]
    numbit = 0
    for i, s in enumerate(springs):
        if s == 2:
            nextbit = ((1 << numbit) & num) >> numbit
            # print('set bit {} to {}'.format(i, nextbit))
            filled[i] = nextbit
            numbit += 1
    return filled

bit_count_memo = dict()
def bit_count(num):
    if num in bit_count_memo:
        return bit_count_memo[num]
    else:
        x = bin(num).count('1')
        bit_count_memo[num] = x
        return x

def part1(lines):
    total_ways = 0
    for il, l in enumerate(lines):
        # print('Progress: ', il / len(lines))
        ways = 0
        springs, vals = l
        vals_num_ones = sum(vals)
        springs_num_ones = sum([1 for s in springs if s == 1])

        qs = sum([1 for s in springs if s == 2])
        for i in range(2**qs):
            if bit_count(i) != (vals_num_ones - springs_num_ones):
                continue
            filled = fill(springs, i)
            # print(filled)
            if matches(filled, vals):
                ways += 1

        # print(l, ways)
        total_ways += ways
    return total_ways

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
        # print(springs, new_springs)
        # print(vals, new_vals)
        expanded.append((new_springs, new_vals))
    return expanded


lines = [parse_line(line[:-1]) for line in fileinput.input()]
# print(lines)
# print(part1(lines))
expanded = expand(lines)
# for e in expanded:
#     print(e)
print(part1(expanded))
