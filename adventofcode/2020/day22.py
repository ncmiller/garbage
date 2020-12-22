def score(cards):
    score = 0
    for i in range(len(cards)):
        score += ((i+1) * cards[len(cards) - i - 1])
    return score

def part1(p1, p2):
    r = 1
    while p1 and p2:
        # print("[{}] {}, {}".format(r, p1, p2))
        c1,c2 = p1[0], p2[0]
        p1,p2 = p1[1:], p2[1:]
        if c1 > c2:
            p1 += [c1,c2]
        else:
            p2 += [c2,c1]
        r += 1
    if p1:
        # print("p1 wins")
        winner = p1
    else:
        # print("p2 wins")
        winner = p2
    return score(winner)

def round_seen(p1, p2, game_memo):
    return ((tuple(p1), tuple(p2)) in game_memo)

def recursive_combat(p1, p2, level):
    game_memo = set()
    while p1 and p2:
        if round_seen(p1, p2, game_memo):
            # print('[{}] Seen, p1 wins.'.format(level))
            return (1,p1)
        # print(p1,p2)
        game_memo.add((tuple(p1), tuple(p2)))

        c1,c2 = p1[0], p2[0]
        p1,p2 = p1[1:], p2[1:]

        if c1 <= len(p1) and c2 <= len(p2):
            pnum, deck = recursive_combat(list(p1[:c1]), list(p2[:c2]), level+1)
        else:
            if c1 > c2:
                pnum = 1
            else:
                pnum = 2
        if pnum == 1:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]
    if p1:
        # print('[{}] {}, {}. P1 wins'.format(level, p1, p2))
        return (1,p1)
    else:
        # print('[{}] {}, {}. P2 wins'.format(level, p1, p2))
        return (2,p2)

def part2(p1, p2):
    pnum, winning_deck = recursive_combat(p1, p2, 0)
    # print(pnum, winning_deck)
    return score(winning_deck)

# Example of infinite game prevention
# start: [43 19] [2 29 14]
# [19 43 2] [29 14]
# [43 2] [14 29 19]
# [2 43 14] [29 19]
# [43 14] [19 29 2]
# [14 43 19] [29 2]
# [43 19] [2 29 14] <-- same as start, p1 wins

# example
# p1 = [9,2,6,3,1]
# p2 = [5,8,4,7,10]

# infinite recurse example
# p1 = [43, 19]
# p2 = [2, 29, 14]

# input
p1 = [17, 19, 30, 45, 25, 48, 8, 6, 39, 36, 28, 5, 47, 26, 46, 20, 18, 13, 7, 49, 34, 23, 43, 22, 4]
p2 = [44, 10, 27, 9, 14, 15, 24, 16, 3, 33, 21, 29, 11, 38, 1, 31, 50, 41, 40, 32, 42, 35, 37, 2, 12]

print(part1(list(p1), list(p2)))
# not 32340 - too high
print(part2(list(p1), list(p2)))
