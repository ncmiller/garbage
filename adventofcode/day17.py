step = 328
# step = 3
final = 2017
buf = [0]
current = 0

def insert(x):
    global current
    global buf
    if current == len(buf)-1:
        buf = buf + [x]
    else:
        buf = buf[:current+1] + [x] + buf[current+1:]
    current += 1

def stepforward():
    global current
    current = (current + step) % len(buf)

N = 2018
for i in range(1, N):
    stepforward()
    insert(i)

idx = buf.index(2017)
print buf[idx-5:idx+5]

#---

def stepforward_lite():
    global current, lenbuf
    current = (current + step) % lenbuf

current = 0
lenbuf = 1
N = 50000001
after = 1

for i in range(1, N):
    stepforward_lite()
    if current == 0:
        after = i
    lenbuf += 1
    current += 1

print after
