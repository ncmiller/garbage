import fileinput
import string
#----------------------
# File IO
#----------------------
# for line in fileinput.input():

# with open("day9_input.txt") as f:
#     chars = f.read()

# vals = map(int, fileinput.input())

# weight = int(fields[1].replace('(','').replace(')',''))
# stowers = [x.split(',')[0] for x in fields[2:]]
#----------------------

with open("day5_input.txt") as f:
# with open("day5_sample.txt") as f:
    chars = f.read()

chars = chars[:-1] # remove newline

def opposite(a, b):
    oa = ord(a)
    ob = ord(b)
    if oa < ob:
        oa, ob = ob, oa
    return (oa - ob == 32)

def remove_polymer(s, type):
    i = 0
    new_string = s
    oc = ord(type)
    oC = oc - 32
    while i < len(new_string):
        os = ord(new_string[i])
        if os == oc or os == oC:
            del new_string[i]
            i -= 1
        i += 1
    return new_string

def chain_react(s):
    react = list(s)
    while True:
        i = 0
        react_len = len(react)
        while i < len(react):
            if i != 0 and opposite(react[i], react[i-1]):
                # print react[i], react[i-1]
                del react[i]
                del react[i-1]
                i -= 2
            i += 1
        if react_len == len(react):
            break
    return len(react)


def part1():
    print chain_react(chars)

def part2():
    min_len = 10000000
    for c in string.ascii_lowercase:
        react = list(chars)
        react = remove_polymer(react, c)
        min_len = min(min_len, chain_react(react))
    print min_len

part1()
part2()
