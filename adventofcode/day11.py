from collections import defaultdict
l = raw_input().split(',')
""" Indexing in hex grid

            11
  012345678901
0  1 1 1 1 1 1
0 1 1 1 1 1 1
1  1 1 1 1 1 1
1 1 1 1 1 1 1
2  1 1 1 1 1 1
2 1 1 1 1 1 1

n = up
ne = if col even: right, else: up, right
se = if col even: right, down, else: right
s = down
sw = if col even: down, left, else: left
nw = if col even: left, else: up, left

"""

counts = defaultdict(int)

# l = ['ne', 'ne', 'ne']
# l = ['ne', 'ne', 'sw', 'sw']
# l = ['ne', 'ne', 's', 's']
# l = ['se', 'sw', 'se', 'sw', 'sw']

def reduce_counts(counts):
    while(1):
        modified = False

        # n+se = ne
        if counts['n'] > 0 and counts['se'] > 0:
            m = min(counts['n'], counts['se'])
            counts['ne'] += m
            counts['n'] -= m
            counts['se'] -= m
            modified = True

        # n+sw = nw
        if counts['n'] > 0 and counts['sw'] > 0:
            m = min(counts['n'], counts['sw'])
            counts['nw'] += m
            counts['n'] -= m
            counts['sw'] -= m
            modified = True

        # s+ne = se
        if counts['s'] > 0 and counts['ne'] > 0:
            m = min(counts['s'], counts['ne'])
            counts['se'] += m
            counts['s'] -= m
            counts['ne'] -= m
            modified = True

        # s+nw = sw
        if counts['s'] > 0 and counts['nw'] > 0:
            m = min(counts['s'], counts['nw'])
            counts['sw'] += m
            counts['s'] -= m
            counts['nw'] -= m
            modified = True

        # se+sw = s
        if counts['se'] > 0 and counts['sw'] > 0:
            m = min(counts['se'], counts['sw'])
            counts['s'] += m
            counts['se'] -= m
            counts['sw'] -= m
            modified = True

        # ne+nw = n
        if counts['ne'] > 0 and counts['nw'] > 0:
            m = min(counts['ne'], counts['nw'])
            counts['n'] += m
            counts['ne'] -= m
            counts['nw'] -= m
            modified = True

        if not modified:
            break

    # sw+ne = 0
    if counts['sw'] > counts['ne']:
        counts['sw'] -= counts['ne']
        counts['ne'] = 0
    else:
        counts['ne'] -= counts['sw']
        counts['sw'] = 0

    # nw+se = 0
    if counts['nw'] > counts['se']:
        counts['nw'] -= counts['se']
        counts['se'] = 0
    else:
        counts['se'] -= counts['nw']
        counts['nw'] = 0

    # n+s = 0
    if counts['n'] > counts['s']:
        counts['n'] -= counts['s']
        counts['s'] = 0
    else:
        counts['s'] -= counts['n']
        counts['n'] = 0

maxdist = 0
for step in l:
    counts[step] += 1
    reduce_counts(counts)
    maxdist = max(maxdist, sum(counts.values()))

print sum(counts.values())
print maxdist
