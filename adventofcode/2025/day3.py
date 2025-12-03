import fileinput

def part1(lines):
    total_jolts = 0
    for line in lines:
        max_jolts = -1
        line = line[:-1]
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                jolts = line[i] + line[j]
                max_jolts = max(max_jolts, int(jolts))
        # print(line, max_jolts)
        total_jolts += max_jolts
    return total_jolts

def max_jolts(line, n, memo):
    if len(line) == 0:
        return ""
    if n == 0:
        return ""

    if (line, n) in memo:
        return memo[(line,n)]

    jolts_with = line[0] + max_jolts(line[1:], n-1, memo)
    jolts_without = max_jolts(line[1:], n, memo)

    if (jolts_without == ""):
        jolts_without = "0"
    if (jolts_with == ""):
        jolts_with = "0"

    if int(jolts_with) > int(jolts_without):
        memo[(line,n)] = jolts_with
        return jolts_with
    else:
        memo[(line,n)] = jolts_without
        return jolts_without

def part2(lines, n):
    total_jolts = 0
    for line in lines:
        line = line[:-1]
        num_batteries = n
        memo = dict()
        # print(line, max_jolts(line, num_batteries, memo))
        total_jolts += int(max_jolts(line, num_batteries, memo))
        # if line == "811111111111119":
        #     print(memo)
        #     assert(False)
    return total_jolts

lines = list(fileinput.input())
print(part1(lines))

# WA (too low): 172601598658182
print(part2(lines, 12))
# print(part2(lines, 2))
