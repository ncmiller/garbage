import fileinput

# seeds: [79, 14, 55, 13]
# maps: [[[50, 98, 2], [52, 50, 48]], [[0, 15, 37], ...], ...]

def parse_input(lines):
    lines = [l.strip() for l in lines]
    seeds = [int(seed) for seed in lines[0].split()[1:]]

    maps = []
    m = []

    for i, line in enumerate(lines[2:]):
        if line == '':
            maps.append(m)
            m = []
        elif not line[0].isnumeric():
            continue
        else:
            m.append([int(n) for n in line.split()])

    maps.append(m)

    return seeds, maps

def resolve(seed, maps):
    source = seed
    for m in maps:
        dest = source
        for row in m:
            if (source >= row[1]) and (source < row[1] + row[2]):
                dest = row[0] + (source - row[1])
        # print(source, '->', dest)
        source = dest
    # print('')
    # print('seed', seed, '=', source)
    # print('')
    return source

# (79, 93), (98, 100) -> None
# (79, 93), (50, 98) -> (50, 98), (79, 93)
def range_overlap(r1, r2):
    # print(r1, r2)
    if r1[0] > r2[0]:
        r1, r2 = r2, r1
    if r2[0] <= r1[1]:
        return (r2[0], min(r1[1], r2[1]))
    else:
        return None

def resolve_range(r, maps, level):
    if not maps:
        # print('base', r, min(r))
        return min(r)

    new_source_ranges = []
    for row in maps[0]:
        ro = range_overlap((row[1], row[1] + row[2]), r)
        if ro:
            delta = row[0] - row[1]
            new_source_range = (ro[0] + delta, ro[1] + delta)
            new_source_ranges.append(new_source_range)
            # print(level, r, new_source_range)

    # outside left
    outside_left_ro = range_overlap((-1000000000000, min([r[1] for r in maps[0]]) - 1), r)
    if outside_left_ro:
        # print(level, 'left', outside_left_ro)
        new_source_ranges.append(outside_left_ro)

    # outside right
    outside_right_ro = range_overlap((max([r[1]+r[2] for r in maps[0]]) + 1, 1000000000000), r)
    if outside_right_ro:
        # print(level, 'right', outside_right_ro)
        new_source_ranges.append(outside_right_ro)

    if not new_source_ranges:
        # print(level, 'default', r)
        new_source_ranges.append(r)

    return min([resolve_range(nsr, maps[1:], level + 1) for nsr in new_source_ranges])

def part1(seeds, maps):
    return min([resolve(s, maps) for s in seeds])

def part2(seeds, maps):
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    # print(seed_ranges)
    # print(resolve_range(seed_ranges[0], maps, 0))
    return min([resolve_range(sr, maps, 0) for sr in seed_ranges])
    # min_seed = 10000000000000000
    # for sr in seed_ranges:
    #     min_seed = min(min_seed, min([resolve(s, maps) for s in sr]))
    # return min_seed

lines = [line[:-1] for line in fileinput.input()]
seeds, maps = parse_input(lines)
print(part1(seeds, maps))
print(part2(seeds, maps))
