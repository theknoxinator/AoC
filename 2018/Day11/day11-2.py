# Determine the square within a 300x300 grid that has the highest power sum

SERIAL_NUMBER = 1723
GRID_SIZE = 300

if __name__ == '__main__':
    print("Starting Day11-2")

    # Create a grid to hold all the power values
    grid = [[0]*GRID_SIZE for i in range(GRID_SIZE)]

    # Iterate through each square and compute its power level based on the serial number
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rack_id = x + 11 # Add 11 to offset the coordinate difference (0 versus 1)
            power_level = rack_id * (y + 1) # Offset is here too
            power_level = power_level + SERIAL_NUMBER
            power_level = power_level * rack_id
            power_level = int((power_level % 1000) / 100)
            power_level = power_level - 5

            grid[y][x] = power_level

    # Now go through the grid and determine the sums for each size of square
    highest_sum = 0
    highest_coord = None
    highest_square = 0
    for square_size in range(1, GRID_SIZE + 1):
        print("Calculating squares for size: {0!s}".format(square_size))
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

        # Print out answer
        print("The coordinate with the highest sum of {0!s} is: {1!s},{2!s} with square size: {3!s}".format(
            highest_sum, highest_coord[0], highest_coord[1], highest_square))
