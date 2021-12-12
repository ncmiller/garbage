import fileinput
import copy
import itertools

def is_one(digit): return len(digit) == 2
def is_four(digit): return len(digit) == 4
def is_seven(digit): return len(digit) == 3
def is_eight(digit): return len(digit) == 7

def parse(lines):
    displays = []
    for line in lines:
        signals, outputs = line.rstrip().replace(' | ', '|').split('|')
        signals = signals.split(' ')
        outputs = outputs.split(' ')
        displays.append((signals, outputs))
    return displays

def part1(displays):
    num_1478 = 0
    for d in displays:
        signals, outputs = d
        num_1478 += len(
            [o for o in outputs
                if is_one(o) or is_four(o) or is_seven(o) or is_eight(o)])
    return num_1478

def generate_permutation_map(permutation):
    d = {}
    order = "abcdefg"
    for i in range(len(order)):
        d[permutation[i]] = order[i]
    return d

def part2(displays):
    # 2-seg: 1
    # 3-seg: 7
    # 4-seg: 4
    # 5-seg: 2,3,5
    # 6-seg: 0,6,9
    # 7-seg: 8

    # idea: find digits that are only different by one segment
    # (7,1): unique segment is top
    # (9,8): unique segment is bottom left
    # (6,8): unique segment is top right
    # (3,9): unique segment is top left

    # (7,1): unique seg is top (known: [top], [1,4,7,8]))
    # Find 6-seg digit with two unique relative to 4. This is a 9, and the non-top seg is the bottom. (known: [top, bot], [1,4,7,8,9])
    # Bottom left is unique between (9,8) (known: [top, bot, botL], [1,4,7,8,9])
    # Find 6-seg digit with one unique relative to 9. This is a 0, and

    # idea: brute-force, there's only 7! possibilities for each display
    permutations = list(itertools.permutations("abcdefg"))
    segment_to_digit_map = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }
    normal_order = "abcdefg"
    display_total = 0
    for d in displays:
        signals, outputs = d
        display_permutation = ""

        # Test only
        # permutations = ["deafgbc"]
        # signals = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]

        for p in permutations:
            # if not a digit or not a unique digit, continue
            # when len(seen_digits) == 10, return
            pmap = generate_permutation_map(p)
            seen = set()

            # Convert signal to normalized segment order using permutation
            invalid = False
            found = False
            for s in signals:
                normalized_signal = ''.join(sorted([pmap[c] for c in s]))
                # print(normalized_signal)
                if normalized_signal not in segment_to_digit_map:
                    # print("not a num:", s, pmap, normalized_signal)
                    invalid = True
                    break
                digit = segment_to_digit_map[normalized_signal]
                if digit in seen:
                    # print("already seen: {}".format(digit))
                    invalid = True
                    break
                seen.add(digit)
                if len(seen) == 10:
                    display_permutation = p
                    found = True
                    break
            if invalid:
                continue
            if found:
                break;
        assert(display_permutation != "")
        # print(d, display_permutation)
        final_pmap = generate_permutation_map(p)

        # Convert outputs to digits
        num_str = ""
        for o in outputs:
            normalized_output = ''.join(sorted([final_pmap[c] for c in o]))
            digit = segment_to_digit_map[normalized_output]
            num_str += str(digit)
        display_total += int(num_str)
    return display_total


lines = list(fileinput.input())
displays = parse(lines)
print(part1(copy.deepcopy(displays)))
print(part2(copy.deepcopy(displays)))
