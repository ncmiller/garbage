import fileinput
#----------------------
# File IO
#----------------------
# for line in fileinput.input():

# with open("day9_input.txt") as f:
#     chars = f.read()

# vals = map(int, fileinput.input())

# weight = int(fields[1].replace('(','').replace(')',''))
# stowers = [x.split(',')[0] for x in fields[2:]]
#----------------------

rects = []
for line in fileinput.input():
    line = line.rstrip()
    line = line.replace('#','').replace('@ ','').replace(',', ' ').replace(':','').replace('x', ' ').split(' ')
    rect = map(int, line)
    rects.append(rect)

#  -> x
# |y
# v
# .......
# .1...2.
# .......
# .3...4.
# .......

def print_fabric(fabric):
    for row in fabric:
        print row

def part1():
    N = 2000
    fabric = [['.' for _ in range(N)] for _ in range(N)]
    occupied_count = 0
    for r in rects:
        id, l, t, w, h = r
        p1 = (l, t)
        p2 = (l+w, t)
        p3 = (l, t+h)
        p4 = (l+w, t+h)
        # print p1, p2, p3, p4
        for x in range(p1[0], p2[0]):
            for y in range(p1[1], p3[1]):
                if fabric[x][y] == '.':
                    fabric[x][y] = '#'
                elif fabric[x][y] == '#':
                    fabric[x][y] = 'X'
                    occupied_count += 1
    # print_fabric(fabric)
    print occupied_count

    for r in rects:
        id, l, t, w, h = r
        p1 = (l, t)
        p2 = (l+w, t)
        p3 = (l, t+h)
        p4 = (l+w, t+h)
        overlapped = False
        for x in range(p1[0], p2[0]):
            for y in range(p1[1], p3[1]):
                if fabric[x][y] == 'X':
                    overlapped = True
        if not overlapped:
            print id

part1()
