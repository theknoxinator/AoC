# Determine the number of trees encountered on slope
import math


def count_trees(values, slopes):
    # We can leave the input data as-is because strings act as arrays of characters
    # For this we are incrementing x by 3 and y by 1 each cycle, until y is greater than the number of rows in values
    tree_counts = []
    for x_step, y_step in slopes:
        x = 0
        tree_count = 0
        for y in range(y_step, len(values), y_step):
            # Since the map extends to the right forever, we can determine the x-coord by modulus
            x += x_step
            adjusted_x = x % len(values[y])
            if values[y][adjusted_x] == '#':
                tree_count += 1
        tree_counts.append(tree_count)

    return math.prod(tree_counts)


def part1(values):
    return count_trees(values, [(3,1)])


def part2(values):
    return count_trees(values, [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ])
