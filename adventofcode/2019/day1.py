import fileinput

vals = map(int, fileinput.input())
total = 0.0
for v in vals:
    module_total = 0.0
    mass = int(v / 3.0) - 2
    print("mass = {}".format(mass))
    module_total += mass
    while (mass > 0):
        mass = int(mass / 3.0) - 2
        if mass > 0:
            print("mass = {}".format(mass))
            module_total += mass
    print("module_total = {}".format(module_total))
    total += module_total
print(total)
