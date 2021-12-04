import fileinput

def score(board, marker, n):
    s = 0
    for r in range(5):
        for c in range(5):
            if marker[r][c] == 0:
                s += board[r][c]
    return s * n

def has_win(marker):
    for r in range(5):
        if marker[r] == [1,1,1,1,1]:
            return True

    for c in range(5):
        col = [marker[r][c] for r in range(5)]
        if col == [1,1,1,1,1]:
            return True

    return False

def mark(board, marker, val):
    for r in range(5):
        for c in range(5):
            if board[r][c] == val:
                marker[r][c] = 1
                return has_win(marker)
    return False

def part1(nums, boardlines):
    boards = []
    markers = []
    nboards = int(len(boardlines) / 6)
    for i in range(nboards):
        board = [[0] * 5] * 5
        for r in range(5):
            line = boardlines[1 + (6*i) + r]
            board[r] = list(map(int, line.split()))
        boards.append(board)
        markers.append([[0 for _ in range(5)] for _ in range(5)])
    # print(boards[0])
    # print(markers[0])
    # print(nums)

    for n in nums:
        for bi in range(len(boards)):
            is_winner = mark(boards[bi], markers[bi], n)
            if is_winner:
                # print(boards[bi])
                # print(markers[bi])
                return score(boards[bi], markers[bi], n)
    return -1

def part2(nums, boardlines):
    boards = []
    markers = []
    nboards = int(len(boardlines) / 6)
    for i in range(nboards):
        board = [[0] * 5] * 5
        for r in range(5):
            line = boardlines[1 + (6*i) + r]
            board[r] = list(map(int, line.split()))
        boards.append(board)
        markers.append([[0 for _ in range(5)] for _ in range(5)])

    has_won = set()
    board_scores = {}
    for n in nums:
        for bi in range(len(boards)):
            if bi in has_won:
                continue
            is_winner = mark(boards[bi], markers[bi], n)
            if is_winner:
                has_won.add(bi)
                board_scores[bi] = score(boards[bi], markers[bi], n)
                if len(board_scores) == nboards:
                    return board_scores[bi]

    return -1

vals = list(fileinput.input())
nums = list(map(int, vals[0].split(',')))
boardlines = vals[1:]
print(part1(nums, boardlines))
print(part2(nums, boardlines))

