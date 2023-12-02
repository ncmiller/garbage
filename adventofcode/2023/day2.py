import fileinput
import re

def parse_pull_group(pg):
    pulls = []
    for p in pg.split(', '):
        num, color = p.split(' ')
        num = int(num)
        pulls.append((num, color))
    return pulls

class Game:
    def __init__(self, string):
        string = string[:-1] # remove \n
        result = re.search("Game (\d+): (.+)", string)
        self.game_id = int(result.group(1))
        pull_groups_str = result.group(2).split('; ')
        self.pull_groups = [parse_pull_group(pg) for pg in pull_groups_str]
        # print(self.game_id, self.pull_groups)

def part1(games):
    game_id_sum = 0
    bag_contents = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    for g in games:
        is_valid_game = True
        for pg in g.pull_groups:
            for p in pg:
                if bag_contents[p[1]] < p[0]:
                    is_valid_game = False
                    break
            if not is_valid_game:
                break
        if is_valid_game:
            game_id_sum += g.game_id

    return game_id_sum

def max_of_color(pull_groups, color):
    max_color = -1
    for pg in pull_groups:
        for p in pg:
            if p[1] == color:
                max_color = max(max_color, p[0])
    return max_color

def part2(games):
    power_sum = 0
    for game in games:
        r = max_of_color(game.pull_groups, 'red')
        g = max_of_color(game.pull_groups, 'green')
        b = max_of_color(game.pull_groups, 'blue')
        power_sum += (r * g * b)
    return power_sum

games = list(fileinput.input())
games = [Game(g) for g in games]
print(part1(games))
print(part2(games))
