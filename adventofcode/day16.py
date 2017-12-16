progs = list('abcdefghijklmnop')

def spin(x):
    global progs
    progs = progs[-x:] + progs[:-x]

def ex(a, b):
    global progs
    temp = progs[a]
    progs[a] = progs[b]
    progs[b] = temp

def part(p1, p2):
    global progs
    ex(progs.index(p1), progs.index(p2))

with open("day16_input.txt") as f:
    chars = f.read().split(',')

def dance():
    for move in chars:
        if move[0] == 's':
            x = int(move[1:])
            spin(x)
        elif move[0] == 'x':
            a,b = map(int, move[1:].split('/'))
            ex(a, b)
        elif move[0] == 'p':
            p1,p2 = move[1:].split('/')
            part(p1, p2)

dance()
p = ''.join(progs)
print p

# ---

positions = set()
positions.add(p)
ps = [p]

i = 1
while 1:
    dance()
    p = ''.join(progs)

    if p in positions:
        cycle = i
        print ps[1000000000 % cycle - 1]
        break

    positions.add(p)
    ps.append(p)
    i += 1
