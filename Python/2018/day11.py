# Determine the 3x3 square within a 300x300 grid that has the highest power sum

GRID_SIZE = 300

def determine_square(values, use_part2=False):
    serial_number = int(values[0])

    # Create a grid to hold all the power values
    grid = [[0] * GRID_SIZE for i in range(GRID_SIZE)]

    # Iterate through each square and compute its power level based on the serial number
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rack_id = x + 11 # Add 11 to offset the coordinate difference (0 versus 1)
            power_level = rack_id * (y + 1) # Offset is here too
            power_level = power_level + serial_number
            power_level = power_level * rack_id
            power_level = int((power_level % 1000) / 100)
            power_level = power_level - 5

            grid[y][x] = power_level

    # Now go through the grid and determine the sums
    highest_sum = 0
    highest_coord = None
    highest_square = 0
    if not use_part2:
        for y in range(GRID_SIZE - 3):
            for x in range(GRID_SIZE - 3):
                sum = (grid[y][x] + grid[y][x + 1] + grid[y][x + 2] +
                       grid[y + 1][x] + grid[y + 1][x + 1] + grid[y + 1][x + 2] +
                       grid[y + 2][x] + grid[y + 2][x + 1] + grid[y + 2][x + 2])
                if sum > highest_sum:
                    highest_sum = sum
                    highest_coord = (x + 1, y + 1)

        return "{0!s},{1!s}".format(highest_coord[0], highest_coord[1])
    else:
        for square_size in range(1, GRID_SIZE + 1):
            for y in range(GRID_SIZE - square_size + 1):
                for x in range(GRID_SIZE - square_size + 1):
                    sum = 0
                    for y_offset in range(square_size):
                        for x_offset in range(square_size):
                            sum += grid[y + y_offset][x + x_offset]
                    if sum > highest_sum:
                        highest_sum = sum
                        highest_coord = (x + 1, y + 1)
                        highest_square = square_size
        return "{0!s},{1!s},{2!s}".format(highest_coord[0], highest_coord[1], highest_square)


def part1(values):
    return determine_square(values)


def part2(values):
    return determine_square(values, True)
