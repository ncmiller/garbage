import fileinput
import math
from collections import Counter

def vert_flip(tile):
    return [row for row in tile[::-1]]

def horiz_flip(tile):
    return [row[::-1] for row in tile]

def rotate90CW(tile):
    n = len(tile)
    new_tile = []
    for x in range(n):
        row = ''
        for y in range(n):
            row += tile[n - y - 1][x]
        new_tile.append(row)
    return new_tile

def find_edges(tile):
    # 0: top, 1: right, 2: bottom, 3: left
    # 4,5,6,7 are the same but reversed
    es = []
    es.append(tile[0])
    e = ''
    for row in tile:
        e += row[-1]
    es.append(e)
    es.append(tile[-1])
    e = ''
    for row in tile:
        e += row[0]
    es.append(e)
    es.append(es[0][::-1])
    es.append(es[1][::-1])
    es.append(es[2][::-1])
    es.append(es[3][::-1])
    return es

def parse():
    tiles = []
    n = 0
    tile_id = 0
    tile = []
    for line in fileinput.input():
        l = line.rstrip()
        n += 1
        if n == 1:
            tile_id = int(l.split(' ')[1].replace(':',''))
        elif n == 12:
            tiles.append((tile_id, tile))
            n = 0
            tile = []
        else:
            tile.append(l)
    return tiles

def find_corners(tiles):
    corners = []
    for i in range(len(tiles)):
        tid,tile = tiles[i]
        edges = find_edges(tile)
        edge_matches = []
        for j in range(len(tiles)):
            if i == j:
                continue
            other_tid,other_tile = tiles[j]
            other_edges = find_edges(other_tile)
            for ei1 in range(int(len(edges)/2)):
            # for ei1 in range(len(edges)):
                for ei2 in range(len(other_edges)):
                    if edges[ei1] == other_edges[ei2]:
                        edge_pair = (ei1, ei2)
                        edge_matches.append((tid,other_tid,ei1,ei2))
        if len(edge_matches) == 2:
            corners.append(edge_matches)
    return corners

def find_index_of_tid(tiles, tid):
    for i in range(len(tiles)):
        if tiles[i][0] == tid:
            return i
    assert(False)

def get_tile_by_tid(tiles, tid):
    return tiles[find_index_of_tid(tiles, tid)]

def print_puzzle(puzzle, n):
    s = ''
    for i in range(len(puzzle)):
        if i % n == 0 and i != 0:
            s += '\n'
        piece = puzzle[i]
        if piece:
            s += '{} '.format(piece[0])
        else:
            s += '____ '
    print(s)

def get_edge(tile, edge_index):
    if edge_index == 0:
        return tile[0]
    if edge_index == 1:
        t = rotate90CW(tile)
        t = rotate90CW(t)
        t = rotate90CW(t)
        return t[0]
    if edge_index == 2:
        return tile[-1]
    if edge_index == 3:
        t = vert_flip(tile)
        t = rotate90CW(t)
        return t[0]

def transform_tile(tile, transform):
    tid, t = tile
    for op in transform:
        if op == 'h':
            t = horiz_flip(t)
        elif op == 'r':
            t = rotate90CW(t)
    return (tid, t)

# tiles: [(tid,tile)]
def solve_puzzle(tiles):
    corners = find_corners(tiles)

    # pick first corner piece that has something on edges 1 (right) and 2 (bottom)
    # as the top-left corner
    top_left_corner = None
    for c in corners:
        e1 = c[0][2]
        e2 = c[1][2]
        if e1 == 1 and e2 == 2:
            top_left_corner = c
            break
    # print(top_left_corner)

    tids_to_place = set([tile[0] for tile in tiles])

    tl_tid = top_left_corner[0][0]
    tl_tile = get_tile_by_tid(tiles, tl_tid)

    n2 = len(tiles)
    n = int(math.sqrt(n2))
    puzzle = [None] * n2

    puzzle[0] = tl_tile
    tids_to_place.remove(tl_tid)

    # place pieces one at a time
    for i in range(1,len(puzzle)):
        x_offset = i % n
        y_offset = int(i / n)

        piece_to_match = None
        edges_to_match = None
        if x_offset == 0:
            # match piece on top
            assert(y_offset > 0)
            piece_to_match = puzzle[i - n]
            edges_to_match = (2,0)
        else:
            # match piece to the left
            piece_to_match = puzzle[i - 1]
            edges_to_match = (1,3)

        assert(piece_to_match)
        e1 = get_edge(piece_to_match[1], edges_to_match[0])

        transforms = ['', 'r', 'rr', 'rrr', 'h', 'hr', 'hrr', 'hrrr']
        found_tile = False
        new_tile = None
        for tid in tids_to_place:
            if found_tile:
                break
            candidate_tile = get_tile_by_tid(tiles, tid)
            for transform in transforms:
                transformed_candidate_tile = transform_tile(candidate_tile, transform)
                e2 = get_edge(transformed_candidate_tile[1], edges_to_match[1])
                if e1 == e2:
                    found_tile = True
                    new_tile = transformed_candidate_tile
        assert(new_tile)
        puzzle[i] = new_tile
        tids_to_place.remove(new_tile[0])
    return puzzle

