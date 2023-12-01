import fileinput

spelled_numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

# If found, returns numeric value, otherwise -1
def prefix_is_spelled_number(s):
    for i in range(len(spelled_numbers)):
        sn = spelled_numbers[i]
        if s[:len(sn)] == sn:
            return int(i)
    return -1

def find_number(line, from_start=True):
    r = range(len(line))
    if not from_start:
        r = reversed(r)

    for i in r:
        if line[i].isnumeric():
            return line[i]

        spelled_number = prefix_is_spelled_number(line[i:])
        if spelled_number != -1:
            return str(spelled_number)

    return ''

def part2(lines):
    sum = 0

    for line in lines:
        first_num = find_number(line, True)
        last_num = find_number(line, False)

        # print(first_num + last_num)
        sum += int(first_num + last_num)
    return sum

def part1(lines):
    sum = 0
    for line in lines:
        numbers = [c for c in line if c.isnumeric()]
        numbers = int(numbers[0] + numbers[-1])
        # print(numbers)
        sum += numbers
    return sum

lines = list(fileinput.input())
print(part1(lines))
print(part2(lines))
