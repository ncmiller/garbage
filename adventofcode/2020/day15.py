def part1(vals, last_turn):
    spoken_turn = {}
    turn = 1
    for v in vals:
        spoken_turn[v] = turn
        turn += 1

    last_spoken = vals[-1]
    last_new = True
    while turn <= last_turn:
        if last_new:
            speak = 0
        else:
            speak = (turn - 1) - spoken_turn[last_spoken]
        spoken_turn[last_spoken] = turn-1

        # print(turn, last_spoken, last_new, speak)
        last_new = (speak not in spoken_turn)
        last_spoken = speak
        # print(spoken_turn)
        turn += 1
    return last_spoken

def part2(vals):
    return part1(vals, 30000000)


test_cases = [
    # [0,3,6],
    # [1,3,2],
    # [2,1,3],
    # [1,2,3],
    # [2,3,1],
    # [3,2,1],
    # [3,1,2],
    [0,5,4,1,10,14,7],
]

for tc in test_cases:
    print(part1(tc, 2020))

print('----------------')

for tc in test_cases:
    print(part2(tc))
