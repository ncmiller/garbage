import fileinput
import re

def parse_line(line):
    p = re.compile('.*x=(\d+), y=(\d+).*x=(-?\d+), y=(-?\d+)')
    return list(map(int, p.match(line).groups()))

def dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def part1(row, limit, sensors, beacons, sensor_reaches):
    # for each sensor, add x intervals that intersect with horiz line at row
    x_intervals = []
    for i in range(len(sensors)):
        dist_to_row = abs(sensors[i][1] - row)
        if dist_to_row > sensor_reaches[i]:
            continue
        x_span = sensor_reaches[i] - dist_to_row
        x_interval = [sensors[i][0] - x_span, sensors[i][0] + x_span]
        x_intervals.append(x_interval)

    # merge the intervals so they are non-overlapping
    x_intervals = sorted(x_intervals)
    merged_x_intervals = []
    temp_interval = []
    for i in range(len(x_intervals) - 1):
        if not temp_interval:
            temp_interval = x_intervals[i]
        a = temp_interval
        b = x_intervals[i+1]
        if b[0] <= a[1]:
            temp_interval[1] = max(a[1], b[1])
        else:
            merged_x_intervals.append(temp_interval)
            temp_interval = []
    if temp_interval:
        merged_x_intervals.append(temp_interval)

    # print('merged',merged_x_intervals)
    if limit:
        merged_x_intervals = [[max(limit[0], i[0]), min(limit[1], i[1])] for i in merged_x_intervals]

    # add up the length of each interval, but don't count the beacons
    # that are in the interval
    not_beacon_count = 0
    for interval in merged_x_intervals:
        num_beacons = len([b[0] for b in beacons
            if b[1] == row and b[0] >= interval[0] and b[1] <= interval[1]])
        not_beacon_count += (interval[1] - interval[0] + 1 - num_beacons)

    return not_beacon_count, merged_x_intervals

# Super slow! But gets an answer after 30 seconds
def part2(limit, sensors, beacons, sensor_reaches):
    beacon_row = None
    for row in range(limit[0], limit[1] + 1):
        # if row % 100000 == 0:
        #     print(row)
        _, intervals = part1(row, limit, sensors, beacons, sensor_reaches)
        beacon_or_not_beacon = sum([i[1]-i[0]+1 for i in intervals])
        if beacon_or_not_beacon < limit[1] - limit[0] + 1:
            beacon_row = row
            break
    beacon_col = intervals[0][1] + 1
    return beacon_col * 4000000 + beacon_row

positions = [parse_line(line.rstrip()) for line in fileinput.input()]
sensors = [(p[0],p[1]) for p in positions]
beacons = [(p[2],p[3]) for p in positions]
# compute reach of each sensor (dist from sensor to nearest beacon
sensor_reaches = [dist(sensors[i],beacons[i]) for i in range(len(sensors))]
beacons = list(set(beacons)) # remove duplicates

print(part1(2000000, None, sensors, beacons, sensor_reaches)[0]) # input
print(part2((0,4000000), sensors, beacons, sensor_reaches)) # input
