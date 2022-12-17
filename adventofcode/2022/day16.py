import fileinput
import re
from itertools import combinations

def parse_line(line):
    p = re.compile('Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
    m = p.match(line)
    g = m.groups()
    return (g[0], int(g[1]), g[-1].split(', '))

def dijkstra(graph, start, end):
    unvisited = set()
    dist = {}

    for node in graph.keys():
        unvisited.add(node)
        dist[node] = 100000
    dist[start] = 0

    while unvisited:
        u = min(unvisited, key=lambda node:dist[node])
        if u == end:
            break
        unvisited.remove(u)
        neighbors = [n for n in graph[u] if n in unvisited]
        for v in neighbors:
            temp_dist = dist[u] + 1
            if temp_dist < dist[v]:
                dist[v] = temp_dist

    return dist[end]

def pressure_released(path, total_minutes):
    released = 0
    for node, minute_opened in path:
        released += flow[node] * (total_minutes - minute_opened)
    return released

scans = [parse_line(line.rstrip()) for line in fileinput.input()]
flow = dict([(scan[0], scan[1]) for scan in scans])
graph = dict([(scan[0], scan[2]) for scan in scans])

# precompute shortest paths between all valves with non-zero flow rate
non_zero_valves = [k for k,v in flow.items() if v > 0 or k == 'AA']
shortest_path = {} # maps (start,end) -> shortest path length
for i in range(len(non_zero_valves)):
    for j in range(i+1, len(non_zero_valves)):
        start = non_zero_valves[i]
        end = non_zero_valves[j]
        shortest_path[(start,end)] = dijkstra(graph, start, end)
        shortest_path[(end,start)] = shortest_path[(start,end)]

# Backtrack algorithm to find all possible valid valve sequences
# Each path is a list of (x,y) where
#       x is the valve name (e.g. 'AA')
#       y is the minute the valve was opened (0 <= y <= total_minutes)
def backtrack(valves, total_minutes, minutes_left, path, paths):
    if minutes_left <= 0 or len(path) == len(valves):
        paths.append(path[:])
        return

    current = path[-1][0]
    path_valves = [p[0] for p in path]
    candidates = [v for v in valves if v not in path_valves]

    for c in candidates:
        # travel to valve and open it
        minutes_left -= (shortest_path[(current,c)] + 1)
        if minutes_left >= 0:
            path.append((c, total_minutes - minutes_left))
        backtrack(valves, total_minutes, minutes_left, path, paths)
        if minutes_left >= 0:
            path.pop()
        minutes_left += (shortest_path[(current,c)] + 1)

def part1():
    paths = []
    path = [('AA', 0)]
    total_minutes = 30
    backtrack(non_zero_valves, total_minutes, total_minutes, path, paths)
    print(max([pressure_released(p, total_minutes) for p in paths]))

def part2():
    # sample best division
    # my_valves = ['AA', 'JJ', 'BB', 'CC']
    # elephant_valves = ['AA', 'DD', 'HH', 'EE']

    # divide valves among me and elephant
    # choose the ones I'll do, and give the rest to the elephant
    non_start_valves = [v for v in non_zero_valves if v != 'AA']
    max_pressure_released = 0
    for num_my_valves in range(1, len(non_start_valves)//2):
        my_valve_combs = list(combinations(non_start_valves, num_my_valves))
        for mv in my_valve_combs:
            my_valves = ['AA'] + list(mv)
            elephant_valves = ['AA'] + [v for v in non_start_valves if v not in my_valves]

            my_paths = []
            elephant_paths = []

            my_path = [('AA', 0)]
            elephant_path = [('AA', 0)]

            total_minutes = 26
            backtrack(my_valves, total_minutes, total_minutes, my_path, my_paths)
            backtrack(elephant_valves, total_minutes, total_minutes, elephant_path, elephant_paths)

            my_best_path = max(my_paths, key=lambda p:pressure_released(p, total_minutes))
            elephant_best_path = max(elephant_paths, key=lambda p:pressure_released(p, total_minutes))

            merged_path = sorted(my_best_path + elephant_best_path, key = lambda p: p[1])[1:]
            max_pressure_released = max(max_pressure_released, pressure_released(merged_path, total_minutes))
    print(max_pressure_released)

part1()
part2()
