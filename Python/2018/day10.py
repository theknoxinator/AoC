# Determine the message being written in the sky by points moving at a constant velocity and intersect at
# one second to display the message

def write_message(values):
    # First, take all initial values and put them into two arrays for easy lookup (can't use dictionary
    # as points will cross each other and cancel out)
    positions = []
    velocities = []
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for val in values:
        items = val.replace(',', '').replace('<', ' ').replace('>', ' ').split()
        x,y = int(items[1]), int(items[2])
        velocity = (int(items[4]), int(items[5]))
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y
        positions.append((x,y))
        velocities.append(velocity)

    # Now, have the points move each "second", print out the new positions, and only continue on user input
    last_min_x = 0
    last_min_y = 0
    last_max_x = 0
    last_max_y = 0
    last_x_diff = abs(max_x - min_x)
    last_y_diff = abs(max_y - min_y)
    seconds = 0
    while True:
        min_x = 99999
        min_y = 99999
        max_x = -99999
        max_y = -99999
        new_positions = []
        for index in range(len(positions)):
            # Move the point by the velocity
            point = positions[index]
            velocity = velocities[index]
            x,y = (point[0] + velocity[0], point[1] + velocity[1])

            # Find the new mins/maxes
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y

            # Save the point
            new_positions.append((x,y))

        # In order to determine which one is the message, we check the new mins/maxes against the previous
        # one, and as long as they continue to shrink, we are getting closer to the message
        # If the new mins/maxes are getting farther apart, then we need to stop
        x_diff = abs(max_x - min_x)
        y_diff = abs(max_y - min_y)

        if x_diff < last_x_diff and y_diff < last_y_diff:
            last_min_x = min_x
            last_min_y = min_y
            last_max_x = max_x
            last_max_y = max_y
            last_x_diff = x_diff
            last_y_diff = y_diff
            positions = new_positions
            seconds += 1
        else:
            break

    # Print out the final state
    for row in range(last_min_y - 2, last_max_y + 3):
        for col in range(last_min_x - 2, last_max_x + 3):
            if (col, row) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print('', flush=True)
    return seconds


def part1(values):
    return write_message(values)


def part2(values):
    return write_message(values)
