# Generate a maze using an algorithm and determine the shortest path between two points within it
from collections import deque

DESIGNER_NUMBER = 1362
# DESIGNER_NUMBER = 10


if __name__ == '__main__':
    print("Starting Day 13-1")

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

    # Find a path, starting at 1,1
    x,y = 1,1
    # TARGET_X, TARGET_Y = 7,4
    TARGET_X, TARGET_Y = 31,39

    # In order to determine the right path, we need to keep track of current states and how many steps it took to get
    # there. We will use a simple dictionary with the current coordinates and the path history to keep track of steps
    # and also prevent repeating steps.
    min_path = None
    queue = deque()
    start = {'coord': (x,y), 'hist': []}
    queue.append(start)

    # Now start the looping through the queue
    while len(queue) > 0:
        step = queue.popleft()
        x,y = step['coord']
        # Check to see if we have reached our target
        if x == TARGET_X and y == TARGET_Y:
            path = step['hist'] + [(x,y)]
            if min_path == None:
                min_path = path
            elif len(min_path) > len(path):
                min_path = path
            continue

        # Make the next steps and put them in a list
        options = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
        for option in options:
            if option[0] < 0 or option[1] < 0:
                # Out of bounds
                continue
            if option in step['hist']:
                # Already visited
                continue
            tile = get_tile(*option)
            if tile == '#':
                # Found wall
                continue
            elif tile == '.':
                # We have an open space we haven't visited yet, so add it to the queue
                new_step = {'coord': option, 'hist': step['hist'][:] + [(x,y)]}
                queue.append(new_step)

    # Testing get_tile
    grid = [[''] * 40 for i in range(40)]
    for y in range(40):
        for x in range(40):
            if (x,y) in min_path:
                grid[y][x] = 'O'
            else:
                grid[y][x] = get_tile(x, y)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end='')
        print()

    print("The shortest path is {0!s} steps".format(len(min_path) - 1))
