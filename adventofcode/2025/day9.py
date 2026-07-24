import fileinput
from collections import defaultdict

def on_perimeter(x_coords, y_coords, coord):
    if coord[0] not in x_coords and coord[1] not in y_coords:
        return False

    # check vertical
    if coord[0] in x_coords:
        for i in range(0, len(x_coords[coord[0]]), 2):
            c1, c2 = x_coords[coord[0]][i], x_coords[coord[0]][i+1]
            if coord[1] >= c1[1] and coord[1] <= c2[1]:
                return True

    # check horizontal
    if coord[1] in y_coords:
        for i in range(0, len(y_coords[coord[1]]), 2):
            c1, c2 = y_coords[coord[1]][i], y_coords[coord[1]][i+1]
            if coord[0] >= c1[0] and coord[0] <= c2[0]:
                return True

    return False

def print_poly(poly_points, red_coords):
    min_x = min([c[0] for c in poly_points])
    max_x = max([c[0] for c in poly_points])
    min_y = min([c[1] for c in poly_points])
    max_y = max([c[1] for c in poly_points])
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) in red_coords:
                print('#', end='')
            elif (x,y) in poly_points:
                print('X', end='')
            else:
                print('.', end='')
        print('')

def get_poly_points(coords, red_coords, x_coords, y_coords):
    poly_points = set()
    start = coords[0]
    pos = start
    last_dir = '-'
    i = 0
    new_x_coords = defaultdict(set)
    new_y_coords = defaultdict(set)

    for i in range(10000000):
        if i != 0 and pos == start:
            break
        # print(pos)

        # search left
        if not last_dir == 'l' and last_dir != 'r':
        # if not last_dir == 'r':
            max_left = (-1,-1)
            for x,y in y_coords[pos[1]]:
                if x < pos[0]:
                    max_left = max(max_left, (x,y))
            if max_left != (-1,-1):
                for x in range(pos[0], max_left[0]-1, -1):
                    c = (x, pos[1])
                    poly_points.add(c)
                    new_x_coords[x].add(c)
                    new_y_coords[pos[1]].add(c)
                pos = max_left
                last_dir = 'l'
                continue

        # search up
        if not last_dir == 'd' and not last_dir == 'u':
        # if not last_dir == 'd':
            max_up = (-1, -1)
            for x,y in x_coords[pos[0]]:
                if y < pos[1]:
                    max_up = max(max_up, (x,y))
            if max_up != (-1,-1):
                for y in range(pos[1], max_up[1]-1, -1):
                    c = (pos[0], y)
                    poly_points.add(c)
                    new_x_coords[pos[0]].add(c)
                    new_y_coords[y].add(c)
                pos = max_up
                last_dir = 'u'
                continue


        # search down
        if not last_dir == 'd' and not last_dir == 'u':
        # if not last_dir == 'u':
            min_down = (1e9, 1e9)
            for x,y in x_coords[pos[0]]:
                if y > pos[1]:
                    min_down = min(min_down, (x,y))
            if min_down != (1e9, 1e9):
                for y in range(pos[1], min_down[1]):
                    c = (pos[0], y)
                    poly_points.add(c)
                    new_x_coords[pos[0]].add(c)
                    new_y_coords[y].add(c)
                pos = min_down
                last_dir = 'd'
                continue



        # search right
        if not last_dir == 'l' and last_dir != 'r':
        # if not last_dir == 'l':
            min_right = (1e9, 1e9)
            for x,y in y_coords[pos[1]]:
                if x > pos[0]:
                    min_right = min(min_right, (x,y))
            if min_right != (1e9, 1e9):
                for x in range(pos[0], min_right[0]):
                    c = (x, pos[1])
                    poly_points.add(c)
                    new_x_coords[x].add(c)
                    new_y_coords[pos[1]].add(c)
                pos = min_right
                last_dir = 'r'
                continue

    return poly_points, new_x_coords, new_y_coords


def get_rect_points(p1, p2):
    rect_points = []
    if p2 < p1:
        p1, p2 = p2, p1
    for x in range(p1[0], p2[0]+1):
        rect_points.append((x, p1[1]))
        rect_points.append((x, p2[1]))
    for y in range(p1[1], p2[1]+1):
        rect_points.append((p1[0], y))
        rect_points.append((p2[0], y))

    return rect_points

