import fileinput
import heapq

# Heuristic function - manhattan distance to goal
def h(grid, pos):
    nrows = len(grid)
    ncols = len(grid[0])
    goal = (nrows-1,ncols-1)
    return (goal[0] - pos[0]) + (goal[1] - pos[1])

def neighbors(grid, n):
    nrows = len(grid)
    ncols = len(grid[0])
    dpos = [(-1,0),(1,0),(0,-1),(0,1)]
    candidates = [(n[0]+dp[0],n[1]+dp[1]) for dp in dpos]
    candidates = [c for c in candidates if
            (c[0] >= 0) and
            (c[0] < nrows) and
            (c[1] >= 0) and
            (c[1] < ncols)]
    return candidates

# A-star: https://en.wikipedia.org/wiki/A*_search_algorithm
def part1(grid):
    nrows = len(grid)
    ncols = len(grid[0])

    gscore = {}
    fscore = {}
    for i in range(nrows):
        for j in range(ncols):
            gscore[(i,j)] = 10 * nrows * ncols
            fscore[(i,j)] = 10 * nrows * ncols

    start = (0,0)
    goal = (nrows-1,ncols-1)
    openset = []
    visited = set()
    gscore[start] = 0
    fscore[start] = h(grid, start)
    heapq.heappush(openset, (start, fscore[start]))

    while openset:
        current, _ = heapq.heappop(openset)
        if current == goal:
            return gscore[current]

        for n in neighbors(grid, current):
            temp_gscore = gscore[current] + grid[n[0]][n[1]]
            if temp_gscore < gscore[n]:
                gscore[n] = temp_gscore
                fscore[n] = temp_gscore + h(grid, n)
                if n not in visited:
                    heapq.heappush(openset, (n, fscore[n]))
        visited.add(n)

    return -1

def expand_grid(grid):
    nsuperrows = 5
    nsupercols = 5
    nrows = len(grid)
    ncols = len(grid[0])
    new_grid = [[0 for _ in range(nsupercols * ncols)] for _2 in range(nsuperrows*nrows)]
    for superrow in range(nsuperrows):
        for supercol in range(nsupercols):
            for row in range(nrows):
                for col in range(ncols):
                    r = superrow * nrows + row
                    c = supercol * ncols + col
                    new_grid[r][c] = grid[row][col] + superrow + supercol
                    while new_grid[r][c] > 9:
                        new_grid[r][c] = new_grid[r][c] - 9
    # print(new_grid[0])
    # print(new_grid[-1])
    return new_grid


lines = list(fileinput.input())
grid = [list(map(int, list(line.rstrip()))) for line in lines]
print(part1(grid[:]))
print(part1(expand_grid(grid[:])))
