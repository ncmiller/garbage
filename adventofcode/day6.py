"""read lines from stdin, split lines on whitespace"""
import fileinput
import re
lines = []
banks = map(int, raw_input().split())

# banks = [0,2,7,0]
configs = []
configs.append(banks[:])
dist = 0
N = len(banks)
while True:
    m = max(banks)
    i = banks.index(m)
    banks[i] = 0
    while m:
        i = (i + 1) % N
        banks[i] += 1
        m -= 1
    dist += 1
    if banks in configs:
        ans = abs(configs.index(banks) - dist)
        break
    configs.append(banks[:])

print dist
print ans
