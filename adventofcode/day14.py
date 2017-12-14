def to_hex(v):
    return "{:02x}".format(v)

# l = range(256)
def reverse_slice(pos, length, l):
    N = 256
    n = pos + length
    if n >= N:
        forward_slice = l[pos:] + l[:(n%N)]
        rev_slice = list(reversed(forward_slice))
        l[pos:] = rev_slice[:N-pos]
        l[:n%N] = rev_slice[N-pos:]
    else:
        forward_slice = l[pos:n]
        l[pos:n] = list(reversed(forward_slice))

def densehash(s):
    l = range(256)
    s = s.lstrip().rstrip()
    a = map(lambda x: ord(x), s)
    a = a + [17, 31, 73, 47, 23]

    pos = 0
    skip = 0
    for i in range(64):
        for length in a:
            reverse_slice(pos, length, l)
            pos = (pos + length + skip) % 256
            skip += 1
    sparse_hash = l

    dense_hash = []

    for i in range(16):
        x = 0
        vals = l[(i*16):(i*16+16)]
        for v in vals:
            x = x ^ v
        dense_hash.append(x)
    return ''.join(map(to_hex, dense_hash))

binmap = {
    '0': [0,0,0,0],
    '1': [0,0,0,1],
    '2': [0,0,1,0],
    '3': [0,0,1,1],
    '4': [0,1,0,0],
    '5': [0,1,0,1],
    '6': [0,1,1,0],
    '7': [0,1,1,1],
    '8': [1,0,0,0],
    '9': [1,0,0,1],
    'a': [1,0,1,0],
    'b': [1,0,1,1],
    'c': [1,1,0,0],
    'd': [1,1,0,1],
    'e': [1,1,1,0],
    'f': [1,1,1,1],
}
def tobin(hexstr):
    l = []
    for digit in hexstr:
        l = l + binmap[digit]
    return l

i = 'ffayrhll'
# i = 'flqrgnkx'
# i = ''
N = 128

grid = []
for x in range(N):
    grid.append([0 for _ in range(N)])

total = 0
for row in range(N):
    hash_in = i + '-' + str(row)
    # print hash_in
    # print densehash(hash_in)
    grid[row] = tobin(densehash(hash_in))
    total += sum(grid[row])
print total

#---
def adj(i, j):
    #               up        left      down      right
    neighbors = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
    ret = []
    for n in neighbors:
        if n[0] >= 0 and n[0] < 128 and n[1] >= 0 and n[1] < 128:
            if grid[n[0]][n[1]] == 1:
                ret.append(n)
    return ret


part_of_group = set()
numgroups = 0
for i in range(128):
    for j in range(128):
        if grid[i][j] == 1:
            if (i, j) not in part_of_group:
                part_of_group.add((i,j))
                numgroups += 1

                adjacent = [(i,j)]
                while adjacent:
                    # if numgroups == 1:
                    #     print numgroups, i, j
                    front = adjacent.pop(0)
                    neighbors = adj(front[0], front[1])
                    for n in neighbors:
                        if (n[0], n[1]) not in part_of_group:
                            adjacent.append((n[0], n[1]))
                            part_of_group.add((n[0], n[1]))
                            # if numgroups == 1:
                            #     print numgroups, i, j
print numgroups
