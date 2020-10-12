# Determine the 3x3 square within a 300x300 grid that has the highest power sum

SERIAL_NUMBER = 1723
GRID_SIZE = 300

if __name__ == '__main__':
    print("Starting Day11-1")

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

    # Now go through the grid and determine the sums
    highest_sum = 0
    highest_coord = None
    for y in range(GRID_SIZE - 3):
        for x in range(GRID_SIZE - 3):
            sum = (grid[y][x] + grid[y][x + 1] + grid[y][x + 2] +
                   grid[y + 1][x] + grid[y + 1][x + 1] + grid[y + 1][x + 2] +
                   grid[y + 2][x] + grid[y + 2][x + 1] + grid[y + 2][x + 2])
            if sum > highest_sum:
                highest_sum = sum
                highest_coord = (x + 1, y + 1)

    # Print out answer
    print("The coordinate with the highest sum of {0!s} is: {1!s},{2!s}".format(highest_sum, highest_coord[0], highest_coord[1]))
