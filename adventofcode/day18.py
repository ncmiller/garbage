from collections import defaultdict
import sys

inst = [0, 0]
last_sound = [0, 0]
recovered = [0, 0]
regs = [defaultdict(int), defaultdict(int)]
regs[0]['p'] = 0
regs[1]['p'] = 1
instructions = []
sends = [0, 0]
q = [[], []]
waiting = [0, 0]
all_regs = "abcdefghijklmnopqrstuvwxyz"

def get(s, pid):
    if s in all_regs:
        return regs[pid][s]
    else:
        return int(s)

def set(x, y, pid):
    regs[pid][x] = get(y, pid)
    inst[pid] += 1

def snd(x, y, pid):
    last_sound[pid] = regs[pid][x]
    inst[pid] += 1

def snd2(x, y, pid):
    q[pid ^ 1].append(get(x, pid))
    sends[pid] += 1
    inst[pid] += 1

def rcv2(x, y, pid):
    if len(q[pid]) > 0:
        regs[pid][x] = q[pid].pop(0)
        inst[pid] += 1
        waiting[pid] = 0
    else:
        waiting[pid] = 1
        if waiting[pid^1]:
            print 'deadlock!'
            print sends
            sys.exit(0)

def add(x, y, pid):
    regs[pid][x] += get(y, pid)
    inst[pid] += 1

def mul(x, y, pid):
    regs[pid][x] *= get(y, pid)
    inst[pid] += 1

def mod(x, y, pid):
    regs[pid][x] %= get(y, pid)
    inst[pid] += 1

def rcv(x, y, pid):
    if regs[pid][x] != 0:
        recovered[pid] = last_sound[pid]
    inst[pid] += 1

def jgz(x, y, pid):
    jump = get(x, pid) > 0
    if jump:
        inst[pid] += get(y, pid)
    else:
        inst[pid] += 1

op = {
    'set': set,
    'snd': snd2,
    'add': add,
    'mul': mul,
    'mod': mod,
    'rcv': rcv2,
    'jgz': jgz,
}


import fileinput
for line in fileinput.input():
    instructions.append(line.split())

while 1:
    for pid in [0,1]:
        i = instructions[inst[pid]]
        if len(i) == 2:
            op[i[0]](i[1], 0, pid)
        else:
            op[i[0]](i[1], i[2], pid)
