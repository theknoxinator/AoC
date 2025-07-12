# Determine the number of acres of wood and lumberyards there are in a plot of land after a certain amount
# of time. The acres change based on their neighbors.
from datetime import datetime

def calc_lumber(values, num_loops=10):
    # Convert the input into a grid
    grid = []
    for val in values:
        grid.append(list(val))

    # Debug print out initial grid
    # for row in grid:
    #     print(''.join(row))
    # print()

    # For this problem, we are going to iterate through each cell, which is an acre, look at the 8 (or less)
    # adjacent cells, and determine what the cell will look like on the next step. New steps are going into
    # a new grid of the same size as the existing one, which overwrites the existing grid upon completion.
    new_grid = [[''] * len(grid) for i in range(len(grid))]
    for loops in range(num_loops):
        # if loops % 1000 == 0:
        #     print("{0!s}: {1!s}".format(loops, datetime.now()))
        #     total_woods = 0
        #     total_lumberyards = 0
        #     for row in grid:
        #         for cell in row:
        #             if cell == '|':
        #                 total_woods += 1
        #             elif cell == '#':
        #                 total_lumberyards += 1
        #     print(
        #         "The number of woods is: {0!s}, and number of lumberyards is: {1!s}, which creates total resource value of {2!s}".format(
        #             total_woods, total_lumberyards, total_woods * total_lumberyards))
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                # Get the current cell for later
                cell = grid[y][x]

                # Make a list of the 8 adjacent points to look at
                adjacent_cells = [
                    (x - 1, y - 1),  # Top left
                    (x, y - 1),  # Top middle
                    (x + 1, y - 1),  # Top right
                    (x - 1, y),  # Left
                    (x + 1, y),  # Right
                    (x - 1, y + 1),  # Bottom left
                    (x, y + 1),  # Bottom middle
                    (x + 1, y + 1)  # Bottom right
                ]

                # Count up the number of each acre type
                num_open = 0
                num_woods = 0
                num_lumberyards = 0
                for adjacent_cell in adjacent_cells:
                    ax, ay = adjacent_cell
                    if ax < 0 or ay < 0 or ax >= len(grid) or ay >= len(grid):
                        # Point is outside bounds, so skip
                        continue
                    if grid[ay][ax] == '.':
                        num_open += 1
                    elif grid[ay][ax] == '|':
                        num_woods += 1
                    elif grid[ay][ax] == '#':
                        num_lumberyards += 1

                # Now determine what the next acre type is for the current acre
                if cell == '.':
                    # Open acres become woods if 3 or more neighbors are woods
                    if num_woods >= 3:
                        new_grid[y][x] = '|'
                    else:
                        new_grid[y][x] = '.'
                elif cell == '|':
                    # Woods acres become lumberyards if 3 or more neighbors are lumberyards
                    if num_lumberyards >= 3:
                        new_grid[y][x] = '#'
                    else:
                        new_grid[y][x] = '|'
                elif cell == '#':
                    # Lumberyard acres stay lumberyards if at least one neighbor is a numberyard and
                    # at least one neighbor is a woods, else becomes open
                    if num_woods >= 1 and num_lumberyards >= 1:
                        new_grid[y][x] = '#'
                    else:
                        new_grid[y][x] = '.'

        # Overwrite old grid with new one for next step
        temp = grid
        grid = new_grid
        new_grid = temp
        # print("Loop {0!s}".format(loops + 1))
        # for row in grid:
        #     print(''.join(row))
        # print()

    # Print out answer
    total_woods = 0
    total_lumberyards = 0
    for row in grid:
        for cell in row:
            if cell == '|':
                total_woods += 1
            elif cell == '#':
                total_lumberyards += 1
    print(
        "The number of woods is: {0!s}, and number of lumberyards is: {1!s}, which creates total resource value of {2!s}".format(
            total_woods, total_lumberyards, total_woods * total_lumberyards))
    return total_woods * total_lumberyards


def part1(values):
    return calc_lumber(values, 10)


def part2(values):
    return calc_lumber(values, 1000000000)