def remove_borders(t):
    n = len(t)
    new_t = []
    for row in t:
        new_t.append(row[1:-1])
    return new_t[1:-1]

def remove_borders_from_puzzle(puzzle):
    new_puzzle = []
    for tile in puzzle:
        tid,t = tile
        t = remove_borders(t)
        new_puzzle.append((tid,t))
    return new_puzzle

def create_puzzle_image(puzzle):
    s = ''
    n = int(math.sqrt(len(puzzle)))
    tile_n = len(puzzle[0][1])
    tile_row_index = 0
    for i in range(0, len(puzzle), n):
        tiles_to_print = puzzle[i:i+n]
        for j in range(tile_n):
            for t in tiles_to_print:
                s += t[1][j]
            s += '\n'
    return s

def monster_found(rows, sea_monster):
    monster_len = len(sea_monster[0])
    row_len = len(rows[0])

    x_offsets = []
    for x_offset in range(row_len - monster_len):
        monster_found = True
        for y in range(len(sea_monster)):
            if not monster_found:
                break
            for x in range(len(sea_monster[0])):
                if not monster_found:
                    break
                sea_monster_c = sea_monster[y][x]
                row_c = rows[y][x_offset + x]
                if sea_monster_c == ' ':
                    continue
                else:
                    if row_c != '#':
                        monster_found = False
        if monster_found:
            x_offsets.append(x_offset)
    return x_offsets

def find_monsters(image, sea_monster):
    monster_count = 0
    new_image = list(image)
    for i in range(len(image)-3):
        rows_to_check = image[i:i+3]
        found_x_offsets = monster_found(rows_to_check, sea_monster)
        for xoff in found_x_offsets:
            y = i
            x = xoff
            for a in range(len(sea_monster)):
                for b in range(len(sea_monster[0])):
                    if sea_monster[a][b] == '#':
                        row_list = list(new_image[y+a])
                        row_list[x+b] = '0'
                        new_image[y+a] = ''.join(row_list)
            monster_count += 1
    return (monster_count, new_image)

def pound_count(list_of_str):
    n = 0
    for s in list_of_str:
        for c in s:
            if c == '#':
                n += 1
    return n

def part1(tiles):
    corners = find_corners(tiles)
    prod = 1
    for c in corners:
        tid = c[0][0]
        prod *= tid
    return prod

def part2(tiles):
    puzzle = solve_puzzle(tiles)
    puzzle = remove_borders_from_puzzle(puzzle)
    # print_puzzle(puzzle, int(math.sqrt(len(tiles))))
    # for tile in puzzle:
    #     print(tile)
    puzzle_image = create_puzzle_image(puzzle)
    # print(puzzle_image)

    sea_monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]

    transforms = ['', 'r', 'rr', 'rrr', 'h', 'hr', 'hrr', 'hrrr']
    for transform in transforms:
        transformed_image = puzzle_image.split('\n')[:-1]
        for op in transform:
            if op == 'h':
                transformed_image = horiz_flip(transformed_image)
            elif op == 'r':
                transformed_image = rotate90CW(transformed_image)
        # transformed_image = '\n'.join(transformed_image)
        n_monsters, marked_image = find_monsters(transformed_image, sea_monster)
        if n_monsters:
            # for row in marked_image:
            #     print(row)
            image_water_count = pound_count(marked_image)
            monster_water_count = n_monsters * pound_count(sea_monster)
            # print(n_monsters, image_water_count, monster_water_count)
            return image_water_count
    return -1

tiles = parse()
print(part1(tiles))
# not 1615, too high --> there should be more sea monsters
print(part2(tiles))
