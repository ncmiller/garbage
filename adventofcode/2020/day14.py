import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append(l)
    return vals

def apply_mask(mask, val):
    newval = 0
    lenm = len(mask)
    for i in range(lenm):
        bitpos = lenm - i - 1
        valbit = (1 << bitpos) & val
        if mask[i] == '0':
            pass
        elif mask[i] == '1':
            newval += (1 << bitpos)
        else:
            newval += valbit
    # print(val, mask, newval)
    return newval

def part1(lines):
    mem = {}
    mask = ''
    for l in lines:
        if l[:3] == 'mas':
            mask = l[7:]
        else:
            words = l.split(' ')
            addr = int(words[0][4:-1])
            val = int(words[2])
            val = apply_mask(mask, val)
            mem[addr] = val
    return sum([v for v in mem.values()])

def expand_addr(addr, val, num_x):
    eaddr = ''
    lena = len(addr)
    for i in range(lena):
        if addr[i] == 'X':
            valbit = (1 << num_x-1) & val
            if valbit:
                eaddr += '1'
            else:
                eaddr += '0'
            num_x -= 1
        else:
            eaddr += addr[i]
    return int(eaddr,2)

def get_addrs(addr, mask):
    addrs = []
    lenm = len(mask)
    dest_addr = ''
    for i in range(lenm):
        bitpos = lenm - i - 1
        if mask[i] == '0':
            addrbit = (1 << bitpos) & addr
            if addrbit:
                dest_addr += '1'
            else:
                dest_addr += '0'
        elif mask[i] == '1':
            dest_addr += '1'
        else:
            dest_addr += 'X'
    num_x = sum([1 for c in dest_addr if c == 'X'])
    for i in range(2**num_x):
        addrs.append(expand_addr(dest_addr,i, num_x))
    # print(addrs)
    return addrs

def part2(vals):
    mem = {}
    mask = ''
    for l in lines:
        if l[:3] == 'mas':
            mask = l[7:]
        else:
            words = l.split(' ')
            addr = int(words[0][4:-1])
            val = int(words[2])
            addrs = get_addrs(addr, mask)
            for a in addrs:
                mem[a] = val
    return sum([v for v in mem.values()])

# too low: 6960776365110
lines = parse()
print(part1(list(lines)))
print(part2(list(lines)))
