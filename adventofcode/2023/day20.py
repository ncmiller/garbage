import fileinput
import re
from copy import deepcopy

def part1(modules, return_on_rx_low=False):
    if return_on_rx_low:
        max_iters = 100000000000000
        # n = 1000000000000000000
        n = 100000000
    else:
        max_iters = 10000
        n = 1000
    num_lows = 0
    num_highs = 0
    # states = []
    # states.append(deepcopy(modules))
    for i in range(n):
        sends = []
        sends.append(('button', 0, 'broadcaster'))
        iters = 0
        while sends and iters < max_iters:
            iters += 1
            source, val, dest = sends[0]
            # print(source, val, dest)
            if val:
                num_highs += 1
            else:
                num_lows += 1
            sends = sends[1:]

            if dest not in modules:
                if dest == 'rx' and return_on_rx_low and not val:
                    return i
                else:
                    continue

            modtype, dests, state, inputs = modules[dest]
            if modtype == 'b':
                for d in dests:
                    sends.append((dest, 0, d))
            elif modtype == '%':
                if not val:
                    modules[dest][2] ^= 1
                    for d in dests:
                        sends.append((dest, modules[dest][2], d))
            elif modtype == '&':
                modules[dest][3][source] = val
                all_high = all(modules[dest][3].values())
                if dest == 'bn':
                    count = sum(modules[dest][3].values())
                    if count > 1:
                        print(count, i, iters, modules[dest][3].values())
                for d in dests:
                    if all_high:
                        sends.append((dest, 0, d))
                    else:
                        sends.append((dest, 1, d))
            else:
                assert(False)

            # test = 'vt'
            # s = ''.join([str(x) for x in modules[test][3].values()])
            # val = int(s,2)
            # val = sum(modules[test][3].values())
            # if val == len(modules[test][3].values()):
            #     print(i, iters)
        # states.append(deepcopy(modules))

    # print(num_highs, num_lows)
    # for i, state in enumerate(states):
    #     # print('----',i,'----')
    #     for k,v in state.items():
    #         if k == 'bn':
    #             for k1,v1 in v[3].items():
    #                 if v1 > 0:
    #                     print(i, k, v)

    return num_highs * num_lows

lines = [l[:-1] for l in fileinput.input()]
modules = {} # indexed by name
for l in lines:
    result = re.search(r"(.+) -> (.+)", l)
    module, dests = result.groups()
    modtype = module[0]
    modname = module[1:]
    if modtype == 'b':
        modname = 'broadcaster'
    dests = dests.replace(' ', '').split(',')
    modules[modname] = [modtype, dests, 0, {}]

for name, m in modules.items():
    for dest in m[1]:
        if dest in modules:
            modules[dest][3][name] = 0
modules_copy = deepcopy(modules)

# for k,m in modules.items():
#     print(k,m)
print(part1(modules, False))
# print(part1(modules_copy, True))

# For part 2: did it manually with debug logs.
#
# The 4 major dependencies of rx are conjunction nodes vt, dq, qt, and nl
# For each of these, I logged the button cycle when all inputs were 1.
# These button cycles occurred at the same interval (e.g. nl every 3823 cycles),
# so it was just a matter of using an online LCM calculator of all the node cycles.
