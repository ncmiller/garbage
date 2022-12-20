import fileinput
import re

def parse_line(line):
    p = re.compile('Blueprint (\d+):.*(\d+) ore.*(\d+) ore.*(\d+) ore and (\d+) clay.*(\d+) ore and (\d+)')
    m = p.match(line)
    g = list(map(int, m.groups()))[1:]
    return ((g[0],0,0,0), (g[1],0,0,0), (g[2],g[3],0,0), (g[4],0,g[5],0))

def can_build_robot(blueprint, minerals, robot_i):
    can_buy = True
    for mineral_i in reversed(range(len(minerals))):
        if minerals[mineral_i] < blueprint[robot_i][mineral_i]:
            return False
    return True

def have_enough(blueprint, minerals, mineral_i):
    max_needed = max([b[mineral_i] for b in blueprint])
    # These are heuristics that were calibrated to the input.
    # Affects which sub-trees get pruned.
    if mineral_i == 0: return minerals[0] >= (1.5 * max_needed)
    if mineral_i == 1: return minerals[1] >= max_needed
    if mineral_i == 2: return minerals[2] >= max_needed
    if mineral_i == 3: return minerals[3] >= max_needed

# Returns minerals, choices
def backtrack(blueprint, minerals, robots, total_minutes, minute, choices):
    if minute >= total_minutes:
        return minerals, choices

    robot_choices = []
    for robot_to_build in range(len(robots)):
        # Skip this robot if we have enough of them
        if robot_to_build <= 2 and have_enough(blueprint, minerals, robot_to_build):
            continue

        orig_minute = minute
        orig_minerals = minerals[:]
        orig_robots = robots[:]
        orig_choices = choices[:]

        # Fast-forward until we can build this robot, or total_minutes reached
        while minute < total_minutes:
            build_robot = can_build_robot(blueprint, minerals, robot_to_build)
            minute += 1

            # build robot
            if build_robot:
                choices.append((robot_to_build, minute))
                for mineral_i in range(len(minerals)):
                    minerals[mineral_i] -= blueprint[robot_to_build][mineral_i]
                robots[robot_to_build] += 1

            # produce minerals with current robots
            for robot_i in range(len(robots)):
                n_robots = robots[robot_i]
                if robot_i == robot_to_build and build_robot:
                    # omit the robot we just built from this production
                    n_robots -= 1
                minerals[robot_i] += n_robots

            # recurse if we have built a new robot
            if build_robot:
                # print(minute, ' ' * minute, minerals, robots, choices, robot_to_build)
                robot_choices.append(backtrack(blueprint, minerals, robots, total_minutes, minute, choices))
                break

        # Undo the changes above
        minute = orig_minute
        minerals = orig_minerals[:]
        robots = orig_robots[:]
        choices = orig_choices[:]

    if not robot_choices:
        return (minerals, choices)
    else:
        return max(robot_choices, key=lambda x: x[0][3])

def part1(blueprints, total_minutes):
    quality = 0
    for blueprint_i in range(len(blueprints)):
        # minerals and robots in order: [ore, clay, obs, geo]
        minerals = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        minerals, choices = backtrack(blueprints[blueprint_i], minerals, robots, total_minutes, 0, [])
        # print(minerals[3], choices)
        quality += (minerals[3] * (blueprint_i + 1))
    return quality

def part2(blueprints, total_minutes):
    answer = 1
    for blueprint_i in range(len(blueprints)):
        # minerals and robots in order: [ore, clay, obs, geo]
        minerals = [0, 0, 0, 0]
        robots = [1, 0, 0, 0]
        minerals, choices = backtrack(blueprints[blueprint_i], minerals, robots, total_minutes, 0, [])
        # print(minerals[3], choices)
        answer *= minerals[3]
    return answer

blueprints = [parse_line(line.rstrip()) for line in fileinput.input()]
print(part1(blueprints, 24))
print(part2(blueprints[:3], 32))
