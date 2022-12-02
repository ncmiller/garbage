import fileinput

player1_move = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

player2_move = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

choice_points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

# values are winning moves against the key
winning_move = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock',
}
losing_move = {v:k for k,v in winning_move.items()}

def round_points_for_p2(p1, p2):
    if p1 == p2:
        return 3
    elif winning_move[p1] == p2:
        return 6
    else:
        return 0

def part1(rounds):
    score = 0
    for r in rounds:
        p1 = player1_move[r[0]]
        p2 = player2_move[r[1]]
        score += choice_points[p2]
        score += round_points_for_p2(p1, p2)
    return score

def part2(rounds):
    score = 0
    for r in rounds:
        p1 = player1_move[r[0]]
        if r[1] == 'X':   # lose
            p2 = losing_move[p1]
        elif r[1] == 'Y': # draw
            p2 = p1
        else:           # 'Z', win
            p2 = winning_move[p1]
        score += choice_points[p2]
        score += round_points_for_p2(p1, p2)
    return score

rounds = [l.rstrip().split(' ') for l in list(fileinput.input())]
print(part1(rounds))
print(part2(rounds))
