import fileinput
from collections import Counter

def parse():
    vals = []
    for line in fileinput.input():
        vals.append(line[:-1])
    return vals

def bsp_to_row_col(bsp):
    frontback = bsp[:7]
    leftright = bsp[7:]
    row = 0
    for i in range(7):
        if frontback[i] == 'B':
            row += (2 ** (7 - i - 1))
    col = 0
    for i in range(3):
        if leftright[i] == 'R':
            col += (2 ** (3 - i - 1))
    return row,col

def seat_id(row, col):
    return (8 * row) + col

def part1(vals):
    seat_ids = []
    for bsp in vals:
        row,col= bsp_to_row_col(bsp)
        seat_ids.append(seat_id(row,col))
    # print(seat_ids)
    return max(seat_ids)

def part2(vals):
    seat_ids = []
    for bsp in vals:
        row,col= bsp_to_row_col(bsp)
        seat_ids.append(seat_id(row,col))
    available = []
    for row in range(2**7):
        for col in range(2**3):
            sid = seat_id(row,col)
            if sid not in seat_ids:
                available.append((sid,row,col))
    candidates = []
    for a in available:
        sid,row,col = a
        valid = (row != 0) and (row != 63)
        if valid and (sid+1) in seat_ids and (sid-1) in seat_ids:
            return sid
    return -1


# FBFBBFF RLR
# 0101100 101
# 44      5
# Row = 44, Col = 5
# SeatID = 8*row + col = 357
# Find highest seat ID

vals = parse()
# print(vals)
# print(len(vals))
print(part1(vals))
print(part2(vals))
