import fileinput
import operator
#----------------------
# File IO
#----------------------
# for line in fileinput.input():

# with open("day9_input.txt") as f:
#     chars = f.read()

# vals = map(int, fileinput.input())

# weight = int(fields[1].replace('(','').replace(')',''))
# stowers = [x.split(',')[0] for x in fields[2:]]
#----------------------

logs = []
for line in fileinput.input():
    line = line.rstrip()
    line = line.replace('[','').replace(']','').replace(',', ' ').split(' ')
    date = map(int, line[0].split('-'))
    time = map(int, line[1].split(':'))
    gid = -1
    if line[2] == 'Guard':
        event = 'begin'
        gid = int(line[3][1:])
    elif line[2] == 'wakes':
        event = 'wakes'
    elif line[2] == 'falls':
        event = 'falls'
    logs.append((date, time, gid, event))

def log_compare(x, y):
    if x[0][0] - y[0][0] > 0: # year compare
        return 1
    elif x[0][0] - y[0][0] < 0: # year compare
        return -1

    if x[0][1] - y[0][1] > 0: # month
        return 1
    elif x[0][1] - y[0][1] < 0: # month
        return -1

    if x[0][2] - y[0][2] > 0: # day
        return 1
    elif x[0][2] - y[0][2] < 0: # day
        return -1

    if x[1][0] - y[1][0] > 0: # hour
        return 1
    elif x[1][0] - y[1][0] < 0: # hour
        return -1

    if x[1][1] - y[1][1] > 0: # minute
        return 1
    elif x[1][1] - y[1][1] < 0: # minute
        return -1

    return 0

logs = sorted(logs, cmp=log_compare)

stats = {}
asleep = -1
gid = -1
for l in logs:
    hour = l[1][0]
    minute = l[1][1]

    if l[3] == 'begin':
        gid = l[2]
    elif l[3] == 'falls':
        # asleep = hour*60 + minute
        asleep = minute
    elif l[3] == 'wakes':
        # awake = hour*60 + minute
        awake = minute
        if gid not in stats:
            stats[gid] = []
        stats[gid].append((asleep,awake))

def part1():
    final_stats = []
    for gid,vals in stats.items():
        minutes_asleep = {}
        total_minutes_asleep = 0
        for v in vals:
            for m in range(v[0],v[1]):
                if m not in minutes_asleep:
                    minutes_asleep[m] = 1
                else:
                    minutes_asleep[m] += 1
                total_minutes_asleep += 1
        most_frequent_minute_asleep = sorted(minutes_asleep.items(), key=operator.itemgetter(1))[-1][0]
        final_stats.append((gid, total_minutes_asleep, most_frequent_minute_asleep))
    final_stats = list(reversed(sorted(final_stats, key=lambda x: x[1])))
    print final_stats[0][0] * final_stats[0][2]

def part2():
    final_stats = []
    for gid,vals in stats.items():
        minutes_asleep = {}
        for v in vals:
            for m in range(v[0],v[1]):
                if m not in minutes_asleep:
                    minutes_asleep[m] = 1
                else:
                    minutes_asleep[m] += 1
        s = sorted(minutes_asleep.items(), key=operator.itemgetter(1))[-1]
        most_frequent_minute_asleep = s[0]
        times_asleep_on_minute = s[1]
        final_stats.append((gid, most_frequent_minute_asleep, times_asleep_on_minute))
    final_stats = list(reversed(sorted(final_stats, key=lambda x: x[2])))
    print final_stats[0][0] * final_stats[0][1]

part1()
part2()
