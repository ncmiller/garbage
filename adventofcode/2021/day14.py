import fileinput
from collections import Counter

def part1(polymer, rules):
    nsteps = 10
    for step in range(nsteps):
        new_polymer = []
        for i in range(len(polymer) - 1):
            pair = ''.join(polymer[i:i+2])
            if pair in rules:
                new_polymer += [pair[0], rules[pair]]
        new_polymer.append(polymer[-1])
        polymer = new_polymer

    counts = sorted(Counter(polymer).items(), key=lambda item: item[1])
    print(counts[-1][1] - counts[0][1])

# part 2
# [], NNCB * 40
# [NCNBCHB], CBH * 39 (f(n-1) - 1)
# [NBCCNBBBCBHCB], BCBBBC * 38 (6)
# [NBBBCNCCNBBNBNBBCHBHHBCHB], BBNCBNNBHHBH * 37 (12)
#
# 4
# 4 + 3,  total letters = 2 * f(n-1) - 1
# 7 + 6
# 13 + 12
# 25 + 24
#
#           NN
#      NC            CN
#   NB     BC     CC     CN
# NB  BB  BB BC  CN NC  CC CN
#
#          NN
#          NCN
#         NBCCN
#       NBBBCNCCN
#   NBBNBNBBCCNBCNCCN
#                                                      B  C  N  H
# N               N               C               B    1  1  2  0   4
# N       C       N       B       C       H       B    2  2  2  1   7
# N   B   C   C   N   B   B   B   C   B   H   C   B    6  4  2  1   13
# N B B B C N C C N B B N B N B B C H B H H B C H B    11 5  5  4   25
# NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB    23 10 11 5   49
#
# NN
# NC          CN
# NB    BC    CC    CN
# NB BB BB BC CN NC CC CN

# Can't count that high, not enough CPU or RAM
# Need a closed form solution, or O(#rules)

# NN
# NC
# NB
# NB (loop)

# NC
# NB
# NB (loop)

# CN
# CC
# CN
# CC (loop)

# total = 3298534883329
# B       2192039569602

# How many B's produced this iteration?
#     total number of (CH + HC + NC + NB + BN + BC)
# Track total of each pair, use to update
#     increment CB/BH, HB/BC, NB/BC, NB/BB, BB/BN, BB/BC

def part2(polymer, rules):
    counts = {}
    for k,v in rules.items():
        counts[k] = 0

    for i in range(len(polymer)-1):
        counts[''.join(polymer[i:i+2])] += 1
    # print(counts)

    nsteps = 40
    for step in range(nsteps):
        # print('step', step)
        new_counts = counts.copy()
        for k,v in rules.items():
            new_a = k[0] + v
            new_b = v + k[1]
            matches = counts[k]
            new_counts[k] -= matches
            # print(k, matches, new_a, new_b)
            new_counts[new_a] += matches
            new_counts[new_b] += matches
        counts = new_counts
    # print(counts)

    letter_counts = Counter()
    for k,v in counts.items():
        letter_counts[k[0]] += v
        letter_counts[k[1]] += v

    # Avoid double-counting...this is not very precise, and gave
    # a WA (off by one) in the puzzle input (but not the sample)
    for k,v in letter_counts.items():
        letter_counts[k] = round(letter_counts[k] / 2.0)

    s_counts = sorted(letter_counts.items(), key=lambda item: item[1])
    print(s_counts[-1][1] - s_counts[0][1])


lines = list(fileinput.input())
polymer = list(lines[0].rstrip())
rules_list = [line.rstrip().split(' -> ') for line in lines[2:]]
rules = {}
for k,v in rules_list:
    rules[k] = v
# print(polymer)
# print(rules)

part1(polymer[:], rules)
part2(polymer[:], rules)

# part2
#    WA: 2265039461738 (too high, off by one, CA is 2265039461737)
