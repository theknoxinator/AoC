# Figure out the number of steps it takes to get from a space on a spiraling incrementer to the center (1)


# target = 1
# target = 12
# target = 23
# target = 1024
target = 368078


if __name__ == "__main__":
    print("Starting Day 3-1")

    # First thing is to figure out how big of a grid we need, we do this by finding squares of increasing size until
    # the target number is within the grid size
    grid_size = 1
    while grid_size * grid_size < target:
        grid_size += 2

    print("The size grid we need to find {0!s} is {1!s}x{1!s}".format(target, grid_size))

    # Second thing is to figure out how many steps it takes. We know that the minimum is (grid_size - 1) / 2 since it
    # has to be on the outer edge, and maximum is (grid_size - 1). If all spaces on the outer edge are laid in a single
    # line, the corners are at the end of each quarter.
    corners = []
    inner_max = (grid_size - 2) * (grid_size - 2)
    outer_max = grid_size * grid_size
    segment_size = int((outer_max - inner_max) / 4)
    for i in range(1,5):
        corners.append(inner_max + segment_size * i)

    print("The four corners of the outer grid are: {0!s}".format(corners))

    # With the corners, we can find the mid point between them and get the distance of the point from that mid, then add
    # that to the minimum to find the total distance
    distance_from_mid = 0
    for i in range(3):
        if corners[i] < target < corners[i + 1]:
            distance_from_mid = abs(target - int((corners[i + 1] - corners[i]) / 2 + corners[i]))

    print("The total distance from the middle is {0!s}".format((grid_size - 1) / 2 + distance_from_mid))
