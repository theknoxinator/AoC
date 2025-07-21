# Determine the number of open seats after an algorithm is applied to a seat map

# Make a function to check a specific space in the given grid
def is_occupied(grid, x, y):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return False
    return grid[y][x] == '#'


# Make a function to do the checks, returns the number of occupied seats
def get_occupied(grid, x, y):
    occupied = 0
    # Upper left
    if is_occupied(grid, x - 1, y - 1):
        occupied += 1
    # Upper middle
    if is_occupied(grid, x, y - 1):
        occupied += 1
    # Upper right
    if is_occupied(grid, x + 1, y - 1):
        occupied += 1
    # Middle left
    if is_occupied(grid, x - 1, y):
        occupied += 1
    # Middle right
    if is_occupied(grid, x + 1, y):
        occupied += 1
    # Lower left
    if is_occupied(grid, x - 1, y + 1):
        occupied += 1
    # Lower middle
    if is_occupied(grid, x, y + 1):
        occupied += 1
    # Lower right
    if is_occupied(grid, x + 1, y + 1):
        occupied += 1
    return occupied


# Make a function to check a line of spaces in the given grid
def is_occupied2(grid, start_x, start_y, diff_x, diff_y):
    x = start_x + diff_x
    y = start_y + diff_y
    while 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        if grid[y][x] == 'L':
            return False
        elif grid[y][x] == '#':
            return True
        x += diff_x
        y += diff_y
    return False


# Make a function to do the checks, returns the number of occupied seats
def get_occupied2(grid, x, y):
    occupied = 0
    # Upper left
    if is_occupied2(grid, x, y, -1, -1):
        occupied += 1
    # Upper middle
    if is_occupied2(grid, x, y, 0, -1):
        occupied += 1
    # Upper right
    if is_occupied2(grid, x, y, 1, -1):
        occupied += 1
    # Middle left
    if is_occupied2(grid, x, y, -1, 0):
        occupied += 1
    # Middle right
    if is_occupied2(grid, x, y, 1, 0):
        occupied += 1
    # Lower left
    if is_occupied2(grid, x, y, -1, 1):
        occupied += 1
    # Lower middle
    if is_occupied2(grid, x, y, 0, 1):
        occupied += 1
    # Lower right
    if is_occupied2(grid, x, y, 1, 1):
        occupied += 1
    return occupied


def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()


def find_open_seats(values, use_part2=False):
    # Do a quick conversion of strings to arrays for easier changing
    grid = [[char for char in row] for row in values]
    max_occupied = 5 if use_part2 else 4

    # Now loop until there are no more changes to be made
    has_changed = True
    while has_changed:
        has_changed = False
        old_grid = [[col for col in row] for row in grid]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if old_grid[y][x] == '.':
                    continue
                occupied = get_occupied2(old_grid, x, y) if use_part2 else get_occupied(old_grid, x, y)
                if old_grid[y][x] == 'L' and occupied == 0:
                    grid[y][x] = '#'
                    has_changed = True
                elif old_grid[y][x] == '#' and occupied >= max_occupied:
                    grid[y][x] = 'L'
                    has_changed = True

    # Finally check the number of occupied seats after the algo stops
    count = 0
    for row in grid:
        for col in row:
            if col == '#':
                count += 1
    return count


def part1(values):
    return find_open_seats(values)


def part2(values):
    return find_open_seats(values, True)
