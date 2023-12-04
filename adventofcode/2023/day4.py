import fileinput
from collections import defaultdict

def num_wins(card_line):
    winning, ours = card_line.split(': ')[1].split(' | ')
    winning = set([int(w) for w in winning.split(' ') if w != ''])
    ours = set([int(o) for o in ours.split(' ') if o != ''])
    return len(winning.intersection(ours))

def part1(lines):
    total = 0
    for l in lines:
        wins = num_wins(l)
        if wins > 0:
            total += 2 ** (wins - 1)
    return total

def part2(lines):
    card_instances = defaultdict(int)
    for i, l in enumerate(lines):
        card_instances[i] += 1
        for j in range(i + 1, i + 1 + num_wins(l)):
            card_instances[j] += card_instances[i]
    return sum(card_instances.values())

lines = [line[:-1] for line in fileinput.input()]
print(part1(lines))
print(part2(lines))
