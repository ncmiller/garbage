import fileinput

def part1(vals):
    gamma = ''
    eps = ''
    for c in range(len(vals[0]) - 1):
        n0 = 0
        n1 = 0
        for r in range(len(vals)):
            if vals[r][c] == '0':
                n0 += 1
            else:
                n1 += 1
        if n0 > n1:
            gamma += '0'
            eps += '1'
        else:
            gamma += '1'
            eps += '0'
    # print(gamma, eps)
    gammaval = int(gamma, 2)
    epsval = int(eps, 2)
    # print(gammaval, epsval)
    return (gammaval * epsval)

def part2(vals):
    valscopy = list(vals)
    oxy = 0
    for c in range(len(vals[0]) - 1):
        n0 = 0
        n1 = 0
        for r in range(len(vals)):
            if vals[r][c] == '0':
                n0 += 1
            else:
                n1 += 1
        if n1 >= n0:
            vals = [v for v in vals if v[c] == '1']
        else:
            vals = [v for v in vals if v[c] == '0']
        if len(vals) == 1:
            oxy = int(vals[0], 2)
            break
    # print(oxy)

    scrub = 0
    for c in range(len(valscopy[0]) - 1):
        n0 = 0
        n1 = 0
        for r in range(len(valscopy)):
            if valscopy[r][c] == '0':
                n0 += 1
            else:
                n1 += 1
        if n1 >= n0:
            valscopy = [v for v in valscopy if v[c] == '0']
        else:
            valscopy = [v for v in valscopy if v[c] == '1']
        if len(valscopy) == 1:
            scrub = int(valscopy[0], 2)
            break
    # print(scrub)
    return (oxy * scrub)


vals = list(fileinput.input())
print(part1(vals))
print(part2(vals))
