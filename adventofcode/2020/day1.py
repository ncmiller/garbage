import fileinput

def part1(vals, total):
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            if vals[i] + vals[j] == total:
                # print('vals[{}]:{}, vals[{}]:{} = {}'.format(i, vals[i], j, vals[j], total))
                return vals[i]*vals[j]
    return -1

def part2(vals):
    for i in range(len(vals)):
        res = part1(vals[i:], (2020 - vals[i]))
        if res != -1:
            # print(i, vals[i], res)
            return res * vals[i]

vals = list(map(int, fileinput.input()))
print(part1(vals, 2020))
print(part2(vals))
