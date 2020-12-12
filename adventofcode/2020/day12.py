import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        l = line.rstrip()
        vals.append((l[0], int(l[1:])))
    return vals

def turn_right(d,val):
    n = int(val/90)
    d += n
    return (d % 4)

def turn_left(d,val):
    return turn_right(d,360-val)

def move(x,y,d,op,val):
    if op == 'W':
        return x-val,y,d
    elif op == 'N':
        return x,y-val,d
    elif op == 'S':
        return x,y+val,d
    elif op == 'E':
        return x+val,y,d
    elif op == 'L':
        return x,y,turn_left(d,val)
    elif op == 'R':
        return x,y,turn_right(d,val)
    elif op == 'F':
        if d == 0: return x,y-val,d
        elif d == 1: return x+val,y,d
        elif d == 2: return x,y+val,d
        else: return x-val,y,d
    else:
        return x,y,d

def part1(vals):
    # d:0(north),1(east),2(south),3(west)
    x,y,d = 0,0,1
    for v in vals:
        x,y,d = move(x,y,d,v[0],v[1])
        # print(x,y,d)
    return (abs(x) + abs(y))

def rotate_right_90(wx,wy):
    return -wy,wx

def rotate_right(wx,wy,val):
    for i in range(int(val/90)):
        wx,wy = rotate_right_90(wx,wy)
    return wx,wy

def rotate_left(wx,wy,val):
    return rotate_right(wx,wy,360-val)

def move2(sx,sy,wx,wy,op,val):
    if op == 'N':
        return sx,sy,wx,wy-val
    elif op == 'S':
        return sx,sy,wx,wy+val
    elif op == 'E':
        return sx,sy,wx+val,wy
    elif op == 'W':
        return sx,sy,wx-val,wy
    elif op == 'F':
        return sx+(wx*val),sy+(wy*val),wx,wy
    elif op == 'L':
        wx,wy = rotate_left(wx,wy,val)
        return sx,sy,wx,wy
    elif op == 'R':
        wx,wy = rotate_right(wx,wy,val)
        return sx,sy,wx,wy
    else:
        return x,y,d

def part2(vals):
    sx,sy = 0,0
    wx,wy = 10,-1
    for v in vals:
        sx,sy,wx,wy = move2(sx,sy,wx,wy,v[0],v[1])
    return (abs(sx) + abs(sy))

vals = parse()
# vals = [('F',10),('N',3),('F',7),('R',90),('F',11)]
# print(vals)
print(part1(list(vals)))
print(part2(list(vals)))
