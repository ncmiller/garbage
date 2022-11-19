import fileinput

def is_lower(s):
    return s[0] >= 'a' and s[0] <= 'z'

def is_upper(s):
    return s[0] >= 'A' and s[0] <= 'Z'

def path_has_double_small(p):
    seen = set()
    for s in p:
        if is_lower(s) and s in seen:
            return True
        seen.add(s)
    return False

# recursive, pass visited down, increment npaths if reached end
# if nowhere to go, dead end, return
def search(adj, path, solutions, depth):
    last = path[-1]
    if last == 'end':
        solutions.append(path[:])
        return

    candidates = adj[last]
    for c in candidates:
        # part 1
        # if is_upper(c) or (is_lower(c) and c not in path):

        if is_upper(c) or \
           (is_lower(c) and c not in path) or \
           (is_lower(c) and not path_has_double_small(path) and c != 'start' and c != 'end'):
            path.append(c)
            # print('push', path, depth)
            search(adj, path, solutions, depth + 1)
            path.pop()
            # print('pop', path, depth)
    # print('end',depth)

def part1(pairs):
    adj = {}
    for a,b in pairs:
        if a in adj:
            adj[a].append(b)
        else:
            adj[a] = [b]

        if b in adj:
            adj[b].append(a)
        else:
            adj[b] = [a]
    # print(adj)
    solutions = []
    path = ['start']
    search(adj, path, solutions, 0)
    print(len(solutions))
    # print(solutions)

lines = list(fileinput.input())
pairs = [line.rstrip().split('-') for line in lines]
# print(pairs)
print(part1(pairs))
