# Generate a maze using an algorithm and determine the number of tiles you can reach in 50 steps or less
from collections import deque

DESIGNER_NUMBER = 1362
# DESIGNER_NUMBER = 10


if __name__ == '__main__':
    print("Starting Day 13-2")

    # Define a function that determines what kind of tile a coordinate is
    def get_tile(x, y):
        magic_number = x*x + 3*x + 2*x*y + y + y*y
        magic_number += DESIGNER_NUMBER
        bin_magic_number = bin(magic_number)[2:]
        total_bits = 0
        for char in bin_magic_number:
            if char == '1':
                total_bits += 1
        if total_bits % 2 == 0:
            # Bits is even, so tile is open space
            return '.'
        else:
            # Bits is odd, so tile is wall
            return '#'

    # Start at 1,1
    x,y = 1,1

    # Not finding a path this time, we just need to go 50 steps in every direction and identify how many tiles get hit
    tiles = set()
    tiles.add((x,y))
    queue = deque()
    start = {'coord': (x,y), 'steps': 0}
    queue.append(start)

    # Now start the looping through the queue
    while len(queue) > 0:
        step = queue.popleft()
        x,y = step['coord']
        # Ignore this step if it is above 50
        if step['steps'] > 50:
            continue
        else:
            tiles.add((x,y))

        # Make the next steps and put them in a list
        options = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
        for option in options:
            if option[0] < 0 or option[1] < 0:
                # Out of bounds
                continue
            if option in tiles:
                # Already visited
                continue
            tile = get_tile(*option)
            if tile == '#':
                # Found wall
                continue
            elif tile == '.':
                # We have an open space we haven't visited yet, so add it to the queue
                new_step = {'coord': option, 'steps': step['steps'] + 1}
                queue.append(new_step)

    # Testing get_tile
    grid = [[''] * 40 for i in range(40)]
    for y in range(40):
        for x in range(40):
            if (x,y) in tiles:
                grid[y][x] = 'O'
            else:
                grid[y][x] = get_tile(x, y)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end='')
        print()

    print("The number of unique tiles hit is: {0!s}".format(len(tiles)))
