import fileinput

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

def draw_point_on_grid(grid, point, x_offset, c):
    grid[point[1]][point[0] - x_offset] = c

def draw_line_on_grid(grid, line, x_offset):
    for i in range(len(line) - 1):
        a = line[i]
        b = line[i+1]
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        if dx > 0:
            for x in range(a[0], b[0] + 1):
                draw_point_on_grid(grid, (x, a[1]), x_offset, '#')
        if dx < 0:
            for x in range(a[0], b[0] - 1, -1):
                draw_point_on_grid(grid, (x, a[1]), x_offset, '#')
        if dy > 0:
            for y in range(a[1], b[1] + 1):
                draw_point_on_grid(grid, (a[0], y), x_offset, '#')
        if dy < 0:
            for y in range(a[1], b[1] - 1, -1):
                draw_point_on_grid(grid, (a[0], y), x_offset, '#')


def simulate_sand(grid, sand_entry, x_offset):
    landed = False
    point = sand_entry
    while True:
        # print(point)
        normalized_x = point[0] - x_offset
        if point[1] >= len(grid) - 1 or normalized_x < 0 or normalized_x >= len(grid[0]):
            break
        elif point == sand_entry and grid[point[1]][normalized_x] == 'o':
            break
        elif grid[point[1]+1][normalized_x] == '.': # down
            point = (point[0], point[1] + 1)
        elif grid[point[1]+1][normalized_x - 1] == '.': # down and left
            point = (point[0] - 1, point[1] + 1)
        elif grid[point[1]+1][normalized_x + 1] == '.': # down and right
            point = (point[0] + 1, point[1] + 1)
        else: # all blocked, comes to rest here
            landed = True
            draw_point_on_grid(grid, point, x_offset, 'o')
            break
    return landed

def falling_sand(lines, with_floor):
    sand_entry = (500,0)
    min_x = min([min([point[0] for point in line]) for line in lines])
    max_x = max([max([point[0] for point in line]) for line in lines])
    max_y = max([max([point[1] for point in line]) for line in lines])
    if with_floor:
        max_y += 2
        min_x -= max_y
        max_x += max_y
    width = max_x - min_x + 1
    height = max_y + 1
    x_offset = min_x
    # (0,0) in the grid represents (min_x, 0)
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for line in lines:
        draw_line_on_grid(grid, line, min_x)

    if with_floor:
        floor = [[min_x,max_y],[max_x,max_y]]
        draw_line_on_grid(grid, floor, min_x)

    # print_grid(grid)

    total_landed = 0
    while True:
        landed = simulate_sand(grid, sand_entry, x_offset)
        if not landed:
            break
        total_landed += 1
    # print_grid(grid)
    return total_landed

lines = [[list(map(int, x.split(','))) for x in line.rstrip().split(' -> ')] for line in fileinput.input()]
print(falling_sand(lines, False))
print(falling_sand(lines, True))
