from collections import defaultdict
regsnames = "abcdefgh"
regs = defaultdict(int)

with open('day23_input.txt') as f:
    lines = f.readlines()

inst = []
for line in lines:
    inst.append(line.split())

def get(s):
    if s in regsnames: return regs[s]
    else: return int(s)

i = 0
nummul = 0
while i >= 0 and i < len(inst):
    ins = inst[i]
    if ins[0] == 'set':
        regs[ins[1]] = get(ins[2])
        i += 1
    elif ins[0] == 'sub':
        regs[ins[1]] -= get(ins[2])
        i += 1
    elif ins[0] == 'mul':
        regs[ins[1]] = regs[ins[1]] * get(ins[2])
        nummul += 1
        i += 1
    elif ins[0] == 'jnz':
        cond = get(ins[1])
        if cond != 0: i += get(ins[2])
        else: i += 1
print nummul

# By translating assembly to more readable code,
# discovered the code is counting the number of
# composites in a range of numbers.
with open('primes.txt') as f:
    chars = f.read()
primes = set(map(int, chars.split()))

h = 0
for x in range(109900, 126901, 17):
    if x not in primes:
        h += 1

print h
