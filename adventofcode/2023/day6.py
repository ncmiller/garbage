import fileinput
import math

def part1(times, distances):
    prod_beats = 1
    for t, d in zip(times, distances):
        beats = 0
        for ms in range(0, t):
            dist = ms * (t - ms)
            if dist > d:
                beats += 1
        prod_beats *= beats
    return prod_beats

def part2(time, distance):
    # x * (t - x) > d, find x
    # (-1)x**2 + tx - d > 0
    # quadratic formula
    s = math.sqrt(time**2 - 4*distance)
    lo = math.ceil((-time + s) / (-2))
    hi = math.floor((-time - s) / (-2))
    return hi - lo + 1

lines = [line[:-1] for line in fileinput.input()]
times = list(map(int, lines[0].split()[1:]))
distances = list(map(int, lines[1].split()[1:]))
time_nospace = int(''.join(lines[0].split()[1:]))
dist_nospace = int(''.join(lines[1].split()[1:]))
print(part1(times, distances))
print(part2(time_nospace, dist_nospace))
