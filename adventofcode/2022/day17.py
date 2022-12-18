import fileinput

PIECES = [
    [
        '####'
    ],
    [
        '.#.',
        '###',
        '.#.'
    ],
    [
        '..#',
        '..#',
        '###'
    ],
    [
        '#',
        '#',
        '#',
        '#',
    ],
    [
        '##',
        '##',
    ],
]
BLANK = '.......'

def render_piece(board, pos, piece_index):
    piece = PIECES[piece_index]
    height = len(piece)
    width = len(piece[0])

    for row in range(height):
        for col in range(width):
            board[pos[0] - row][pos[1] + col] = piece[row][col]

def would_collide(board, pos, piece_index):
    piece = PIECES[piece_index]
    height = len(piece)
    width = len(piece[0])

    nlines_to_add = pos[0] - len(board) + 1
    for _ in range(nlines_to_add):
        board.append(list(BLANK))

    for row in range(height):
        for col in range(width):
            piece_val = piece[row][col]
            if pos[0] - row < 0: # bottom of board
                return True
            if pos[1] < 0: # left wall
                return True
            if pos[1] + width - 1 >= 7: # right wall
                return True
            board_val = board[pos[0] - row][pos[1] + col]
            if piece_val == '#' and board_val == '#': # piece collision
                return True

    return False

def print_board(board):
    for line in reversed(board):
        print(''.join(line))

def board_contour(board):
    contour = []
    for col in range(7):
        blanks = 0
        for row in reversed(range(len(board))):
            if board[row][col] == '#':
                break
            else:
                blanks += 1
        contour.append(blanks)
    return contour

def part1(jets, N):
    board = []
    jet_index = 0
    states_seen = {}
    board_height = []
    cycle_end = 0
    cycle_start = 0
    for i in range(N):
        piece_index = i % len(PIECES)
        top_of_board = len(board) - 1
        piece = PIECES[piece_index]
        piece_pos = [top_of_board + 4 + len(piece) - 1, 2]

        while True:
            # jet move
            jet_move = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)
            temp_pos = piece_pos[:]
            if jet_move == '<':
                temp_pos[1] -= 1
            else:
                temp_pos[1] += 1
            if not would_collide(board, temp_pos, piece_index):
                piece_pos = temp_pos

            # move down
            temp_pos = [piece_pos[0] - 1, piece_pos[1]]
            if not would_collide(board, temp_pos, piece_index):
                piece_pos = temp_pos
            else:
                render_piece(board, piece_pos, piece_index)
                break

        # Trim blank lines at the top of the stack
        while board[-1] == list(BLANK):
            board.pop()

        state = tuple(board_contour(board) + [piece_index, jet_index])
        if state in states_seen:
            cycle_start = states_seen[state]
            cycle_end = i
            board_height.append(len(board))
            break
        else:
            states_seen[state] = i
            board_height.append(len(board))

    cycle_length = cycle_end - cycle_start
    board_grows_each_cycle = board_height[cycle_end] - board_height[cycle_start]
    num_cycles = (N - cycle_start) // cycle_length
    end_cycles = (N - cycle_start) % cycle_length

    beginning = board_height[cycle_start]
    middle = num_cycles * board_grows_each_cycle
    end = board_height[cycle_start + end_cycles - 1] - board_height[cycle_start]

    return beginning + middle + end

jets = list(fileinput.input())[0].rstrip()

print(part1(jets, 2022))
print(part1(jets, 1000000000000))
