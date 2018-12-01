import fileinput

def orig():
    lines = []
    for line in fileinput.input():
        lines.append((line[0], int(line[1:])))
    sum = 0
    seen = {}
    i = 0
    while True:
        sign,val = lines[i]
        if sign == '+':
            sum += val
        else:
            sum -= val
        if sum in seen:
            print sum
            break
        else:
            seen[sum] = 1
        i = (i + 1) % len(lines)

#---

def after():
    vals = map(int, fileinput.input())
    print sum(vals)

    seen = {}
    i = 0
    s = 0
    while True:
        s += vals[i]
        if s in seen:
            print s
            break
        seen[s] = 1
        i = (i + 1) % len(vals)

#orig()
after()
