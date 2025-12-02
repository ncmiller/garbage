import fileinput

def part1(ranges):
    sum_invalid_ids = 0
    for r in ranges:
        first, last = int(r[0]), int(r[1])
        for x in range(int(first), int(last)+1):
            s = str(x)
            l = len(s)
            if l % 2 == 1:
                continue
            # print(s, l)
            if s[:l//2] == s[l//2:]:
                sum_invalid_ids += x
    return sum_invalid_ids

def all_equal(string_list):
    assert(len(string_list) >= 2)
    return len(set(string_list)) == 1

def part2(ranges):
    sum_invalid_ids = 0
    for r in ranges:
        first, last = int(r[0]), int(r[1])
        for x in range(int(first), int(last)+1):
            s = str(x)
            l = len(s)
            # if l % 2 == 1:
            #     continue
            # print(s, l)
            for i in range(1,l//2+1):
                split_strings = [s[j:j+i] for j in range(0,l,i)]
                if all_equal(split_strings):
                    sum_invalid_ids += x
                    # print(s, i, split_strings)
                    break
    return sum_invalid_ids

lines = list(fileinput.input())
ranges = [r.split('-') for r in lines[0][:-1].split(',')]
# print(ranges)
print(part1(ranges))
print(part2(ranges))
