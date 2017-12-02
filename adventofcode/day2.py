import fileinput

rows = []
for line in fileinput.input():
    rows.append([int(x) for x in line.split()])

# part 1
total = 0
for row in rows:
    total += (max(row) - min(row))

print(total)

# part 2
total = 0
for row in rows:
    for i in range(len(row)-1):
        for j in range(i+1, len(row)):
            x, y = row[i], row[j]
            if x % y == 0:
                total += x / y
                break
            if y % x == 0:
                total += y / x
                break

print(total)