def rect_inside_poly(rect_points, poly_points, p1, p2):
    poly_points = set(poly_points)

    # debug_print = False
    # if p1 == (9,5) and p2 == (2,3):
    #     debug_print = True

    min_x = min([c[0] for c in poly_points])
    max_x = max([c[0] for c in poly_points])
    min_y = min([c[1] for c in poly_points])
    max_y = max([c[1] for c in poly_points])

    debug_print = False
    if p1 == (16463, 84861) and p2 == (83449, 15228):
        debug_print = True

    # search in each direction
    print(len(rect_points))
    np = 0
    for rp in rect_points:
        if debug_print and np % 1000 == 0: print(rp)
        np += 1
        # up
        # if debug_print: print('up')
        found = False
        for y in range(rp[1], min_y-1, -1):
            if (rp[0], y) in poly_points:
                found = True
                break
        if not found:
            # if debug_print:
            #     print('up')
            return False

        # left
        # if debug_print: print('left')
        found = False
        for x in range(rp[0], min_x-1, -1):
            if (x, rp[1]) in poly_points:
                found = True
                break
        if not found:
            return False

        # right
        # if debug_print: print('right')
        found = False
        for x in range(rp[0], max_x+1):
            if (x, rp[1]) in poly_points:
                found = True
                break
        if not found:
            return False

        # down
        # if debug_print: print('down')
        found = False
        for y in range(rp[1], max_y+1):
            if (rp[0], y) in poly_points:
                found = True
                break
        if not found:
            return False

    return True

def part1(coords):
    max_area = 0
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            p1, p2 = coords[i], coords[j]
            length = abs(p2[0] - p1[0]) + 1
            width = abs(p2[1] - p1[1]) + 1
            area = length * width
            max_area = max(max_area, area)
    return max_area

def part2(coords):
    red_coords = set(coords)

    coords = sorted(coords)
    x_coords = defaultdict(list)
    y_coords = defaultdict(list)
    for sc in coords:
        x_coords[sc[0]].append(sc)
        y_coords[sc[1]].append(sc)

    min_x = min([c[0] for c in coords])
    max_x = max([c[0] for c in coords])
    min_y = min([c[1] for c in coords])
    max_y = max([c[1] for c in coords])
    # print(min_x, min_y, max_x, max_y)


    # on perimeter if:
    #   * it's between any pairs of coords
    #   * it's between any pairs of transposed coords
    # rectangle in polygon if:
    #   * each point on perimeter of rectangle is inside polygon
    # green if:
    #   * in rectangle and not in red_coords

    # sort by area
    # areas = []
    # for i in range(len(coords)):
    #     for j in range(i+1, len(coords)):
    #         p1, p2 = coords[i], coords[j]
    #         length = abs(p2[0] - p1[0]) + 1
    #         width = abs(p2[1] - p1[1]) + 1
    #         area = length * width
    #         areas.append((area, p1, p2))
    # areas.sort(reverse=True)

    # print('areas', len(areas))
    poly_points, x_coords, y_coords = get_poly_points(coords, red_coords, x_coords, y_coords)
    # print('poly_points', len(poly_points))
    # print_poly(poly_points, red_coords)

    for x,c in x_coords.items():
        print(x, c)

    # for area in areas[140:]:
    # for area in areas:
        # a, p1, p2 = area
        # print(a, p1, p2)
        # rect_points = set(get_rect_points(p1, p2))
        # # rect_points = (p1, p2, (p2[0], p1[1]), (p1[0], p2[1]))
        # if rect_inside_poly(rect_points, poly_points, p1, p2):
        #     return a

    # x_coords_y_range = dict()
    # for cs in x_coords.values():
    #     cs = list(cs)
    #     min_y = min([y for _,y in cs])
    #     max_y = max([y for _,y in cs])
    #     x_coords_y_range[cs[0][0]] = (min_y, max_y)

    # y_coords_x_range = dict()
    # for cs in y_coords.values():
    #     cs = list(cs)
    #     min_x = min([x for x,_ in cs])
    #     max_x = max([x for x,_ in cs])
    #     y_coords_x_range[cs[0][1]] = (min_x, max_x)

    # print(x_coords_y_range)
    # print(y_coords_x_range)

    # for each corner, check that it's within min/max x/y
    max_area = -1
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            p1, p2 = coords[i], coords[j]
            p3, p4 = (p2[0], p1[1]), (p1[0], p2[1])
            corners = (p1, p2, p3, p4)
            valid = True
            for c in corners:
                x,y = c
                y_range = x_coords_y_range[x]
                x_range = y_coords_x_range[y]
                if x < x_range[0] or x > x_range[1]:
                    # print(f'OOR: {corners}, {c}, {y_range}, {x_range}')
                    valid = False
                    break
                if y < y_range[0] or y > y_range[1]:
                    # print(f'OOR: {corners}, {c}, {y_range}, {x_range}')
                    valid = False
                    break
            if valid:
                # print('valid',corners)
                length = abs(p2[0] - p1[0]) + 1
                width = abs(p2[1] - p1[1]) + 1
                max_area = max(max_area, length*width)

    return max_area

coords = [tuple(map(int, l.split(','))) for l in fileinput.input()]
print(part1(coords))

# Too high (4664572758)
print(part2(coords))
