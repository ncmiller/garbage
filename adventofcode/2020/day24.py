import fileinput
from collections import Counter

#   +z
#    |
#   / \
# +y   +x

xyz_delta = {
    'e':  (1,-1,0),
    'ne': (0,-1,1),
    'nw': (-1,0,1),
    'w':  (-1,1,0),
    'sw': (0,1,-1),
    'se': (1,0,-1),
}

def add_coords(a,b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])

def parse():
    flips = []
    for line in fileinput.input():
        dirs = []
        l = line[:-1]
        i = 0
        while i < len(l):
            c = l[i]
            if c == 's' or c == 'n':
                dirs.append(c + l[i+1])
                i += 1
            else:
                dirs.append(c)
            i += 1
        flips.append(dirs)
    return flips

def part1(flips):
    tiles_flipped = {}
    for f in flips:
        t = (0,0,0)
        for d in f:
            t = add_coords(t, xyz_delta[d])
        if t in tiles_flipped:
            tiles_flipped[t] ^= 1
        else:
            tiles_flipped[t] = 1

    total_black = 0
    for v in tiles_flipped.values():
        if v == 1:
            total_black += 1
    return total_black

def adjacent_hexes(h):
    return [
        add_coords(h, xyz_delta['e']),
        add_coords(h, xyz_delta['ne']),
        add_coords(h, xyz_delta['nw']),
        add_coords(h, xyz_delta['w']),
        add_coords(h, xyz_delta['sw']),
        add_coords(h, xyz_delta['se']),
    ]

def apply_rules(tiles_flipped):
    new_tiles_flipped = dict(tiles_flipped)

    min_x = min([x for x,y,z in tiles_flipped.keys()]) - 1
    max_x = max([x for x,y,z in tiles_flipped.keys()]) + 1
    min_y = min([y for x,y,z in tiles_flipped.keys()]) - 1
    max_y = max([y for x,y,z in tiles_flipped.keys()]) + 1
    min_z = min([z for x,y,z in tiles_flipped.keys()]) - 1
    max_z = max([z for x,y,z in tiles_flipped.keys()]) + 1
    # print(tiles_flipped)
    # print((min_x, min_y, min_z), (max_x, max_y, max_z))

    new_flips = set()
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            for z in range(min_z, max_z+1):
                t = (x,y,z)
                tile_is_black = (t in tiles_flipped and tiles_flipped[t] == 1)
                num_black_adjacent = 0
                for h in adjacent_hexes((x,y,z)):
                    if (h in tiles_flipped and tiles_flipped[h] == 1):
                        num_black_adjacent += 1
                if tile_is_black:
                    if num_black_adjacent == 0 or num_black_adjacent > 2:
                        new_flips.add(t)
                else:
                    if num_black_adjacent == 2:
                        new_flips.add(t)

    new_tiles_flipped = dict(tiles_flipped)
    for h in new_flips:
        if h in tiles_flipped:
            new_tiles_flipped[h] ^= 1
        else:
            new_tiles_flipped[h] = 1
    return new_tiles_flipped

def part2(flips):
    tiles_flipped = {}
    for f in flips:
        t = (0,0,0)
        for d in f:
            t = add_coords(t, xyz_delta[d])
        if t in tiles_flipped:
            tiles_flipped[t] ^= 1
        else:
            tiles_flipped[t] = 1

    ndays = 100
    total_black = 0
    for day in range(ndays):
        tiles_flipped = apply_rules(tiles_flipped)
        total_black = 0
        for v in tiles_flipped.values():
            if v == 1:
                total_black += 1
        print(day+1, total_black)
    return total_black

flips = parse()
print(part1(list(flips)))
print(part2(list(flips)))
