import fileinput
from collections import defaultdict

def convert_hex(hex_string):
    hex_string = hex_string[1:-1] # remove ()
    dirmap = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    steps = int(hex_string[1:-1], 16)
    direction = dirmap[hex_string[-1]]
    return direction, steps

def neighbors(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def floodfill(rows, startx, starty):
    visited = []
    visited.append((startx, starty))
    while visited:
        x,y = visited[0]
        rows[x].add(y)
        visited = visited[1:]
        ns = [n for n in neighbors(x,y) if n not in visited]
        ns = [(x,y) for (x,y) in ns if y not in rows[x]]
        visited += ns

def numhashes(rows):
    return sum([len(ys) for ys in rows.values()])

def part1(lines):
    x, y = 0, 0
    rows = defaultdict(set)
    for d,v,c in lines:
        for i in range(int(v)):
            if d == 'R':
                y += 1
            elif d == 'L':
                y -= 1
            elif d == 'U':
                x  -= 1
            else: # d == 'D':
                x  += 1
            rows[x].add(y)
            # print('add:',x,y)

    # minx, miny = 100000000, 100000000
    # maxx, maxy = -100000000, -10000000
    # for x, ys in rows.items():
    #     for y in ys:
    #         minx = min(minx, x)
    #         miny = min(miny, y)
    #         maxx = max(maxx, x)
    #         maxy = max(maxy, y)
    # print(minx, miny, maxx, maxy)
    # xrange = maxx-minx + 1
    # yrange = maxy-miny + 1
    # print(xrange, yrange)

    floodfill(rows, 1, 1) # sample
    # floodfill(rows, -1, -1) # input

    return numhashes(rows)


def part2(lines):
    vertices = {}
    edges = set()
    x, y = 0, 0
    dvs = []
    for i,stuff in enumerate(lines):
        d,v,c = stuff
        # dvs.append((d,v))
        dvs.append(convert_hex(c))

    for i,stuff in enumerate(dvs):
        oldx, oldy = x, y
        d,v = stuff
        # print(d,v,c)
        if i == 0:
            prior_d = dvs[-1][0]
        else:
            prior_d = dvs[i-1][0]
        combo = prior_d + d
        # print(i, combo)
        t = None
        if combo == 'UR' or combo == 'LD':
            t = 'F'
        elif combo == 'RD' or combo == 'UL':
            t = '7'
        elif combo == 'RU' or combo == 'DL':
            t = 'J'
        elif combo == 'DR' or combo == 'LU':
            t = 'L'
        assert(t)

        vertices[(x,y)] = t

        if d == 'R':
            y += int(v)
        elif d == 'L':
            y -= int(v)
        elif d == 'U':
            x  -= int(v)
        else: # d == 'D':
            x  += int(v)

        edges.add(((oldx, oldy), (x,y)))

    # print(vertices)
    # print(edges)

    minx = 100000000
    maxx = -100000000
    for x, y in vertices.keys():
        minx = min(minx, x)
        maxx = max(maxx, x)
    # print(minx, maxx)

    vert_edges = [e for e in edges if e[0][1] == e[1][1]]
    # print(vert_edges)
    row_patterns = []
    for x in range(minx, maxx+1):
        # check all vertical edges, determine intersection point (if any)
        ipoints = []
        for ve in vert_edges:
            a, b = ve
            if b[0] < a[0]:
                a,b = b,a
            # now a is guaranteed lower x coord
            if x >= a[0] and x <= b[0]:
                ipoints.append((x,a[1]))
        # sort ipoints by y value
        ipoints = sorted(ipoints)

        # print(ipoints)
        row_pattern = []
        for point in ipoints:
            if point in vertices:
                row_pattern.append((point, vertices[point]))
            else:
                row_pattern.append((point, '|'))
        row_patterns.append(row_pattern)

    # for rp in row_patterns:
    #     print(rp)

    total = 0
    for i,rp in enumerate(row_patterns):
        # if i % 1000 == 0:
        #     print(i)
        prior_is_outside = True
        prior_point = None
        is_outside = True
        is_top = False
        for i, stuff in enumerate(rp):
            point, c = stuff
            if c == 'F':
                if is_outside:
                    is_outside = False
                    is_top = True
                else:
                    is_top = False
            elif c == 'J':
                if not is_top:
                    is_outside = not is_outside
            elif c == 'L':
                if is_outside:
                    is_outside = False
                    is_top = False
                else:
                    is_top = True
            elif c == '7':
                if is_top:
                    is_outside = not is_outside
            elif c == '|':
                is_outside = not is_outside

            # print(point, c, is_outside, prior_is_outside)
            if i > 0:
                if not prior_is_outside:
                    total += (point[1] - prior_point[1] + 1)
                    if not is_outside:
                        total -= 1 # avoid double-counting

            prior_is_outside = is_outside
            prior_point = point

    return total



    ######.###
    #....#.#.#
    #....###.#
    #........#
    #.####...#
    #.#..#.###
    ###..###..

    # F----7.F-7
    # |....|.|.|
    # |....L-J.|
    # |........|
    # |.F--7...|
    # |.|..|.F-J
    # L-J..L-J..

    # R: if next edge D, then top edge, else bottom edge
    # L: if next edge D, then top edge, else bottom edge
    # U: if next edge R, then left edge, else right edge
    # D: if next edge R, then left edge, else right edge

    # vertices are F, 7, L, or J
    # dict of vertices
    # for each row, find intersection points
    # if point in vertices, use that, otherwise it's |

    # F7F7
    #   - outside, bottom
    #   F inside, top
    #   7 outside, top
    #   F inside, top
    #   7 outside, top
    # ||||
    #   - outside, bottom
    #   | inside, bottom
    #   | outside, bottom
    #   | inside, bottom
    #   | outside, bottom
    # |LJ|
    #   - outside, bottom
    #   | inside, bottom
    #   L inside, top
    #   J inside, top
    #   | outside, top
    # ||
    #   - outside, bottom
    #   | inside, bottom
    #   | outside, bottom
    # |F7|
    #   - outside, bottom
    #   | inside, bottom
    #   F inside, bottom
    #   7 inside, bottom
    #   | outside, bottom
    # |||FJ
    #   - outside, bottom
    #   | inside, bottom
    #   | outside, bottom
    #   | inside, bottom
    #   F inside, bottom
    #   J outside, bottom
    # LJLJ
    #   - outside, bottom
    #   L inside, bottom
    #   J outside, bottom
    #   L inside, bottom
    #   J outside, bottom



    # (0,0), (0,5), T
    # (0,5), (2,5), L
    # (2,5), (2,7), B
    # (2,7), (0,7), L
    # (0,7), (0,9), T
    # (0,9), (5,9), R
    # (5,9), (5,7), T
    # (5,7), (6,7), R
    # (6,7), (6,5), B
    # (6,5), (4,5), R
    # (4,5), (4,2), T
    # (4,2), (6,2), R
    # (6,2), (6,0), B
    # (6,0), (0,0), L

    # 0
    #   (0,0), (0,5), (0,7), (0,9)
    #   (0,0)/(0,5): is top edge, count it, now outside
    #   (0,5)/(0,7): not edge, outside, so don't count it
    #   (0,7)/(0,9): is top edge, count it, now outside
    # 1
    #   (1,0), (1,5), (1,7), (1,9)
    #   (1,0), (1,5): not edge, outside, so count it, now outside
    #   (1,5), (1,7): not edge, outside

    # collect edges
    # for each row
    #   find intersection points with vertical edges
    #   if intersection is bottom of edge, and the intersection point again
    #   Pair up the intersection points, count (p0,p1), (p2,p3), ...

    # sample edges -> intersections
    # (0,0), (0,6) -> [(0,0)..(0,6)]
    # (0,6), (5,6) -> [(0,6)]
    # (5,6), (5,4)
    # (5,4), (7,4)
    # (7,4), (7,6)
    # (7,6), (9,6)
    # (9,6), (9,1)
    # (9,1), (7,1)
    # (7,1), (7,0)
    # (7,0), (5,0)
    # (5,0), (5,2)
    # (5,2), (2,2)
    # (2,2), (2,0)
    # (2,0), (0,0) -> [(0,0)]

lines = [l.split() for l in fileinput.input()]
print(part1(lines))
print(part2(lines)) # 11m5.847s on macbook pro
