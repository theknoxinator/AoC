# Determine the first crash site of mine carts given tracks and starting positions of the carts

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.rstrip())

    return values

def test_data():
    return ['/->-\\',
            '|   |  /----\\',
            '| /-+--+-\\  |',
            '| | |  | v  |',
            '\\-+-/  \\-+--/',
            '  \\------/']

if __name__ == '__main__':
    print("Starting Day 13-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # First we need to read the map into a grid that can be looked at later
    # The position and direction of each cart also needs to be stored separately
    map = []
    carts = []

    class Cart:
        def __init__(self, start_direction):
            self.direction = start_direction
            self.turn_count = 0

    # The best thing to do first is just read in the map so that we can create an equally sized grid for
    # the carts
    max_width = 0
    for val in values:
        if len(val) > max_width:
            max_width = len(val)
        map.append(list(val))

    # Now create the carts grid, and read the values into it from the map grid
    carts = [[None] * max_width for i in range(len(map))]
    for y in range(len(map)):
        row = map[y]
        for x in range(len(row)):
            if row[x] == '^' or row[x] == 'v':
                # Cart is going up/down
                carts[y][x] = Cart(row[x])
                row[x] = '|'
            elif row[x] == '<' or row[x] == '>':
                # Cart is going left/right
                carts[y][x] = Cart(row[x])
                row[x] = '-'

    for y in range(len(map)):
        for x in range(len(map[y])):
            if carts[y][x]:
                print(carts[y][x].direction, end='')
            else:
                print(map[y][x], end='')
        print()

    # Now that we have our map and carts, iterate through the carts from left to right, top to bottom, and
    # move them until a collision happens
    has_collision = False
    count = 0
    while not has_collision:
        count += 1
        next_carts = [[None] * max_width for i in range(len(carts))]
        for y in range(len(carts)):
            for x in range(len(carts[y])):
                if carts[y][x]:
                    # There is a cart at this spot, see where it is headed, and move it to the next spot
                    current_cart = carts[y][x]
                    next_x = x
                    next_y = y
                    direction = current_cart.direction
                    if direction == '^':
                        next_y -= 1
                    elif direction == 'v':
                        next_y += 1
                    elif direction == '<':
                        next_x -= 1
                    elif direction == '>':
                        next_x += 1

                    # First check to see if there is a cart there
                    if carts[next_y][next_x] is not None or next_carts[next_y][next_x] is not None:
                        print("Collision happens at {0!s},{1!s}".format(next_x, next_y))
                        has_collision = True

                    next_space = map[next_y][next_x]
                    if next_space == '+':
                        # Intersection, so determine the next direction
                        if current_cart.turn_count % 3 == 0:
                            # Turn left relative to current direction
                            if direction == '^' or direction == 'v':
                                next_space = '\\'
                            elif direction == '<' or direction == '>':
                                next_space = '/'
                            else:
                                print("Error occurred with current cart direction: {0}".format(direction))
                        elif current_cart.turn_count % 3 == 1:
                            # Go straight relative to current direction
                            if direction == '^' or direction == 'v':
                                next_space = '|'
                            elif direction == '<' or direction == '>':
                                next_space = '-'
                            else:
                                print("Error occurred with current cart direction: {0}".format(direction))
                        elif current_cart.turn_count % 3 == 2:
                            # Turn right relative to current direction
                            if direction == '^' or direction == 'v':
                                next_space = '/'
                            elif direction == '<' or direction == '>':
                                next_space = '\\'
                            else:
                                print("Error occurred with current cart direction: {0}".format(direction))
                        else:
                            print("Your code is bad and you should feel bad")
                        # Increment the turn count
                        current_cart.turn_count += 1

                    if next_space == '-' or next_space == '|':
                        # Cart is going straight, so no need to change direction
                        pass
                    elif next_space == '\\':
                        if direction == '^':
                            # Up goes left
                            current_cart.direction = '<'
                        elif direction == 'v':
                            # Down goes right
                            current_cart.direction = '>'
                        elif direction == '<':
                            # Left goes up
                            current_cart.direction = '^'
                        elif direction == '>':
                            # Right goes down
                            current_cart.direction = 'v'
                        else:
                            print("Error occurred with current cart direction: {0}".format(direction))
                    elif next_space == '/':
                        if direction == '^':
                            # Up goes right
                            current_cart.direction = '>'
                        elif direction == 'v':
                            # Down goes left
                            current_cart.direction = '<'
                        elif direction == '<':
                            # Left goes down
                            current_cart.direction = 'v'
                        elif direction == '>':
                            # Right goes up
                            current_cart.direction = '^'
                        else:
                            print("Error occurred with current cart direction: {0}".format(direction))

                    # Move the cart to the new spot
                    carts[y][x] = None
                    next_carts[next_y][next_x] = current_cart

        carts = next_carts
        # for y in range(len(map)):
        #     for x in range(len(map[y])):
        #         if carts[y][x]:
        #             print(carts[y][x].direction, end='')
        #         else:
        #             print(map[y][x], end='')
        #     print()

    print("Took {0!s} ticks".format(count))
