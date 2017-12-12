"""read lines from stdin, split lines on whitespace"""
import fileinput
pipes = {}
for line in fileinput.input():
    programs = map(int, line.split())
    pipes[programs[0]] = programs[1:]
# print pipes

connected = [0]
group = set()
while connected:
    p = connected.pop(0)
    group.add(p)
    for ps in pipes[p]:
        if ps not in group:
            connected.append(ps)
print len(group)


groups = []
for p in pipes.keys():
    connected = [p]
    group = set()
    while connected:
        p = connected.pop(0)
        group.add(p)
        for ps in pipes[p]:
            if ps not in group:
                connected.append(ps)
    if group not in groups:
        groups.append(group)
print len(groups)
