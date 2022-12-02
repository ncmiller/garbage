import fileinput

def part1(elves):
    return max([sum(e) for e in elves])

def part2(elves):
    return sum(list(reversed(sorted([sum(e) for e in elves])))[:3])


lines = list(fileinput.input())
elves = []
calories = []
for line in lines:
    if line == '\n':
        elves.append(calories)
        calories = []
    else:
        calories.append(int(line.rstrip()))
elves.append(calories)

print(part1(elves))
print(part2(elves))
