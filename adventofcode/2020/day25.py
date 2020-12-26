# (7 ^ loop_size) mod 20201227
def find_loop_size(subject, target):
    n = 1
    loop_size = 1
    while True:
        n = (n * subject) % 20201227
        if n == target:
            return loop_size
        loop_size += 1
    return -1

def transform(subject, loop_size):
    n = 1
    for i in range(loop_size):
        n = (n * subject) % 20201227
    return n

def part1(card_pub, door_pub):
    subject = 7

    card_loop_size = find_loop_size(subject, card_pub)
    door_loop_size = find_loop_size(subject, door_pub)

    # print(card_loop_size, door_loop_size)

    encr_key1 = transform(door_pub, card_loop_size)
    encr_key2 = transform(card_pub, door_loop_size)
    assert(encr_key1 == encr_key2)

    return encr_key1

def part2(card_pub, door_pub):
    return 0

# Sample
# card_pub = 5764801
# door_pub = 17807724

# Input
card_pub = 2959251
door_pub = 4542595

print(part1(card_pub, door_pub))
print(part2(card_pub, door_pub))
