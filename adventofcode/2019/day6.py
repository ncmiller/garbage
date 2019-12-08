import fileinput

def part1(orbits):
    num_orbits = 0
    for planet in orbits.keys():
        if planet == 'COM':
            continue
        orbiter = planet
        while True:
            orbiting = orbits[orbiter]
            num_orbits += 1
            if orbiting == 'COM':
                break
            orbiter = orbiting
    print(num_orbits)

def get_orbits(orbits, planet):
    planets = []
    orbiter = planet
    while True:
        orbiting = orbits[orbiter]
        planets.append(orbiting)
        if orbiting == 'COM':
            break
        orbiter = orbiting
    return planets

def part2(orbits):
    you_orbits = get_orbits(orbits, 'YOU')[::-1]
    san_orbits = get_orbits(orbits, 'SAN')[::-1]
    # print(you_orbits)
    # print(san_orbits)
    idx = 0
    while you_orbits[idx] == san_orbits[idx]:
        idx += 1
    print(len(you_orbits[:-idx]) + len(san_orbits[:-idx]))

orbits = {}
for line in fileinput.input():
    first, second = line.rstrip().split(')')
    orbits[second] = first

part1(orbits)
part2(orbits)
