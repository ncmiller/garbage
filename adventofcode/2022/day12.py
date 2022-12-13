import fileinput
import heapq

# Heuristic function - manhattan distance to goal
def h(grid, pos, goal):
    return (goal[0] - pos[0]) + (goal[1] - pos[1])

def is_at_most_one_higher(elev_src, elev_dest):
    return (ord(elev_dest) - ord(elev_src)) <= 1

def neighbors(grid, n):
    nrows = len(grid)
    ncols = len(grid[0])
    dpos = [(0,1),(0,-1),(-1,0),(1,0)]
    current_elevation = grid[n[0]][n[1]]
    candidates = [(n[0]+dp[0],n[1]+dp[1]) for dp in dpos]
    return [c for c in candidates if
        (c[0] >= 0) and (c[0] < nrows) and
        (c[1] >= 0) and (c[1] < ncols) and
        is_at_most_one_higher(current_elevation, grid[c[0]][c[1]])]

# A-star: https://en.wikipedia.org/wiki/A*_search_algorithm
def a_star(grid, start, goal):
    nrows = len(grid)
    ncols = len(grid[0])

    gscore = {}
    fscore = {}
    for i in range(nrows):
        for j in range(ncols):
            gscore[(i,j)] = nrows * ncols
            fscore[(i,j)] = nrows * ncols

    openset = []
    came_from = {}
    visited = set()
    gscore[start] = 0
    fscore[start] = h(grid, start, goal)
    heapq.heappush(openset, (fscore[start], start))

    while openset:
        _, current = heapq.heappop(openset)
        if current == goal:
            return gscore[current]

        for n in neighbors(grid, current):
            temp_gscore = gscore[current] + 1
            if temp_gscore < gscore[n]:
                came_from[n] = current
                gscore[n] = temp_gscore
                fscore[n] = temp_gscore + h(grid, n, goal)
                if n not in visited:
                    heapq.heappush(openset, (fscore[n], n))
                    visited.add(n)

    # not found
    return nrows*ncols

# find (row,col) indices of occurences of letter in grid
def find(grid, letter):
    found = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == letter:
                found.append((row, col))
    return found

lines = list(fileinput.input())
grid = [list(line.rstrip()) for line in lines]
start = find(grid, 'S')[0]
end = find(grid, 'E')[0]
grid[start[0]][start[1]] = 'a' # remap S to a
grid[end[0]][end[1]] = 'z' # remap E to z

# part 1
pathlen = a_star(grid, start, end)
print(pathlen)

# part 2 (just run a_star a bunch!)
starts = find(grid, 'a')
pathlens = [a_star(grid, x, end) for x in starts]
print(min(pathlens))
