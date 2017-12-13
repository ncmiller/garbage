class Firewall:
    def __init__(self, layer, depth):
        self.layer = layer
        self.depth = depth
        depth_lookup = list(range(depth))
        self.lookup = depth_lookup + list(reversed(depth_lookup[1:-1]))
        self.index = 0

    def reset(self):
        self.index = 0

    def advance(self, amount):
        self.index = (self.index + amount) % len(self.lookup)
        return self.lookup[self.index]


"""read lines from stdin, split lines on whitespace"""
import fileinput
firewalls = {}
for line in fileinput.input():
    layer, depth = map(int, line.split())
    firewalls[layer] = Firewall(layer, depth)

def severity(packet_idx):
    if packet_idx in firewalls:
        f = firewalls[packet_idx]
        if f.index == 0:
            return f.layer * f.depth, True
    return 0, False

total_severity = 0
packet_idx = -1
for picosecond in range(93):
    packet_idx += 1
    s, _ = severity(packet_idx)
    total_severity += s
    for _,f in firewalls.items():
        f.advance(1)

print total_severity

# There is a smarter way to do this, but brute force works!
# This takes several minutes to find the answer of 3861798
for delay in range(1,10000000):
    # if delay % 1000 == 0:
    #     print 'delay = {}'.format(delay)
    for _,f in firewalls.items():
        f.reset()

    for _,f in firewalls.items():
        f.advance(delay)

    packet_idx = -1
    caught = False
    for picosecond in range(93):
        packet_idx += 1
        _, caught = severity(packet_idx)
        if caught:
            break
        for _,f in firewalls.items():
            f.advance(1)

    if not caught:
        print delay
        break
