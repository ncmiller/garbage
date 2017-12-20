import fileinput
particles = []
for line in fileinput.input():
    particles.append(map(int, line.strip().split()))
orig_particles = particles[:]

# particles = [
#     [-6, 0, 0, 3, 0, 0, 0, 0, 0],
#     [-4, 0, 0, 2, 0, 0, 0, 0, 0],
#     [-2, 0, 0, 1, 0, 0, 0, 0, 0],
#     [3, 0, 0, -1, 0, 0, 0, 0, 0],
# ]

def dist(p):
    # return sum(map(abs, p[:3]))
    return abs(p[0]) + abs(p[1]) + abs(p[2])

def update(p):
    px, py, pz, vx, vy, vz, ax, ay, az = p
    vx += ax
    vy += ay
    vz += az
    px += vx
    py += vy
    pz += vz
    return [px, py, pz, vx, vy, vz, ax, ay, az]

def getmin(dists):
    m = 10000000000000000000000000
    idx = -1
    for i in range(len(dists)):
        if dists[i] < m:
            m = dists[i]
            idx = i
    return m, idx

i = 0
dists = [10000000000 for _ in range(len(particles))]
while i < 1000:
    for j in range(len(particles)):
        particles[j] = update(particles[j])
        dists[j] = dist(particles[j])
    i += 1

m, idx = getmin(dists)
print idx

# ---


particles = orig_particles[:]
i = 0
dists = [10000000000 for _ in range(len(particles))]
alive = [1 for _ in range(len(particles))]
while i < 1000:
    posdict = {}
    for j in range(len(particles)):
        if not alive[j]:
            continue
        particles[j] = update(particles[j])
        dists[j] = dist(particles[j])

        pos = (particles[j][0], particles[j][1], particles[j][2])
        if pos in posdict:
            posdict[pos].append(j)
        else:
            posdict[pos] = [j]

    for parts in posdict.values():
        if len(parts) > 1:
            for p in parts:
                alive[p] = 0

    i += 1

print sum(alive)
