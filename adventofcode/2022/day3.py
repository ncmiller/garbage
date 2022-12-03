import fileinput

def part1(sacks):
    div_sacks = [[s[:len(s)//2], s[len(s)//2:]] for s in sacks]
    total = 0
    for s in div_sacks:
        s0, s1 = s
        for c0 in s0:
            found = False
            for c1 in s1:
                if c0 == c1:
                    if c0.isupper():
                        total += ord(c0) - ord('A') + 27
                    else:
                        total += ord(c0) - ord('a') + 1
                    found = True
                    break
            if found:
                break
    return total

def part2(sacks):
    groups = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    total = 0
    for g in groups:
        s0, s1, s2 = g
        found = False
        for c0 in s0:
            for c1 in s1:
                for c2 in s2:
                    if c0 == c1 and c1 == c2:
                        if c0.isupper():
                            total += ord(c0) - ord('A') + 27
                        else:
                            total += ord(c0) - ord('a') + 1
                        found = True
                        break
                if found:
                    break
            if found:
                break
    return total

sacks = [l.rstrip() for l in list(fileinput.input())]
print(part1(sacks[:]))
print(part2(sacks[:]))
