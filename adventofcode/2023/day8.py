import fileinput
from functools import reduce

def part1(turns, nodes):
    current = 'AAA'
    steps = 0
    i = 0
    while True:
        current = nodes[current][turns[i]]
        steps += 1
        i = (i + 1) % len(turns)
        if current == 'ZZZ':
            break
    return steps

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b / gcd(a,b)

def lcm_list(nums):
    return int(reduce(lcm, nums, 1))

def part2(turns, nodes):
    starts = [k for k,v in nodes.items() if k[-1] == 'A']

    periods = []
    for s in starts:
        step = 0
        current = s
        t = 0
        ends_in_z = [] # steps when node ending in Z found

        while True:
            current = nodes[current][turns[t]]
            step += 1
            t = (t + 1) % len(turns)
            if current[-1] == 'Z':
                ends_in_z.append(step)
            if len(ends_in_z) >= 3:
                break

        periods.append(ends_in_z[2] - ends_in_z[1])

    return lcm_list(periods)

lines = [l[:-1] for l in fileinput.input()]
turns = lines[0]
turns = [0 if t == 'L' else 1 for t in turns]
nodes = [l.replace('=','').replace('(','').replace(',','').replace(')','').split() for l in lines[2:]]
nodes = dict([(x[0], (x[1], x[2])) for x in nodes])
print(part1(turns, nodes))
print(part2(turns, nodes))
