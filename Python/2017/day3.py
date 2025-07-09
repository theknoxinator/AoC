# Figure out the number of steps it takes to get from a space on a spiraling incrementer to the center (1)

def find_steps(values):
    target = int(values[0])

    # First thing is to figure out how big of a grid we need, we do this by finding squares of increasing size until
    # the target number is within the grid size
    grid_size = 1
    while grid_size * grid_size < target:
        grid_size += 2

    # Second thing is to figure out how many steps it takes. We know that the minimum is (grid_size - 1) / 2 since it
    # has to be on the outer edge, and maximum is (grid_size - 1). If all spaces on the outer edge are laid in a single
    # line, the corners are at the end of each quarter.
    corners = []
    inner_max = (grid_size - 2) * (grid_size - 2)
    outer_max = grid_size * grid_size
    segment_size = int((outer_max - inner_max) / 4)
    for i in range(1,5):
        corners.append(inner_max + segment_size * i)

    # With the corners, we can find the mid point between them and get the distance of the point from that mid, then add
    # that to the minimum to find the total distance
    distance_from_mid = 0
    for i in range(3):
        if corners[i] < target < corners[i + 1]:
            distance_from_mid = abs(target - int((corners[i + 1] - corners[i]) / 2 + corners[i]))

    return int((grid_size - 1) / 2 + distance_from_mid)


def find_steps2(values):
    target = int(values[0])

    # This time we can't use an algorithm, so we have to actually build out the grid
    # Instead of a 2D array though, we're just going to use a map to store the values so that we can more easily find
    # the adjacent squares
    x, y = 0, 0
    grid = {(x, y): 1}

    def get_adjacent_squares(x, y):
        sum = 0
        for x_i in range(x - 1, x + 2):
            for y_i in range(y - 1, y + 2):
                if (x_i, y_i) in grid:
                    sum += grid[(x_i, y_i)]
        return sum

    next_step = 'r'
    while True:
        if next_step == 'r':
            # Moving right
            x = x + 1
            sum = get_adjacent_squares(x, y)
            grid[(x, y)] = sum
            if (x, y - 1) not in grid:
                next_step = 'u'
        elif next_step == 'u':
            # Moving up
            y = y - 1
            sum = get_adjacent_squares(x, y)
            grid[(x, y)] = sum
            if (x - 1, y) not in grid:
                next_step = 'l'
        elif next_step == 'l':
            # Moving left
            x = x - 1
            sum = get_adjacent_squares(x, y)
            grid[(x, y)] = sum
            if (x, y + 1) not in grid:
                next_step = 'd'
        elif next_step == 'd':
            # Moving down
            y = y + 1
            sum = get_adjacent_squares(x, y)
            grid[(x, y)] = sum
            if (x + 1, y) not in grid:
                next_step = 'r'

        if grid[(x, y)] > target:
            break

    return grid[(x, y)]


def part1(values):
    return find_steps(values)


def part2(values):
    return find_steps2(values)
