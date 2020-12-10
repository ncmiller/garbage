import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append(int(l))
    return vals

def part1(vals):
    # add 0 and max + 3 to adapter list
    vals += [0, max(vals) + 3]
    vals = sorted(vals)
    # print(vals)
    diff1 = 0
    diff3 = 0
    for i in range(1, len(vals)):
        diff = vals[i] - vals[i-1]
        if diff == 1:
            diff1 += 1
        if diff == 3:
            diff3 += 1
    return diff1 * diff3

def removable_indices(adapters):
    removable = []
    for i in range(1, len(adapters) - 1):
        p,c,n = adapters[i-1:i+2]
        diff = n - p
        if diff <= 3:
            removable.append(i)
    return removable

def fact(x):
    val = 1
    for i in range(2,x+1):
        val *= i
    return val

def choose(n, k):
    return int(fact(n) / (fact(k) * fact(n - k)))

def triples(a):
    t = []
    for i in range(0, len(a)-2):
        if ((a[i+2] - a[i+1] == 1) and (a[i+1] - a[i] == 1)):
            t.append((a[i],a[i+1],a[i+2]))
    return t

def valid_combos(lenr, nt):
    n = 2**lenr
    if nt == 0:
        return n
    for i in range(1,int(lenr/3)+1):
        cs = choose(nt,i)
        n -= (cs * valid_combos(lenr-(i*3), nt-i))
    return n

def part2(vals):
    vals += [0, max(vals) + 3]
    vals = sorted(vals)
    r = removable_indices(vals)
    # print(vals)
    # print(r)
    t = triples(r)
    n = valid_combos(len(r), len(t))
    return n

vals = parse()
print(part1(list(vals)))
print(part2(list(vals)))
