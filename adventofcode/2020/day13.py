import fileinput
from collections import Counter

def valid_busses(busses):
    return [int(b) for b in busses if b != 'x']

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append(l)
    depart = int(vals[0])
    busses = vals[1].split(',')
    return depart,busses

def part1(depart, busses):
    busses = valid_busses(busses)
    min_diff = 999999
    min_bus_id = -1
    for b in busses:
        next_depart = int(depart/b)*b
        if next_depart < depart:
            next_depart += b
        diff = next_depart - depart
        # print(b,next_depart,diff)
        if diff < min_diff:
            min_diff = diff
            min_bus_id = b
    return min_bus_id * min_diff

def is_valid_bus_configuration(busses, t):
    if t == 0: return False
    for i in range(len(busses)):
        b = busses[i]
        if b != 'x':
            b = int(b)
            if (b - (t % b)) % b != i:
                return False
    return True

def find_t_offset(tstart, tinc, b):
    i1,bid1 = b
    t = tstart
    while(True):
        if (t + i1) % bid1 == 0:
            return t
        t += tinc
    return -1

def sorted_busses(busses):
    vals = []
    for i in range(len(busses)):
        if busses[i] != 'x':
            vals.append((i,int(busses[i])))
    vals_sorted = sorted(vals, key=lambda x: x[1])
    return list(reversed(vals_sorted))

def part2(busses):
    first_bus = int(busses[0])

    sb = sorted_busses(busses)
    # print(sb)

    inc = first_bus
    toffset = 0

    for b in sb:
        if b[0] == 0:
            continue
        toffset = find_t_offset(toffset, inc, b)
        inc *= b[1]
        # print (toffset, inc)

    return toffset

depart,busses = parse()
print(part1(depart, list(busses)))

# depart,busses = 939,[7,13,'x','x',59,'x',31,19]
# depart,busses = 939,[17,'x',13,19]
# depart,busses = 939,[1789,37,47,1889]
# depart,busses = 939,[67,7,'x',59,61]
# depart,busses = 939,[67,'x',7,59,61]
print(part2(list(busses)))
