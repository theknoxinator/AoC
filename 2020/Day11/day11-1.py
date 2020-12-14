# Determine the number of open seats after an algorithm is applied to a seat map

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["L.LL.LL.LL",
            "LLLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLLL",
            "L.LLLLLL.L",
            "L.LLLLL.LL"]


print("Starting Day11-1")
values = read_file("input.txt")
# values = test_data()


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


def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

# Do a quick conversion of strings to arrays for easier changing
grid = [[char for char in row] for row in values]

# Now loop until there are no more changes to be made
has_changed = True
while has_changed:
    has_changed = False
    old_grid = [[col for col in row] for row in grid]
    print_grid(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if old_grid[y][x] == '.':
                continue
            occupied = get_occupied(old_grid, x, y)
            if old_grid[y][x] == 'L' and occupied == 0:
                grid[y][x] = '#'
                has_changed = True
            elif old_grid[y][x] == '#' and occupied >= 4:
                grid[y][x] = 'L'
                has_changed = True

# Finally check the number of occupied seats after the algo stops
count = 0
for row in grid:
    for col in row:
        if col == '#':
            count += 1
print("The number of occupied seats is: {0!s}".format(count))
