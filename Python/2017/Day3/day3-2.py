# Figure out the first value larger than the target when filling a grid with a spiral incrementer that uses adjacent
# values to calculate sums


target = 368078


if __name__ == "__main__":
    print("Starting Day 3-2")

    # This time we can't use an algorithm, so we have to actually build out the grid
    # Instead of a 2D array though, we're just going to use a map to store the values so that we can more easily find
    # the adjacent squares
    x,y = 0,0
    grid = {(x,y): 1}

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
            grid[(x,y)] = sum
            if (x, y-1) not in grid:
                next_step = 'u'
        elif next_step == 'u':
            # Moving up
            y = y - 1
            sum = get_adjacent_squares(x, y)
            grid[(x,y)] = sum
            if (x-1, y) not in grid:
                next_step = 'l'
        elif next_step == 'l':
            # Moving left
            x = x - 1
            sum = get_adjacent_squares(x, y)
            grid[(x,y)] = sum
            if (x, y+1) not in grid:
                next_step = 'd'
        elif next_step == 'd':
            # Moving down
            y = y + 1
            sum = get_adjacent_squares(x, y)
            grid[(x,y)] = sum
            if (x+1, y) not in grid:
                next_step = 'r'

        if grid[(x,y)] > target:
            break

    print("The first value after {0!s} is {1!s}".format(target, grid[(x,y)]))