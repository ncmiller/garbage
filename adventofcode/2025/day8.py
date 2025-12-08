import fileinput
import math

def dist(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

def part1_and_part2(lines):
    # dict of (dist, p1, p2), sort it by dist, process first X
    # list of sets of points, the circuits, build up incrementally
    dists = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            dists.append((dist(lines[i], lines[j]), lines[i], lines[j]))
    dists = sorted(dists)

    circuits = dict()
    for p in lines:
        circuits[p] = set([p])
    # print(circuits)

    circuits = []
    for i in range(len(dists)):
        d, p1, p2 = dists[i]

        # find p1 and p2 in existing circuits
        # print(p1, p2)
        p1_index = -1
        p2_index = -1
        for j in range(len(circuits)):
            if p1 in circuits[j]:
                p1_index = j
            if p2 in circuits[j]:
                p2_index = j

        # if both exist, merge them and delete the other
        # if only p1 exists, add p2
        # if only p2 exists, add p1
        # if neither exist, add [p1, p2]
        if p1_index != -1 and p2_index != -1:
            if p1_index != p2_index:
                merged = circuits[p1_index].union(circuits[p2_index])
                circuits[p1_index] = merged
                circuits[p2_index] = set()
        elif p1_index != -1:
            circuits[p1_index].add(p2)
            if len(circuits[p1_index]) == len(lines):
                print('complete', p1, p2, p1[0]*p2[0])
                return
        elif p2_index != -1:
            circuits[p2_index].add(p1)
            if len(circuits[p2_index]) == len(lines):
                print('complete', p1, p2, p1[0]*p2[0])
                return
        else:
            circuits.append(set([p1, p2]))

#         for c in circuits:
#             print(c)
#         print('---')

        if i == 999:
            circuits.sort(reverse=True, key=lambda x: len(x))
            # for c in circuits:
            #     print(c)
            product = 1
            for circuit in circuits[:3]:
                if len(circuit) > 0:
                    product *= len(circuit)
            print(product)

def part2(lines):
    pass

lines = [tuple(map(int, l[:-1].split(','))) for l in fileinput.input()]
# print(lines)
part1_and_part2(lines)
