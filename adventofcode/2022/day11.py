import fileinput
import copy
import re
import math

def parse_lines(lines):
    monkies = []
    m = []
    for l in lines:
        if not l:
            monkies.append(m)
            m = []
            continue
        if l[0] == 'M':
            pass
        elif l[0] == 'S':
            items = list(map(int, re.split(r'Starting items: |, ', l)[1:]))
            m.append(items)
        elif l[0] == 'O':
            op = re.split(r'Operation: |new = ', l)[2].split(' ')
            m.append(op)
        elif l[0] == 'T':
            div_by = int(re.split(r'Test: divisible by ', l)[1])
            m.append(div_by)
        elif 'true' in l:
            true_throw = int(re.split(r' ', l)[-1])
            m.append(true_throw)
        elif 'false' in l:
            false_throw = int(re.split(r' ', l)[-1])
            m.append(false_throw)
        else:
            print(l)
            assert(False)
    monkies.append(m)
    return monkies

def apply_op(op, worry):
    a = worry if op[0] == 'old' else int(op[0])
    b = worry if op[2] == 'old' else int(op[2])
    if op[1] == '+': return a + b
    elif op[1] == '*': return a * b
    else: assert(False)

def monkey_business(monkies, div_by_3, nrounds):
    monkey_inspections = [0 for _ in range(len(monkies))]
    modulus = math.prod([m[2] for m in monkies])
    for r in range(nrounds):
        for i in range(len(monkies)):
            m = monkies[i]
            while m[0]:
                item = m[0].pop(0)
                monkey_inspections[i] += 1
                worry = item
                worry = apply_op(m[1], worry)
                if div_by_3:
                    worry = worry // 3
                worry = worry % modulus
                if worry % m[2] == 0:
                    monkies[m[3]][0].append(worry)
                else:
                    monkies[m[4]][0].append(worry)
    return math.prod(list(reversed(sorted(monkey_inspections)))[:2])

lines = [l.rstrip().lstrip() for l in fileinput.input()]
monkies = parse_lines(lines)
# for m in monkies: print(m)
print(monkey_business(copy.deepcopy(monkies), True, 20))
print(monkey_business(copy.deepcopy(monkies), False, 10000))
