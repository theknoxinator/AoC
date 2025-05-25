# Determine how many locations are visited on a grid using defined instructions
def move(x, y, direction):
    if direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    elif direction == '<':
        x -= 1
    elif direction == '>':
        x += 1
    return x, y


def add_location(x, y, locations):
    current = (x, y)
    if current in locations:
        locations[current] += 1
    else:
        locations[current] = 1
    return locations


def part1(values):
    # For the first part we are just counting the number of grid points that get visited
    locations = {(0,0): 1}

    x, y = 0, 0
    for direction in values[0]:
        x, y = move(x, y, direction)
        locations = add_location(x, y, locations)

    return len(locations.keys())


def part2(values):
    # For the second part we are doing the same thing but we are tracking two visitors
    locations = {(0,0): 1}

    x = [0, 0]
    y = [0, 0]
    for index, direction in enumerate(values[0]):
        visitor = index % 2
        x[visitor], y[visitor] = move(x[visitor], y[visitor], direction)
        locations = add_location(x[visitor], y[visitor], locations)

    return len(locations.keys())
