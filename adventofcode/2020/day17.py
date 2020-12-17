import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append(l)
    return vals

def neighbors3(point):
    nbr = set()
    x,y,z = point
    for nx in range(x-1,x+2):
        for ny in range(y-1,y+2):
            for nz in range(z-1,z+2):
                np = (nx,ny,nz)
                nbr.add(np)
    nbr.remove(point)
    return list(nbr)

def neighbors4(point):
    nbr = set()
    x,y,z,w = point
    for nx in range(x-1,x+2):
        for ny in range(y-1,y+2):
            for nz in range(z-1,z+2):
                for nw in range(w-1,w+2):
                    np = (nx,ny,nz,nw)
                    nbr.add(np)
    nbr.remove(point)
    return list(nbr)

def bounds3(active):
    min_x = min([a[0] for a in active]) - 1
    max_x = max([a[0] for a in active]) + 1
    min_y = min([a[1] for a in active]) - 1
    max_y = max([a[1] for a in active]) + 1
    min_z = min([a[2] for a in active]) - 1
    max_z = max([a[2] for a in active]) + 1
    return min_x,max_x,min_y,max_y,min_z,max_z

def bounds4(active):
    min_x = min([a[0] for a in active]) - 1
    max_x = max([a[0] for a in active]) + 1
    min_y = min([a[1] for a in active]) - 1
    max_y = max([a[1] for a in active]) + 1
    min_z = min([a[2] for a in active]) - 1
    max_z = max([a[2] for a in active]) + 1
    min_w = min([a[3] for a in active]) - 1
    max_w = max([a[3] for a in active]) + 1
    return min_x,max_x,min_y,max_y,min_z,max_z,min_w,max_w

def print_cube(cycle, active):
    min_x,max_x,min_y,max_y,min_z,max_z = bounds(active)
    print('\n\n')
    print('------------- CYCLE {} -------------'.format(cycle))
    print('\n\n')
    cube = ''
    for z in range(min_z, max_z + 1):
        cube += '\n\nz = {}\n\n'.format(z)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                p = (x,y,z)
                if p in active:
                    cube += '#'
                else:
                    cube += '.'
            cube += '\n'
    print(cube)

def part1(vals):
    n = len(vals[0])
    active = set()
    for y in range(n):
        for x in range(n):
            if vals[y][x] == '#':
                active.add((x,y,0))

    ncycles = 6
    for c in range(ncycles):
        # print_cube(c, active)
        next_active = set()
        min_x,max_x,min_y,max_y,min_z,max_z = bounds3(active)
        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    p = (x,y,z)
                    nbr_p = neighbors3(p)
                    active_nbr = [nbr for nbr in nbr_p if nbr in active]
                    num_active_nbr = len(active_nbr)
                    if p in active:
                        if num_active_nbr == 2 or num_active_nbr == 3:
                            next_active.add(p)
                    else:
                        if num_active_nbr == 3:
                            next_active.add(p)
        active = next_active
    return len(active)

def part2(vals):
    n = len(vals[0])
    active = set()
    for y in range(n):
        for x in range(n):
            if vals[y][x] == '#':
                active.add((x,y,0,0))

    ncycles = 6
    for c in range(ncycles):
        next_active = set()
        min_x,max_x,min_y,max_y,min_z,max_z,min_w,max_w = bounds4(active)
        for w in range(min_w, max_w + 1):
            for z in range(min_z, max_z + 1):
                for y in range(min_y, max_y + 1):
                    for x in range(min_x, max_x + 1):
                        p = (x,y,z,w)
                        nbr_p = neighbors4(p)
                        active_nbr = [nbr for nbr in nbr_p if nbr in active]
                        num_active_nbr = len(active_nbr)
                        if p in active:
                            if num_active_nbr == 2 or num_active_nbr == 3:
                                next_active.add(p)
                        else:
                            if num_active_nbr == 3:
                                next_active.add(p)
        active = next_active
    return len(active)

vals = parse()
print(part1(list(vals)))
print(part2(list(vals)))
