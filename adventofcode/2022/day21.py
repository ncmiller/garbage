import fileinput
from operator import add, sub, mul, floordiv, eq

def solve(monkey, monkeys):
    value = monkeys[monkey]

    if not isinstance(value, tuple):
        return value

    opmap = {'+':add, '-':sub, '*':mul, '/':floordiv, '==':eq}
    ans = opmap[value[1]](solve(value[0], monkeys), solve(value[2], monkeys))
    return ans

lines = [line.rstrip().split(' ') for line in fileinput.input()]
monkeys = {}
for line in lines:
    if len(line) == 4:
        monkeys[line[0][:-1]] = tuple(line[1:])
    else:
        monkeys[line[0][:-1]] = int(line[1])

#                      root(==)
#          pppw(/)                sjmn(*)
#      cczh(+) lfqf(4)       drzm(-)        dbpl(5)
# sllz(4)   lgvd(*)     hmdt(32) zczc(2)
#        ljgn(2) ptdq(-)
#             humn(?) dvpt(3)

# (4 + (2 * (X - 3))) / 4 == (32 - 2) * 5

def get_humn_path(monkeys):
    parent = {}
    for m in monkeys:
        value = monkeys[m]
        if isinstance(value, tuple):
            parent[value[0]] = m
            parent[value[2]] = m
    humn_path = []
    node = 'humn'
    while node:
        humn_path.append(node)
        node = parent[node] if node in parent else None
    return humn_path

def find_humn(monkeys):
    humn_path = get_humn_path(monkeys)
    left = monkeys['root'][0]
    right = monkeys['root'][2]
    humn_side = left if left in humn_path else right
    non_humn_side = left if humn_side is right else right
    target_value = solve(non_humn_side, monkeys)

    # collect partial operations on humn path
    # e.g. [(/,4),(+,4),(*,2),(-,3)]
    partial_ops = []
    for monkey in reversed(humn_path[1:-1]):
        value = monkeys[monkey]
        if value[0] not in humn_path:
            left_val = solve(value[0], monkeys)
            partial_ops.append((value[1], left_val, True))
        if value[2] not in humn_path:
            right_val = solve(value[2], monkeys)
            partial_ops.append((value[1], right_val, False))

    # Apply inverse operations to target value to find X
    # e.g. ((((150 * 4) - 4) // 2) + 3) = 301
    # Note: + and * are commutative, * and // are not
    X = target_value
    for op, val, is_left in partial_ops:
        if op == '+':
            X = X - val
        elif op == '*':
            X = X // val
        elif op == '-':
            if is_left:
                X = val - X
            else:
                X = X + val
        elif op == '/':
            if is_left:
                X = val // X
            else:
                X = X * val
    return X

# part 1
print(solve('root', monkeys))

# part 2
monkeys['root'] = (monkeys['root'][0], '==', monkeys['root'][2])
humn_val = find_humn(monkeys)
print(humn_val)

# check work
monkeys['humn'] = humn_val
assert(solve('root',monkeys))
