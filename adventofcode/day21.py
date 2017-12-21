def flips_and_rotates(grid):
    f = [grid]

    # flip about vert axis
    fvert = []
    for row in grid:
        fvert.append(''.join(reversed(row)))
    if fvert not in f:
        f.append(fvert)

    # flip about horiz axis
    fhoriz = []
    for row in reversed(grid):
        fhoriz.append(row)
    if fhoriz not in f:
        f.append(fhoriz)

    # flip about horiz and vert axis
    fboth = []
    for row in reversed(grid):
        fboth.append(''.join(reversed(row)))
    if fboth not in f:
        f.append(fboth)

    for g in f:
        # rotation y=x
        r = [''.join(list(x)) for x in zip(*g)]
        if r not in f:
            f.append(r)

        # rotation y=-x
        rvert = []
        for row in r:
            rvert.append(''.join(reversed(row)))
        if rvert not in f:
            f.append(rvert)

    return f

"""read lines from stdin, split lines on whitespace"""
import fileinput
rules = {}
for line in fileinput.input():
    pre, post = line.split()
    pregrid = pre.split('/')
    postgrid = post.split('/')
    allgrids = flips_and_rotates(pregrid)
    for g in allgrids:
        s = ' '.join(g)
        rules[s] = postgrid

grid = [
    ".#.",
    "..#",
    "###",
]
size = 3
# grid = [
#     ".#..#.",
#     "..#..#",
#     "######",
#     ".#..#.",
#     "..#..#",
#     "######",
# ]
# size = 6

#3, 4
#6, 8
#9, 12
#12, 16

# 2 3
# 4 6
# 6 9

for n in range(18):
    if size % 2 == 0:
        nextsize = size + size/2
        nextgrid = ['' for _ in range(nextsize)]
        subgrids = []
        for ridx in range(0, size, 2):
            for cidx in range(0, size, 2):
                subgrid = []
                subgrid.append(grid[ridx][cidx:cidx+2])
                subgrid.append(grid[ridx+1][cidx:cidx+2])
                tf = rules[' '.join(subgrid)]
                subgrids.append(tf)

        sg_idx = 0
        for ridx in range(0, nextsize, 3):
            for cidx in range(0, nextsize, 3):
                nextgrid[ridx] += subgrids[sg_idx][0]
                nextgrid[ridx+1] += subgrids[sg_idx][1]
                nextgrid[ridx+2] += subgrids[sg_idx][2]
                sg_idx += 1
    elif size % 3 == 0:
        nextsize = size + size/3
        nextgrid = ['' for _ in range(nextsize)]
        subgrids = []
        for ridx in range(0, size, 3):
            for cidx in range(0, size, 3):
                subgrid = []
                subgrid.append(grid[ridx][cidx:cidx+3])
                subgrid.append(grid[ridx+1][cidx:cidx+3])
                subgrid.append(grid[ridx+2][cidx:cidx+3])
                tf = rules[' '.join(subgrid)]
                subgrids.append(tf)

        sg_idx = 0
        for ridx in range(0, nextsize, 4):
            for cidx in range(0, nextsize, 4):
                nextgrid[ridx] += subgrids[sg_idx][0]
                nextgrid[ridx+1] += subgrids[sg_idx][1]
                nextgrid[ridx+2] += subgrids[sg_idx][2]
                nextgrid[ridx+3] += subgrids[sg_idx][3]
                sg_idx += 1
    grid = nextgrid[:]
    size = nextsize

def count_on(grid):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '#':
                sum += 1
    return sum

print count_on(grid)
