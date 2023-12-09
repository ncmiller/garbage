import fileinput

def part1(seqs):
    total = 0
    for s in seqs:
        history = []
        diff = s[:]
        history.append(diff)

        while True:
            diff = [diff[i]-diff[i-1] for i in range(1, len(diff))]
            if all([d==0 for d in diff]):
                break
            history.append(diff)

        val = 0
        for i in reversed(range(0, len(history) - 1)):
            val = history[i][-1] + history[i+1][-1]
            history[i].append(val)
        total += val
    return total

def part2(seqs):
    total = 0
    for s in seqs:
        history = []
        diff = s[:]
        history.append(diff)

        while True:
            diff = [diff[i]-diff[i-1] for i in range(1, len(diff))]
            history.append(diff)
            if all([d==0 for d in diff]):
                break

        val = 0
        for i in reversed(range(0, len(history) - 1)):
            val = history[i][0] - val
        total += val
    return total


lines = [line[:-1] for line in fileinput.input()]
seqs = [list(map(int, l.split())) for l in lines]
print(part1(seqs))
print(part2(seqs))
