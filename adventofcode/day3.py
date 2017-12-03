"""read lines from stdin, split lines on whitespace"""
# import fileinput
# lines = []
# for line in fileinput.input():
#     lines.append([int(x) for x in line.split()])


"""read single number from stdin"""
# num = map(int, raw_input())

"""read one char at a time from named file"""
# with open("dayX_input.txt") as f:
#     for line in f:
#         for ch in line:
#             if ch != '\n':
#                 print ch


""" math-only solution to part 1 (with assist from REPL) """
N = 591

start = (295, 295)

leftcorner = 348691
topleft = 348101
topright = 347511

# 110 right from topleft

# 295 up
# 295 - 110 = 185 left
# 295 + 185 = 480

""" programmatic solution to part 1 """
import math

puzzle_input = 347991
N = int(math.ceil(math.sqrt(347991)))
if N % 2 == 0:
    N += 1

# make a N x N grid (with extra to prevent OOB)
g = [[0 for x in range(N+1)] for x in range(N+1)]

def next_dir(d):
    return (d + 1) % 4

moves = []
d = 0 # 0 = right, 1 = up, 2 = left, 3 = down
for i in range(1, N+1):
    for j in range(i):
        moves.append(d)
    d = next_dir(d)
    for j in range(i):
        moves.append(d)
    d = next_dir(d)

def next_coord(coord, move):
    x, y = coord
    if move == 0:
        return (x, y+1)
    elif move == 1:
        return (x-1, y)
    elif move == 2:
        return (x, y-1)
    else:
        return (x+1, y)

x, y = ((N-1)/2, (N-1)/2)
val = 1
for move in moves:
    g[x][y] = val
    if val == puzzle_input:
        print abs(x-(N-1)/2) + abs(y-(N-1)/2)
        break
    val += 1
    x, y = next_coord((x,y), move)

""" programmatic solution to part 2 """
g = [[0 for x in range(N+2)] for x in range(N+2)]
x, y = ((N-1)/2, (N-1)/2)
g[x][y] = 1

def sum_neighbors(coord):
    x, y = coord
    total = 0
    total += g[x][y-1] # left
    total += g[x+1][y-1] # down-left
    total += g[x+1][y] # down
    total += g[x+1][y+1] # down-right
    total += g[x][y+1] # right
    total += g[x-1][y+1] # up-right
    total += g[x-1][y] # up
    total += g[x-1][y-1] # up-left
    return total

for move in moves:
    x, y = next_coord((x,y), move)
    val = sum_neighbors((x,y))
    if val > puzzle_input:
        print val
        break
    g[x][y] = val
