import fileinput
import copy

def part1(fish, ndays=80):
    for day in range(ndays):
        # new_fish = []
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
        # print(day, len(fish))
    return len(fish)

memo = {}
def part2(fish, ndays=256):
    if ndays in memo:
        return memo[ndays]

    total = 0
    new_fish = []
    for i in range(fish[0], ndays, 7):
        total += 1
        total += part2([8], ndays - i - 1)
    # print(ndays, total)
    memo[ndays] = total
    return total

line = list(fileinput.input())[0]
fish = list(map(int, line.split(',')))
print(part1(copy.deepcopy(fish), 80))

# part2 wrapper
total = len(fish)
for i in range(len(fish)):
    memo = {}
    ans = part2(copy.deepcopy([fish[i]]), 256)
    total += ans
print(total)

