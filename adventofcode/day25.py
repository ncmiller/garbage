from collections import defaultdict

states = {
    'A': {0: (1, 1, 'B'), 1: (0, 1, 'F')},
    'B': {0: (0, -1, 'B'), 1: (1, -1, 'C')},
    'C': {0: (1, -1, 'D'), 1: (0, 1, 'C')},
    'D': {0: (1, -1, 'E'), 1: (1, 1, 'A')},
    'E': {0: (1, -1, 'F'), 1: (0, -1, 'D')},
    'F': {0: (1, 1, 'A'), 1: (0, -1, 'E')},
}

s = 'A'
N = 12425180

idx = 0
tape = defaultdict(int)

for i in range(N):
    state = states[s]
    w, m, n = state[tape[idx]]
    tape[idx] = w
    idx += m
    s = n

print sum(tape.values())
