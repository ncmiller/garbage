import fileinput
from heapq import heappush, heappop

dp_to_dir = {
    (0, 1): 'E',
    (1, 0): 'S',
    (-1, 0): 'N',
    (0, -1): 'W',
}

dir_to_neighbors = {
    'N': ('N', 'E', 'W'),
    'E': ('E', 'N', 'S'),
    'W': ('N', 'S', 'W'),
    'S': ('S', 'E', 'W'),
}

dir_to_dp = dict((v, k) for k, v in dp_to_dir.items())

def reconstruct_path(came_from, current, limit=1000000000):
    total_path = [current[0]]
    while current in came_from.keys() and len(total_path) < limit:
        current = came_from[current]
        total_path.append(current[0])
    return list(reversed(total_path))

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def oob(grid, p):
    return (p[0] < 0) or (p[1] < 0) or (p[0] >= len(grid)) or (p[1] >= len(grid[0]))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def direction(path):
    if len(path) == 1:
        return 'E'

    # print(path)
    dx = path[-1][0] - path[-2][0]
    dy = path[-1][1] - path[-2][1]
    return dp_to_dir[(dx, dy)]

def heat_loss(grid, path):
    total = 0
    for i in range(1, len(path)):
        x, y = path[i]
        total += int(grid[x][y])
    return total

def all_in_same_direction(path):
    if all(p[0] == path[0][0] for p in path):
        return True
    if all(p[1] == path[0][1] for p in path):
        return True
    return False

def a_star(grid, start, goal):
    open_set = []
    came_from = {}
    g_score = {}
    f_score = {}

    g_score[start] = 0
    f_score[start] = dist(start[0], goal)
    heappush(open_set, (f_score[start], start))

    maxlen = 0
    while open_set:
        score, current = heappop(open_set)
        current_pos, current_path = current
        if current_pos == goal:
            # for k, v in g_score.items():
                # print(k, v)
            return reconstruct_path(came_from, current)
        # print(score, current)

        path = reconstruct_path(came_from, current)
        last_4 = path[-4:]
        d = direction(last_4)
        neighbors = list(dir_to_neighbors[direction(last_4)])

        if len(path) > maxlen:
            maxlen = len(path)
            print(maxlen)
        # print(path, d)

        # part 1
        # if len(last_4) == 4 and all_in_same_direction(last_4):
        #     # print('remove', d)
        #     neighbors.remove(d)

        # part 2
        last_5 = path[-5:]
        last_11 = path[-11:]
        if len(last_5) <= 5 and not all_in_same_direction(last_5): # below 4 - only in same direction
            neighbors = [n for n in neighbors if n == d]
        elif len(last_11) == 11 and all_in_same_direction(last_11): # 10+ - not in same same direction
            # print('remove', d)
            neighbors.remove(d)
        else: # 4-10 - any neighbor direction
            pass

        neighbors = [add(current[0], dir_to_dp[n]) for n in neighbors]
        neighbors = [n for n in neighbors if not oob(grid, n)]
        # print('neighbors', neighbors)
        for n in neighbors:
            # part 1
            # n = (n, tuple(last_4[1:] + [n]))
            # part 2
            n = (n, tuple(last_11[1:] + [n]))
            tentative_g_score = g_score[current] + int(grid[n[0][0]][n[0][1]])
            if n not in g_score or tentative_g_score < g_score[n]:
                came_from[n] = current
                g_score[n] = tentative_g_score
                f_score[n] = tentative_g_score + dist(n[0], goal)
                # print('better', n, f_score[n])
                if n not in open_set:
                    # print('push')
                    heappush(open_set, (f_score[n], n))

    return None


def part1(grid):
    path = a_star(grid, ((0,0), (None, None, None, None)), (len(grid)-1, len(grid[0])-1))
    print(path[0], 'E')
    for i in range(1, len(path)):
        print(path[i], direction(path[:i+1]))

    return heat_loss(grid, path)

grid = [l[:-1] for l in fileinput.input()]
print(part1(grid))
