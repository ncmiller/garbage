Af = 16807
Bf = 48271
div = 2147483647 # bottom 31 bits

# A = 65
# B = 8921
A = 512
B = 191

N = 40000000

match = 0
for i in range(N):
    A *= Af
    B *= Bf
    A = A % div
    B = B % div
    if A&0xffff == B&0xffff:
        match += 1
print match

# ----

A = 512
B = 191

match = 0
Av = []
Bv = []
for i in range(N):
    A *= Af
    B *= Bf
    A = A % div
    B = B % div
    if A&0x3 == 0:
        Av.append(A)
    if B&0x7 == 0:
        Bv.append(B)

r = min(len(Av), len(Bv))
for i in range(r):
    if i>= 5000000:
        break
    if Av[i]&0xffff == Bv[i]&0xffff:
        match += 1

print match

