import fileinput

def part1(pairs):
    total = 0
    for p in pairs:
        p0, p1 = p
        # check if p0 fully contains p1
        if p0[0] <= p1[0] and p0[1] >= p1[1]:
            total += 1
            continue
        # check if p1 fully contains p0
        if p1[0] <= p0[0] and p1[1] >= p0[1]:
            total += 1
            continue
    return total

def part2(pairs):
    total = 0
    for p in pairs:
        p0, p1 = p
        # normalize so low of p0 <= p1
        if p0[0] > p1[0]:
            p0, p1 = p1, p0
        # overlap if high of p0 >= low of p1
        if p0[1] >= p1[0]:
            total += 1
    return total

pairs = [l.rstrip() for l in list(fileinput.input())]
pairs = [p.split(',') for p in pairs]
# print(pairs)
for i in range(len(pairs)):
    lo0, hi0 = map(int, pairs[i][0].split('-'))
    lo1, hi1 = map(int, pairs[i][1].split('-'))
    pairs[i] = [(lo0, hi0), (lo1, hi1)]
# print(pairs)

print(part1(pairs))
print(part2(pairs))
