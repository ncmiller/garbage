import fileinput
from collections import Counter
from functools import cmp_to_key


def hand_strength(hand):
    c = Counter(hand)

    if len(c) == 5:
        return 1 # high card
    elif len(c) == 4:
        return 2 # one pair
    elif len(c) == 3:
        if c.most_common(1)[0][1] == 2:
            return 3 # two pair
        else:
            return 4 # three of a kind
    elif len(c) == 2:
        if c.most_common(1)[0][1] == 3:
            return 5 # full house
        else:
            return 6 # four of a kind
    else:
        assert(len(c) == 1)
        return 7 # five of a kind


class Hand:
    def __init__(self, hand, bid, use_jokers=False):
        self.hand = hand
        self.bid = bid

        if use_jokers:
            joker_vals_to_try = []
            for c in hand:
                if c != 'J':
                    joker_vals_to_try.append(c)
            if not joker_vals_to_try:
                joker_vals_to_try = ['A'] # special case: JJJJJ
            self.strength = max([hand_strength(hand.replace('J', jv)) for jv in joker_vals_to_try])
        else:
            self.strength = hand_strength(hand)

def compare_hands(h1, h2):
    if h1.strength < h2.strength:
        return -1
    elif h1.strength > h2.strength:
        return 0
    else:
        for i in range(5):
            if cards.index(h1.hand[i]) < cards.index(h2.hand[i]):
                return -1
            elif cards.index(h1.hand[i]) > cards.index(h2.hand[i]):
                return 1
        return 0

def total_score(hands):
    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))
    # for h in sorted_hands:
    #     print(h.__dict__)
    return(sum([h.bid * (i+1) for i,h in enumerate(sorted_hands)]))

lines = [line[:-1].split() for line in fileinput.input()]

cards = '23456789TJQKA'
p1_hands = [Hand(x[0], int(x[1])) for x in lines]
print(total_score(p1_hands))

cards = 'J23456789TQKA'
p2_hands = [Hand(x[0], int(x[1]), True) for x in lines]
print(total_score(p2_hands))
