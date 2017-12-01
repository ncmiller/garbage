def next(x, n):
    return (x + 1) % n

def halfway_around(x, n):
    return (x + n/2) % n

def sum_list(list, f):
    N = len(list)
    return sum([list[i] for i in range(N) if list[i] == list[f(i, N)]])

puzzle_input = raw_input()
digits = map(int, puzzle_input)
part1 = sum_list(digits, next)
part2 = sum_list(digits, halfway_around)

print part1, part2
