import fileinput
import math
from queue import Queue
import heapq
import sys

def cycle(grid):
    return (len(grid), len(grid[0]))

def is_occupied(grid, query_pos, minute, start, dest):
    # start and dest are never occupied
    if query_pos == dest or query_pos == start:
        return False

    # walls are always occupied
    if query_pos[0] < 0 or query_pos[0] >= len(grid):
        return True
    if query_pos[1] < 0 or query_pos[1] >= len(grid[0]):
        return True

    # blizzards will depend on where in the cycle it is and the direction
    row_cycle, col_cycle = cycle(grid)
    if grid[query_pos[0]][(query_pos[1] + minute) % col_cycle] == '<':
        return True
    if grid[query_pos[0]][(query_pos[1] - minute) % col_cycle] == '>':
        return True
    if grid[(query_pos[0] + minute) % row_cycle][query_pos[1]] == '^':
        return True
    if grid[(query_pos[0] - minute) % row_cycle][query_pos[1]] == 'v':
        return True

    return False

def neighbors(pos):
    return [
        (pos[0] - 1, pos[1]), # up
        (pos[0] + 1, pos[1]), # down
        (pos[0], pos[1] - 1), # left
        (pos[0], pos[1] + 1), # right
    ]

def h(grid, pos, goal):
    return (goal[0] - pos[0]) + (goal[1] - pos[1])

def a_star(grid, minute, start, dest):
    nrows = len(grid)
    ncols = len(grid[0])
    max_minute = nrows * ncols

    gscore = {}
    fscore = {}

    openset = []
    visited = set()
    gscore[(start,minute)] = 0
    fscore[(start,minute)] = h(grid, start, dest)
    heapq.heappush(openset, (fscore[(start,minute)], (start,minute)))

    while openset:
        _, current = heapq.heappop(openset)
        if current[0] == dest:
            return minute + gscore[current]

        candidates = []
        ns = [n for n in neighbors(current[0]) if n != start]
        max_wait = 10
        for n in ns:
            for i in range(1, max_wait):
                if is_occupied(grid, current[0], current[1] + (i-1), start, dest):
                    break
                if not is_occupied(grid, n, current[1] + i, start, dest):
                    candidates.append((n,current[1] + i))

        for n in candidates:
            temp_gscore = gscore[current] + (n[1] - current[1])
            if n not in gscore:
                gscore[n] = 10000000
            if temp_gscore < gscore[n]:
                gscore[n] = temp_gscore
                fscore[n] = temp_gscore + h(grid, n[0], dest)
                v = (n[0],n[1])
                if v not in visited:
                    heapq.heappush(openset, (fscore[n], n))
                    visited.add(v)

    # not found
    return -1

# remove walls to simplify indexing
grid = [line.rstrip() for line in fileinput.input()]
grid = [row[1:-1] for row in grid[1:-1]]

# part 1
start = (-1, 0)
dest = (len(grid), len(grid[0])-1)
at_dest = a_star(grid, 0, start, dest)
print(at_dest)

# part 2
start = (len(grid), len(grid[0])-1)
dest = (-1, 0)
back_at_start = a_star(grid, at_dest, start, dest)

start = (-1, 0)
dest = (len(grid), len(grid[0])-1)
back_at_dest = a_star(grid, back_at_start, start, dest)

print(back_at_dest)
