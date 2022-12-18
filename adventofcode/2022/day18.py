import fileinput

def in_bounds(coord, bounds):
    if not bounds:
        return True
    if coord[0] < bounds[0][0] or coord[0] > bounds[1][0]:
        return False
    if coord[1] < bounds[0][1] or coord[1] > bounds[1][1]:
        return False
    if coord[2] < bounds[0][2] or coord[2] > bounds[1][2]:
        return False
    return True

def coord_neighbors(coord, bounds):
    delta = [(-1,0,0),(0,-1,0),(0,0,-1),(1,0,0),(0,1,0),(0,0,1)]
    # list of tuples (c, d) where c is the neighbor coord, and d is the delta that got there.
    neighbor_coords = [(tuple_add(coord, d), d) for d in delta]
    return [nc for nc in neighbor_coords if in_bounds(nc[0], bounds)]

def part1(coords):
    coord_set = set(coords)
    total = 0
    for c in coords:
        total += 6
        for cn,_ in coord_neighbors(c, None):
            if cn != c and cn in coord_set:
                total -= 1
    return total

def tuple_add(a, b):
    return tuple(map(sum, zip(a,b)))


def part2(coords):
    # flood fill from outside, track cube faces touched
    coord_set = set(coords)
    min_x = min([c[0] for c in coords]) - 1
    min_y = min([c[1] for c in coords]) - 1
    min_z = min([c[2] for c in coords]) - 1
    max_x = max([c[0] for c in coords]) + 1
    max_y = max([c[1] for c in coords]) + 1
    max_z = max([c[2] for c in coords]) + 1
    bounds = [(min_x,min_y,min_z),(max_x,max_y,max_z)]

    faces_touched = set()
    visited = set()
    to_visit = []
    to_visit.append((min_x,min_y,min_z))
    while to_visit:
        coord = to_visit.pop()
        visited.add(coord)
        neighbors = coord_neighbors(coord, bounds)
        for n in neighbors:
            neighbor_coord, delta = n
            if neighbor_coord in coord_set:
                faces_touched.add(neighbor_coord + delta)
            elif neighbor_coord not in visited:
                to_visit.append(neighbor_coord)

    return len(faces_touched)

coords = [eval(line.rstrip()) for line in fileinput.input()]
print(part1(coords))
print(part2(coords))
