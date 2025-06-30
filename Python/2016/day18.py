# Determine how many safe tiles there in a floor where traps are set based on the row prior

def get_safe_tiles(values):
    # The first row of the floor is given, so we set it in a new array
    floor = [values[0]]
    width = len(floor[0])
    height = int(values[1])

    # Now we just go through each row and construct them
    for row in range(1, height):
        tiles = ""
        for index in range(width):
            # Get left
            left = '.' if index - 1 < 0 else floor[row-1][index-1]
            # Get middle
            middle = floor[row-1][index]
            # Get right
            right = '.' if index + 1 >= width else floor[row-1][index+1]

            # Now see if this tile should be a trap or not
            # The rules basically make it such that we do an xor on left and right
            if left != right:
                tiles += '^'
            else:
                tiles += '.'
        floor.append(tiles)

    # Calculate the total number of safe tiles
    safe_tiles = 0
    for row in floor:
        for tile in row:
            if tile == '.':
                safe_tiles += 1
    return safe_tiles


def part1(values):
    return get_safe_tiles(values)


def part2(values):
    values[1] = "400000"
    return get_safe_tiles(values)
