import fileinput
from collections import Counter

#
# Super-slow solution today, but it works
#

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append(l)
    return vals

def print_board(board):
    # print('rows',len(vals))
    # print('cols',len(vals[0]))
    for row in board:
        print(row)

def num_occupied(board):
    n = 0
    for row in board:
        for seat in row:
            if seat == '#':
                n += 1
    return n

def num_adjacent_occupied(board, x, y):
    max_y = len(board) - 1
    max_x = len(board[0]) - 1

    # list of (x,y) adjacent points
    check = [
        (x-1,y),
        (x+1,y),
        (x,y-1),
        (x,y+1),
        (x-1,y-1),
        (x+1,y+1),
        (x-1,y+1),
        (x+1,y-1),
    ]
    n = 0
    for ax,ay in check:
        if ax >= 0 and ax <= max_x and ay >= 0 and ay <= max_y:
            if board[ax][ay] == '#':
                n += 1
    return n

def in_bounds(x, y, max_x, max_y):
    return (x >= 0 and y >= 0 and x <= max_x and y <= max_y)

def look_for_occupied(board, x, y, dx, dy):
    max_y = len(board) - 1
    max_x = len(board[0]) - 1
    ax,ay = x,y
    while True:
        ax += dx
        ay += dy
        if not in_bounds(ax,ay,max_x,max_y):
            return False
        if board[ax][ay] == '#':
            return True
        elif board[ax][ay] == 'L':
            return False

def num_visibly_occupied(board, x, y):
    n = 0
    if look_for_occupied(board,x,y,-1,0): n += 1  # left
    if look_for_occupied(board,x,y,1,0): n += 1   # right
    if look_for_occupied(board,x,y,0,-1): n += 1  # up
    if look_for_occupied(board,x,y,0,1): n += 1   # down
    if look_for_occupied(board,x,y,-1,-1): n += 1 # up-left
    if look_for_occupied(board,x,y,1,-1): n += 1  # up-right
    if look_for_occupied(board,x,y,-1,1): n += 1  # down-left
    if look_for_occupied(board,x,y,1,1): n += 1  # down-right
    return n

def part1(board):
    nrows = len(board)
    ncols = len(board[0])

    iters = 0
    state_changes = 1
    while state_changes != 0:
        # print('---------------')
        # print_board(board)

        new_board = []
        state_changes = 0
        for y in range(nrows):
            new_row = ''
            for x in range(ncols):
                n = num_adjacent_occupied(board, x, y)
                if board[x][y] == 'L' and n == 0:
                    state_changes += 1
                    new_row += '#'
                elif board[x][y] == '#' and n >= 4:
                    state_changes += 1
                    new_row += 'L'
                else:
                    new_row += board[x][y]
            new_board.append(new_row)
        # copy new board to board
        board = [x[:] for x in new_board]
        iters += 1

    print('stabilized after {} rounds'.format(iters - 1))
    return num_occupied(board)

def part2(board):
    nrows = len(board)
    ncols = len(board[0])

    iters = 0
    state_changes = 1
    while state_changes != 0:
        # print('---------------')
        # print_board(board)

        new_board = []
        state_changes = 0
        for y in range(nrows):
            new_row = ''
            for x in range(ncols):
                n = num_visibly_occupied(board, x, y)
                if board[x][y] == 'L' and n == 0:
                    state_changes += 1
                    new_row += '#'
                elif board[x][y] == '#' and n >= 5:
                    state_changes += 1
                    new_row += 'L'
                else:
                    new_row += board[x][y]
            new_board.append(new_row)
        # copy new board to board
        board = [x[:] for x in new_board]
        iters += 1

    print('stabilized after {} rounds'.format(iters - 1))
    return num_occupied(board)

vals = parse()
# print(vals)
print(part1(list(vals)))
print(part2(list(vals)))
