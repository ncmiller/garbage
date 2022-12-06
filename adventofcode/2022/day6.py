import fileinput

def start(buffer, num_unique):
    for i in range(num_unique, len(buffer)):
        if len(set(buffer[i-num_unique:i])) == num_unique:
            return i

def part1(buffer):
    return start(buffer, 4)

def part2(buffer):
    return start(buffer, 14)

buffer = list(fileinput.input())[0].rstrip()
print(part1(buffer))
print(part2(buffer))
