import fileinput
from functools import cmp_to_key

# returns -1: left is definitely before right (in order)
#          1: left is definitely after right (not in order)
#          0: not sure what the order should be
def cmp_order(left, right):
    for i in range(max(len(left), len(right))):
        if i >= len(left):
            # print('null', right[i])
            return -1
        if i >= len(right):
            # print(left[i], 'null')
            return 1

        l = left[i]
        r = right[i]

        l_is_list = isinstance(l, list)
        r_is_list = isinstance(r, list)

        # print(l, r)
        if not l_is_list and not r_is_list:
            if l < r:
                return -1
            elif l > r:
                return 1
        elif l_is_list and not r_is_list:
            sub_inorder = cmp_order(l, [r])
            if sub_inorder != 0:
                return sub_inorder
        elif not l_is_list and r_is_list:
            sub_inorder = cmp_order([l], r)
            if sub_inorder != 0:
                return sub_inorder
        else: # both lists
            sub_inorder = cmp_order(l, r)
            if sub_inorder != 0:
                return sub_inorder

    return 0

def part1(pairs):
    total = 0
    for i in range(len(pairs)):
        left, right = pairs[i]
        if cmp_order(left, right) == -1:
            total += (i + 1)
    return total

def part2(pairs):
    answer = 1
    packets = [[[2]], [[6]]]
    for a,b in pairs:
        packets.append(a)
        packets.append(b)
    sorted_packets = sorted(packets, key=cmp_to_key(cmp_order))
    for i in range(len(sorted_packets)):
        p = sorted_packets[i]
        if p == [[2]] or p == [[6]]:
            answer *= (i + 1)
    return answer

lines = [line.rstrip() for line in fileinput.input()]
pairs = []
for i in range(len(lines)):
    if not lines[i]:
        pairs.append([eval(lines[i-2]), eval(lines[i-1])])
pairs.append([eval(lines[-2]), eval(lines[-1])])

print(part1(pairs))
print(part2(pairs))
