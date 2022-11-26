import fileinput

# reduce (string)
#   explode
#   split
# add (list)
# magnitude (list)

def add(a, b): # str
    return '[' + a + ',' + b + ']'

def explode(a): # str
    new_a = a[:]
    depth = 0
    for i in range(len(a)):
        if a[i] == '[':
            depth += 1
        if a[i] == ']':
            depth -= 1
        if depth == 5: # this list is nested inside four pairs
            left_i = i
            right_i = -1
            # scan forward until ']'
            for j in range(i+1, len(a)):
                if a[j] == ']':
                    right_i = j
                    break
            assert(right_i != -1)

            # split and convert left/right to int
            left_right_str = a[left_i+1:right_i]
            left, right = tuple(map(int, left_right_str.split(',')))
            # print(left, right)

            # scan left, increment by left if found
            j = left_i - 1
            left_num_start = -1
            left_num_end = -1
            while j >= 0:
                if new_a[j].isnumeric():
                    left_num_end = j
                    while j >= 0:
                        if not new_a[j].isnumeric():
                            left_num_start = j + 1
                            break
                        j -= 1
                    left_num_val = int(new_a[left_num_start:left_num_end+1])
                    # print('left val:', left_num_val)
                    left_num_val += left
                    new_a = new_a[:left_num_start] + str(left_num_val) + new_a[left_num_end+1:]
                    # print('added to left:',new_a)
                    break
                j -= 1
            # if left_num_end == -1:
            #     print('no left num')

            # scan right, increment by right if found
            j = right_i + 1
            right_num_start = -1
            right_num_end = -1
            while j < len(new_a):
                if new_a[j].isnumeric():
                    right_num_start = j
                    while j < len(new_a):
                        if not new_a[j].isnumeric():
                            right_num_end = j - 1
                            break
                        j += 1
                    right_num_val = int(new_a[right_num_start:right_num_end+1])
                    # print('right val:', right_num_val)
                    right_num_val += right
                    new_a = new_a[:right_num_start] + str(right_num_val) + new_a[right_num_end+1:]
                    # print('added to right:', new_a)
                    break
                j += 1
            break

    # Final scan and replace original nested list with 0
    # Have to rescan since original left_i/right_i might have shifted
    # due to additions of left and right numbers
    depth = 0
    for i in range(len(new_a)):
        if new_a[i] == '[':
            depth += 1
        if new_a[i] == ']':
            depth -= 1
        if depth == 5: # this list is nested inside four pairs
            left_i = i
            right_i = -1
            # scan forward until ']'
            for j in range(i+1, len(new_a)):
                if new_a[j] == ']':
                    right_i = j
                    break
            assert(right_i != -1)
            new_a = new_a[:left_i] + '0' + new_a[right_i+1:]
            return True, new_a

    return False, new_a

def split(a): # list[char]
    num_start = -1
    num_end = -1
    for i in range(len(a)):
        if a[i].isnumeric():
            num_start = i
            for j in range(i+1,len(a)):
                if not a[j].isnumeric():
                    num_end = j - 1
                    break
            num_val = int(a[num_start:num_end+1])
            if num_val >= 10:
                div2 = num_val//2
                if num_val % 2 == 0:
                    new_pair = '[' + str(div2) + ',' + str(div2) + ']'
                else:
                    new_pair = '[' + str(div2) + ',' + str(div2+1) + ']'
                return True, a[:num_start] + new_pair + a[num_end+1:]

    return False, a

def reduce(a): # list[char]
    while True:
        # print(a)
        exploded, a = explode(a)
        if exploded:
            # print('exploded')
            continue
        splitted, a = split(a)
        if not exploded and not splitted:
            break
        # print('split')

    return a

def magnitude(a): # list[char]
    if a.isnumeric():
        return int(a)

    left = ''
    right = ''
    # print(a)

    if a[1] == '[':
        # find corresponding ']'
        depth = 0
        found_i = -1
        for i in range(2, len(a)-1):
            if a[i] == '[':
                depth += 1
            elif a[i] == ']':
                if depth == 0:
                    found_i = i
                    break
                else:
                    depth -= 1
        assert(found_i != -1)
        left = a[1:found_i+1]
        right = a[found_i+2:-1] # skip comma
    else:
        # find first ','
        found_i = -1
        for i in range(1, len(a)-1):
            if a[i] == ',':
                found_i = i
                break
        assert(found_i != -1)
        left = a[1:found_i]
        right = a[found_i+1:-1] # skip comma

    return 3 * magnitude(left) + 2 * magnitude(right)

def homework(numbers):
    s = numbers[0]
    for i in range(1, len(numbers)):
        # print('numbers[i]:',numbers[i])
        # print('sum', s)
        # print('reduce', add(s, numbers[i]))
        s = reduce(add(s, numbers[i]))
        if ' ' in s:
            assert(False)
    return s

def expect_eq(a, b):
    if a != b:
        print("not equal")
        print("   actual   :", a)
        print("   expected :", b)
        assert(False)

# magnitude tests
# print(magnitude('[1,2]'))
# print(magnitude('[[1,2],[[3,4],5]]'))
# print(magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'))
# print(magnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'))

# add tests
# print(magnitude(add('[1,2]', '[[3,4],5]')))

# explode tests
# expect_eq(explode('[[[[[9,8],1],2],3],4]')[1], '[[[[0,9],2],3],4]')
# expect_eq(explode('[7,[6,[5,[4,[3,2]]]]]')[1], '[7,[6,[5,[7,0]]]]')
# expect_eq(explode('[[6,[5,[4,[3,2]]]],1]')[1], '[[6,[5,[7,0]]],3]')
# expect_eq(explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')[1], '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
# expect_eq(explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')[1], '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
# expect_eq(explode('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]')[1], '[[[[0,7],4],[15,[0,13]]],[1,1]]')

# split tests
# print(split('[3,[4,[12,[5,0]]]]'))
# print(split('[[[[0,7],4],[15,[0,13]]],[1,1]]'))

# reduce tests
# print(reduce(add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]')))
# print(reduce('[[[[[5,6],[7,8]],[[5,0],8]],[[3,[3,7]],[[3,7],[0,8]]]],[8,[[5,5],[2,9]]]]'))

# homework tests
large_sample = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]'''

# print(homework(['[1,1]','[2,2]','[3,3]','[4,4]']))
# print(homework(['[1,1]','[2,2]','[3,3]','[4,4]','[5,5]']))
# print(homework(large_sample.split('\n')))

lines = list(fileinput.input())
numbers = [line.rstrip() for line in lines]

# part 1
print(magnitude(homework(numbers[:])))

# part 2
max_mag = -1
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        a = numbers[i]
        b = numbers[j]

        max_mag = max(max_mag, magnitude(reduce(add(a, b))))
        max_mag = max(max_mag, magnitude(reduce(add(b, a))))
print(max_mag)
