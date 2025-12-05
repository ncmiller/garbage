import fileinput

def is_fresh(ranges, ingredient):
    for r in ranges:
        if ingredient in range(r[0], r[1]+1):
            return True
    return False

def part1(lines):
    ranges = []
    num_fresh = 0
    in_ingredients = False
    for i in range(len(lines)):
        line = lines[i]
        if line == "":
            in_ingredients = True
            continue

        if in_ingredients:
            ingredient = int(line)
            if is_fresh(ranges, ingredient):
                num_fresh += 1
        else:
            ranges.append(list(map(int, line.split("-"))))
    return num_fresh

def part2(lines):
    ranges = []
    for i in range(len(lines)):
        line = lines[i]
        if line == "":
            break
        ranges.append(list(map(int, lines[i].split("-"))))
    ranges = sorted(ranges)

    # for r in ranges:
    #     print(r)

    num_ids = 0
    for i in range(len(ranges)):
        start, end = ranges[i]
        num_ids += (end - start) + 1
        for j in range(i + 1, len(ranges)):
            if ranges[j][0] > end:
                break
            dec = (min(end, ranges[j][1])-ranges[j][0]) + 1
            print(ranges[i], ranges[j], dec)
            num_ids -= dec
    return num_ids

def overlaps(r1, r2):
    return r1[1] >= r2[0]

def part2_alt(lines):
    ranges = []
    for i in range(len(lines)):
        line = lines[i]
        if line == "":
            break
        ranges.append(list(map(int, lines[i].split("-"))))
    ranges = sorted(ranges)

    # for r in ranges:
    #     print(r)

    deduped_ranges = [ranges[0]]
    for i in range(1,len(ranges)):
        found_overlap = False
        for d in deduped_ranges:
            if overlaps(d, ranges[i]):
                d[0] = min(d[0], ranges[i][0])
                d[1] = max(d[1], ranges[i][1])
                found_overlap = True
        if not found_overlap:
            # print('add', ranges[i])
            deduped_ranges.append(ranges[i])
    print(deduped_ranges)

    num_ids = 0
    for d in deduped_ranges:
        num_ids += d[1] - d[0] + 1
    return num_ids


# case 1: 10-20, 11-19 (smaller, overlapping)
# case 2: 10-20, 10-21 (bigger, overlapping)
# case 3: 10-20, 21-30 (non-overlapping)
# case 4: 10-20, 10-20 (duplicate)

lines = list(fileinput.input())
lines = [l[:-1] for l in lines]
print(part1(lines))

# WA (too low): 358189770742039, 368701529292823
# print(part2(lines))

print(part2_alt(lines))
