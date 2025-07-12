# Determine the first crash site of mine carts given tracks and starting positions of the carts

def determine_crash(values):
    # First we need to read the map into a grid that can be looked at later
    # The position and direction of each cart also needs to be stored separately
    map = []

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

    # for y in range(len(map)):
    #     for x in range(len(map[y])):
    #         if carts[y][x]:
    #             print(carts[y][x].direction, end='')
    #         else:
    #             print(map[y][x], end='')
    #     print()
    # print("Cart count: {0!s}".format(cart_count))

    # Now that we have our map and carts, iterate through the carts from left to right, top to bottom, and
    # move them until a collision happens
    has_collision = False
    count = 0
    first_crash = None
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
                        if not first_crash:
                            first_crash = (next_x, next_y)
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
    return "{0!s},{1!s}".format(first_crash[0], first_crash[1])


def determine_last_cart(values):
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
    cart_count = 0
    for y in range(len(map)):
        row = map[y]
        for x in range(len(row)):
            if row[x] == '^' or row[x] == 'v':
                # Cart is going up/down
                carts[y][x] = Cart(row[x])
                row[x] = '|'
                cart_count += 1
            elif row[x] == '<' or row[x] == '>':
                # Cart is going left/right
                carts[y][x] = Cart(row[x])
                row[x] = '-'
                cart_count += 1

    # for y in range(len(map)):
    #     for x in range(len(map[y])):
    #         if carts[y][x]:
    #             print(carts[y][x].direction, end='')
    #         else:
    #             print(map[y][x], end='')
    #     print()
    # print("Cart count: {0!s}".format(cart_count))

    # Now that we have our map and carts, iterate through the carts from left to right, top to bottom, and
    # move them until a collision happens
    count = 0
    while cart_count > 1:
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
                        # Remove the carts from the system
                        carts[next_y][next_x] = None
                        next_carts[next_y][next_x] = None
                        cart_count -= 2
                        continue

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
    for y in range(len(carts)):
        for x in range(len(carts[y])):
            if carts[y][x] is not None:
                print("The last cart is at {0!s},{1!s}".format(x, y))
                return "{0!s},{1!s}".format(x, y)


def part1(values):
    return determine_crash(values)


def part2(values):
    return determine_last_cart(values)
