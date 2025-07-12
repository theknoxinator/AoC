# Determine the number of sand tiles that the water can reach assuming that it is always falling downward
# and clay blocks flow such that it moves left and right
from collections import deque

def waterfall_hell(values):
    # Create the initial grid with all sand
    grid = [['.'] * 1000 for i in range(2000)]
    # Put in the fountain at 500,0
    grid[0][500] = '+'

    # Go through each piece of the input and fill in the rows/cols being described as clay
    min_x = 1000
    max_x = 0
    max_y = 0
    for val in values:
        items = val.replace(',', '').split()
        if 'x' in items[0]:
            x = int(items[0][2:])
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            start_y, end_y = map(int, items[1][2:].split('..'))
            for y in range(start_y, end_y + 1):
                if y > max_y:
                    max_y = y
                grid[y][x] = '#'
        elif 'y' in items[0]:
            y = int(items[0][2:])
            if y > max_y:
                max_y = y
            start_x, end_x = map(int, items[1][2:].split('..'))
            for x in range(start_x, end_x + 1):
                if x < min_x:
                    min_x = x
                elif x > max_x:
                    max_x = x
                grid[y][x] = '#'

    # Need a little buffer here
    min_x -= 5
    max_x += 5

    # Debug print out grid
    # for y in range(0, max_y + 2):
    #     for x in range(min_x - 1, max_x + 2):
    #         print(grid[y][x], end='')
    #     print()
    # print("Map size is x={0!s}-{1!s}, y=0-{2!s}".format(min_x, max_x, max_y))
    # print()


    # Recursion doesn't work here because it goes beyond the limits of what the computer can do, so we
    # need to do it a different way. This time we will use a queue for determining which spots we need
    # to start from. That spot will recurse left and right if necessary, but going up and down will be done
    # via the queue
    queue = deque()

    def flow_down(x, y):
        # First, if we are beyond the max, then just stop here
        if x < min_x or x > max_x or y > max_y:
            return True

        # Check what the current space is
        space = grid[y][x]
        if space == '.':
            # This is sand, so we need to check the space below for more sand
            grid[y][x] = '|'
            if grid[y + 1][x] == '.':
                # We can go down, so add to queue
                queue.append((x, y + 1))
                return True
            elif grid[y + 1][x] == '|':
                # The space below is already water, so it must have been covered by another path
                return True
            else:
                # Space below is not sand, must be clay so try to go left and right
                free_left = flow_left(x - 1, y)
                free_right = flow_right(x + 1, y)
                if free_left or free_right:
                    # Either left or right is free, so we just return
                    return True
                else:
                    # Neither left nor right is free, so we turn them to standing water and put the
                    # space above back on the queue
                    flow_left(x - 1, y, True)
                    flow_right(x + 1, y, True)
                    grid[y][x] = '~'
                    queue.append((x, y - 1))
                    return False
        elif space == '|':
            # This is water, so we have been here already, check space below to see if we are going back
            # up or if this is repeating. If it's wall or standing water below, we want to try left and
            # right, but for sand or water, just ignore
            if grid[y + 1][x] == '.' or grid[y + 1][x] == '|':
                return True
            free_left = flow_left(x - 1, y)
            free_right = flow_right(x + 1, y)
            if free_left or free_right:
                # Either left or right is free, so we just return
                return True
            else:
                # Neither left nor right is free, so we turn them to standing water and put the space
                # above back on the queue
                flow_left(x - 1, y, True)
                flow_right(x + 1, y, True)
                grid[y][x] = '~'
                queue.append((x, y - 1))
                return False
        elif space == '~':
            # This is standing water, so this area has already been processed, try to go back up if
            # possible
            queue.append((x, y - 1))
            return True
        else:
            print("We hit a weird state, investigate {0!s},{1!s}".format(x,y))
            return False

    def flow_left(x, y, set_standing=False):
        # Check the space
        space = grid[y][x]
        if space == '#':
            # We hit clay, so return that this is blocked
            return False
        elif space == '|':
            # This is existing water, make it standing if asked, then treat it like a sand spot
            if set_standing:
                grid[y][x] = '~'
            if grid[y + 1][x] == '.':
                queue.append((x, y + 1))
                return True
            elif grid[y + 1][x] == '|':
                return True
            else:
                return flow_left(x - 1, y, set_standing)
        elif space == '~':
            # Ignore standing water
            return flow_left(x - 1, y)
        elif space == '.':
            # This is sand, so check to see if we can flow down, if yes then add to queue, otherwise
            # continue left
            grid[y][x] = '|'
            if grid[y + 1][x] == '.':
                # We can go down, so add to queue
                queue.append((x, y + 1))
                return True
            elif grid[y + 1][x] == '|':
                # Water is already flowing this way, so we are good
                return True
            else:
                return flow_left(x - 1, y)

        return False

    def flow_right(x, y, set_standing=False):
        # Check the space
        space = grid[y][x]
        if space == '#':
            # We hit clay, so return that this is blocked
            return False
        elif space == '|':
            # This is existing water, make it standing if asked, then treat it like a sand spot
            if set_standing:
                grid[y][x] = '~'
            if grid[y + 1][x] == '.':
                queue.append((x, y + 1))
                return True
            elif grid[y + 1][x] == '|':
                return True
            else:
                return flow_right(x + 1, y, set_standing)
        elif space == '~':
            # Ignore standing water
            return flow_right(x + 1, y)
        elif space == '.':
            # This is sand, so check to see if we can flow down, if yes then add to queue, otherwise
            # continue left
            grid[y][x] = '|'
            if grid[y + 1][x] == '.':
                # We can go down, so add to queue
                queue.append((x, y + 1))
                return True
            elif grid[y + 1][x] == '|':
                # Water is already flowing this way, so we are good
                return True
            else:
                return flow_right(x + 1, y)

        return False

    # Start the flow of water below the fountain
    queue.append((500, 1))
    count = 0
    while len(queue) > 0:
        count += 1
        # for y in range(72,91):
        #     for x in range(490,515):
        #         print(grid[y][x], end='')
        #     print()
        # print()
        x,y = queue.popleft()
        flow_down(x, y)

    # Print out grid again
    # for y in range(0, max_y + 2):
    #     print("{0!s:>4}".format(y), end='')
    #     for x in range(min_x - 1, max_x + 2):
    #         print(grid[y][x], end='')
    #     print()

    # Print out answer
    water_tiles = 0
    standing_water_tiles = 0
    for row in grid:
        for cell in row:
            if cell == '|' or cell == '~':
                water_tiles += 1
            if cell == '~':
                standing_water_tiles += 1

    print("Number of water tiles: {0!s}".format(water_tiles))
    print("Number of standing water tiles: {0!s}".format(standing_water_tiles))
    return water_tiles, standing_water_tiles


def part1(values):
    return waterfall_hell(values)[0]


def part2(values):
    return waterfall_hell(values)[1]
