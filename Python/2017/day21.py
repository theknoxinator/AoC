# Part 1: Using a set of rules, morph a grid of pixels and determine the number of pixels after 5 iterations
# Part 2:

def create_rules(values):
    rules = dict()
    for val in values:
        left, right = val.replace('/', '').split(' => ')
        rules[left] = right
        if len(left) == 4:
            # For 2x2, there is no need to do flips since it's too small a space, just rotate 3 times
            for _ in range(3):
                left = left[2] + left[0] + left[3] + left[1]
                rules[left] = right
        else:
            # For 3x3, flip the original, then rotate and flip 3 times to get all 8 possible options
            flipped = left[:3][::-1] + left[3:6][::-1] + left[6:][::-1]
            rules[flipped] = right
            for _ in range(3):
                left = left[6] + left[3] + left[0] + left[7] + left[4] + left[1] + left[8] + left[5] + left[2]
                rules[left] = right
                flipped = left[:3][::-1] + left[3:6][::-1] + left[6:][::-1]
                rules[flipped] = right

    return rules


def find_pixels(values, iterations):
    rules = create_rules(values)
    if len(values) == 2:
        iterations = 2

    # Start with the grid as described in the problem
    grid = ['.#.', '..#', '###']
    for _ in range(iterations):
        new_grid = []
        if len(grid) % 2 == 0:
            # Split grid into 2x2s and merge them all together
            x, y = 0, 0
            while y < len(grid):
                # Go across left to right and collect all morphed squares
                all_squares = []
                while x < len(grid[y]):
                    square = grid[y][x:x + 2] + grid[y + 1][x:x + 2]
                    all_squares.append(rules[square])
                    x += 2

                # With all the new 3x3 squares, merge them together into the next 3 rows of the new grid
                first, second, third = '', '', ''
                for new_sq in all_squares:
                    first += new_sq[:3]
                    second += new_sq[3:6]
                    third += new_sq[6:]
                new_grid.append(first)
                new_grid.append(second)
                new_grid.append(third)
                y += 2
                x = 0
        else:
            # Split grid into 3x3s and merge them all together
            x, y = 0, 0
            while y < len(grid):
                # Go across left to right and collect all morphed squares
                all_squares = []
                while x < len(grid[y]):
                    square = grid[y][x:x + 3] + grid[y + 1][x:x + 3] + grid[y + 2][x:x + 3]
                    all_squares.append(rules[square])
                    x += 3

                # With all the new 4x4 squares, merge them together into the next 4 rows of the new grid
                first, second, third, fourth = '', '', '', ''
                for new_sq in all_squares:
                    first += new_sq[:4]
                    second += new_sq[4:8]
                    third += new_sq[8:12]
                    fourth += new_sq[12:]
                new_grid.append(first)
                new_grid.append(second)
                new_grid.append(third)
                new_grid.append(fourth)
                y += 3
                x = 0

        grid = new_grid

    count = 0
    for row in grid:
        count += row.count('#')
    return count


def part1(values):
    return find_pixels(values, 5)


def part2(values):
    return find_pixels(values, 18)
