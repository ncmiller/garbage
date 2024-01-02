import fileinput
import copy

def parse(lines):
    workflows = {}
    parts = []
    is_workflows = True
    for l in lines:
        if l == '':
            is_workflows = False
            continue
        if is_workflows:
            p = l.index('{')
            name = l[:p]
            l = l[p+1:-1] # remove }
            rules_str = l.split(',')
            # print(name,rules_str)
            workflows[name] = rules_str
        else:
            l = l[1:-1] # remove {}
            items = l.split(',')
            part = {
                'x': int(items[0][2:]),
                'm': int(items[1][2:]),
                'a': int(items[2][2:]),
                's': int(items[3][2:]),
            }
            parts.append(part)

    return workflows, parts

def part1(workflows, parts):
    total = 0
    for part in parts:
        flowname = 'in'
        done = False
        while not done:
            if flowname == 'A':
                total += sum(part.values())
                break
            elif flowname == 'R':
                break

            rules = workflows[flowname]
            for r in rules:
                if '<' in r:
                    c = r[0]
                    v = int(r[2:r.index(':')])
                    target = r[r.index(':')+1:]
                    if part[c] < v:
                        flowname = target
                        break
                elif '>' in r:
                    c = r[0]
                    v = int(r[2:r.index(':')])
                    target = r[r.index(':')+1:]
                    if part[c] > v:
                        flowname = target
                        break
                elif r == 'A':
                    done = True
                    total += sum(part.values())
                    break
                elif r == 'R':
                    done = True
                    break
                else:
                    flowname = r
    return total

def all_paths(workflows, start, path, xmas, paths):
    if start == 'A' or start == 'R':
        paths.append((path[:], copy.deepcopy(xmas)))
        return
    rules = workflows[start]
    xmas_map = {'x':0, 'm':1, 'a':2, 's':3}
    for r in rules:
        if '<' in r or '>' in r:
            cond, target = r.split(':')
            path.append((cond, target))
            orig_xmas = copy.deepcopy(xmas)
            if '<' in cond:
                c, val = cond.split('<')
                current = xmas[xmas_map[c]][1]
                val = int(val)
                xmas[xmas_map[c]][1] = min(current, val - 1)
                all_paths(workflows, target, path, xmas, paths)
                xmas = orig_xmas
                current = xmas[xmas_map[c]][0]
                xmas[xmas_map[c]][0] = max(current, val)
            else:
                c, val = cond.split('>')
                current = xmas[xmas_map[c]][0]
                val = int(val)
                xmas[xmas_map[c]][0] = max(current, val + 1)
                all_paths(workflows, target, path, xmas, paths)
                xmas = orig_xmas
                current = xmas[xmas_map[c]][1]
                xmas[xmas_map[c]][1] = min(current, val)
            del path[-1]
        else:
            path.append((None, r))
            all_paths(workflows, r, path, xmas, paths)
            del path[-1]

def part2(workflows):
    # find all paths to A, collecting rules encountered
    paths = []
    xmas = [
        [1, 4000],
        [1, 4000],
        [1, 4000],
        [1, 4000],
    ]
    all_paths(workflows, 'in', [(None, 'in')], xmas, paths)
    paths = [p for p in paths if p[0][-1][1] == 'A']

    total = 0
    for p in paths:
        path_total = 1
        for mn, mx in p[1]:
            path_total *= (mx - mn + 1)
        total += path_total

    return total


lines = [l[:-1] for l in fileinput.input()]
workflows, parts = parse(lines)
print(part1(workflows, parts))
print(part2(workflows))
