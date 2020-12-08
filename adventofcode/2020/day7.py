import fileinput
from collections import Counter

# Remove newlines, periods
# Split on ','
# Parse phrases
def parse():
    bags = {}
    for line in fileinput.input():
        l = line.rstrip()
        l = l[:-1] # remove trailing '.'
        phrases = l.split(',')
        # Handle phrase 0 as special case
        words = phrases[0].split(' ')
        bag_color = ' '.join(words[:2])
        contains = []
        if words[4] != 'no':
            n = int(words[4])
            contain_color = ' '.join(words[5:7])
            contains.append((n, contain_color))
        for p in phrases[1:]:
            p = p[1:] # remove leading ' '
            words = p.split(' ')
            n = int(words[0])
            c = ' '.join(words[1:3])
            contains.append((n, c))
        bags[bag_color] = contains
    return bags

# hash map, keyed on outer bag color
#   value is [((n, color))]

def print_bags(bags):
    for b,c in bags.items():
        print(b,c)

def bag_has_gold(color, bags):
    contains = bags[color]
    for n,color in contains:
        if color == 'shiny gold':
            return True
        elif bag_has_gold(color, bags):
            return True
    return False

def part1(bags):
    count = 0
    for color,contains in bags.items():
        if bag_has_gold(color, bags):
            count += 1
    return count

def num_bags(color, bags):
    count = 0
    contains = bags[color]
    for n,color in contains:
        count += (n + n * num_bags(color, bags))
    return count

def part2(bags):
    return num_bags('shiny gold', bags)

vals = parse()
print_bags(vals)
# print(len(vals))
print(part1(vals))
print(part2(vals))

