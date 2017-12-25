import re

# puzzle = raw_input()
lengths = map(int, puzzle.split(','))
N = 256
l = range(N)

def reverse_slice(pos, length):
    n = pos + length
    if n >= N:
        forward_slice = l[pos:] + l[:(n%N)]
        rev_slice = list(reversed(forward_slice))
        l[pos:] = rev_slice[:N-pos]
        l[:n%N] = rev_slice[N-pos:]
    else:
        forward_slice = l[pos:n]
        l[pos:n] = list(reversed(forward_slice))

pos = 0
skip = 0
for length in lengths:
    reverse_slice(pos, length)
    pos = (pos + length + skip) % N
    skip += 1

print l[0]*l[1]

#----

def densehash(s):
    a = map(lambda x: ord(x), s)
    a = a + [17, 31, 73, 47, 23]

    pos = 0
    skip = 0
    for i in range(64):
        for length in a:
            reverse_slice(pos, length)
            pos = (pos + length + skip) % N
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

lengths = puzzle.lstrip().rstrip()

def to_hex(v):
    return "{:02x}".format(v)

l = range(N)
a = map(lambda x: ord(x), lengths)
a = a + [17, 31, 73, 47, 23]

pos = 0
skip = 0
for i in range(64):
    for length in a:
        reverse_slice(pos, length)
        pos = (pos + length + skip) % N
        skip += 1
sparse_hash = l

dense_hash = []

for i in range(16):
    x = 0
    vals = l[(i*16):(i*16+16)]
    for v in vals:
        x = x ^ v
    dense_hash.append(x)

print ''.join(map(to_hex, dense_hash))
