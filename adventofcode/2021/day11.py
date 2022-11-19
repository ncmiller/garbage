import fileinput
import copy
import itertools

# Iterate over board, add to flashers if == 10
# Process flashers, add to flash if == 10
def part1(energy_levels):
    n = 10
    iters = 1000
    nflashes = 0
    for it in range(iters):
        flashers = []
        for i in range(n):
            for j in range(n):
                energy_levels[i][j] += 1
                if energy_levels[i][j] == 10:
                    nflashes += 1
                    flashers.append((i,j))
        while flashers:
            i,j = flashers[0]
            flashers = flashers[1:]
            adj = []
            if i > 0 and j > 0:
                adj.append((i-1,j-1))
            if i > 0:
                adj.append((i-1,j))
            if i > 0 and j < (n - 1):
                adj.append((i-1,j+1))
            if j < (n - 1):
                adj.append((i,j+1))
            if i < (n - 1) and j < (n - 1):
                adj.append((i+1,j+1))
            if i < (n - 1):
                adj.append((i+1,j))
            if i < (n - 1) and j > 0:
                adj.append((i+1,j-1))
            if j > 0:
                adj.append((i,j-1))
            for a in adj:
                x,y = a
                energy_levels[x][y] += 1
                if energy_levels[x][y] == 10:
                    nflashes += 1
                    flashers.append((x,y))

        flashes_this_iter = 0
        for i in range(n):
            for j in range(n):
                if energy_levels[i][j] > 9:
                    flashes_this_iter += 1
                    energy_levels[i][j] = 0

        # part 1
        if it == 99:
            print(nflashes)

        # part 2
        if flashes_this_iter == (n * n):
            # not 213 (too low)...off by one, 1-indexed, should have been 214
            print('all flashed on iter', it + 1)
            break

    return nflashes

lines = list(fileinput.input())
energy_levels = [list(map(int, line.rstrip())) for line in lines]
# print(energy_levels)
part1(copy.deepcopy(energy_levels))
