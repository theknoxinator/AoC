# Calculate the number of defined squares that overlap, and determine the exact number of square inches
# that is being overlapped

def overlapping_squares(values, use_part2=False):
    # Set up array that represents the full piece of fabric (1000x1000)
    fabric = [[0]*1000 for i in range(1000)]

    # Iterate through each order and fill in the square the order represents
    for order in values:
        # Get the data we care about, split by whitespace and take the third and fourth parts
        order_parts = order.replace(':', '').split()
        # The third part is the starting point
        start_point = list(map(int, order_parts[2].split(',')))
        # The fourth part is the size of the square
        size = list(map(int, order_parts[3].split('x')))

        # Now loop through each space of the square and increment the fabric value
        for i in range(start_point[1], start_point[1] + size[1]):
            for j in range(start_point[0], start_point[0] + size[0]):
                fabric[i][j] += 1

    if not use_part2:
        # Go back through the fabric and check how many spaces are above one
        total_sq = 0
        for row in fabric:
            for space in row:
                if space > 1:
                    total_sq += 1
        return total_sq
    else:
        # Go back through the orders and see which one has only ones in the square
        correct_order = ""
        for order in values:
            # Get the data we care about, split by whitespace and take the third and fourth parts
            order_parts = order.replace(':', '').split()
            # The third part is the starting point
            start_point = list(map(int, order_parts[2].split(',')))
            # The fourth part is the size of the square
            size = list(map(int, order_parts[3].split('x')))

            # Now loop through each space of the square and check the fabric value
            has_overlap = False
            for i in range(start_point[1], start_point[1] + size[1]):
                for j in range(start_point[0], start_point[0] + size[0]):
                    if fabric[i][j] > 1:
                        has_overlap = True

            if not has_overlap:
                correct_order = order_parts[0]
        return correct_order


def part1(values):
    return overlapping_squares(values)


def part2(values):
    return overlapping_squares(values, True)
