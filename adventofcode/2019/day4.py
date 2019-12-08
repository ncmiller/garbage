def has_two_adjacent_digits(x):
    x_str = str(x)
    last_char = x_str[0]
    for i in range(1,len(x_str)):
        c = x_str[i]
        if c == last_char:
            return True
        last_char = c
    return False

def has_strictly_two_adjacent_digits(x):
    x_str = str(x)
    last_char = x_str[0]
    run_length = 1
    for i in range(1,len(x_str)):
        c = x_str[i]
        if c == last_char:
            run_length += 1
        else:
            if run_length == 2:
                return True
            run_length = 1
        last_char = c
    return run_length == 2

def digits_increase(x):
    x_str = str(x)
    last_char = x_str[0]
    for i in range(1,len(x_str)):
        c = x_str[i]
        if c < last_char:
            return False
        last_char = c
    return True

def meets_criteria_part1(x):
    return has_two_adjacent_digits(x) and digits_increase(x)

def meets_criteria_part2(x):
    return has_strictly_two_adjacent_digits(x) and digits_increase(x)

def part1(a, b):
    meets_criteria = []
    for i in range(a, b):
        if meets_criteria_part1(i):
            meets_criteria.append(i)
    return meets_criteria

def part2(a, b):
    meets_criteria = []
    for i in range(a, b):
        if meets_criteria_part2(i):
            meets_criteria.append(i)
    return meets_criteria

# print(meets_criteria_part1(111111))
# print(meets_criteria_part1(223450))
# print(meets_criteria_part1(123789))

a = 372037
b = 905157

part1_vals = part1(a,b)
print(len(part1_vals))

part2_vals = part2(a,b)

# set_diff = set(part1_vals) - set(part2_vals)
# for diff in set_diff:
#     print(diff)

# print(meets_criteria_part2(112233))
# print(meets_criteria_part2(123444))
# print(meets_criteria_part2(111122))
# print(meets_criteria_part2(777899))

# not 235 (too low)
print(len(part2_vals))
