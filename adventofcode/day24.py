import fileinput
components = []
for line in fileinput.input():
    components.append(map(int, line.split('/')))

def strength(bs):
    return sum([b[0]+b[1] for b in bs])

def other(c, next):
    if c[0] == next: return c[1]
    else: return c[0]

def strongest(bs, cs, next, d):
    valid = [c for c in components if next in c]
    if not valid:
        return strength(bs), bs

    best = (0,[])
    for v in valid:
        cs.remove(v)
        bs.append(v)
        o = other(v, next)
        s, br = strongest(bs, cs, o, d+1)
        if s > best[0]:
            best = (s, br[:])
        cs.append(v)
        bs.remove(v)

    return best

def longest(bs, cs, next):
    valid = [c for c in components if next in c]
    if not valid: return strength(bs), len(bs), bs

    best = (0,0,[])
    for v in valid:
        cs.remove(v)
        bs.append(v)
        o = other(v, next)
        s, l, br = longest(bs, cs, o)
        if l > best[1] or (l == best[1] and s > best[0]):
            best = (s,l,br[:])
        cs.append(v)
        bs.remove(v)

    return best

s, br = strongest([], components, 0, 0)
print s, br

s, l, br = longest([], components, 0)
print s, br
