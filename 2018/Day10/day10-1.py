# Determine the message being written in the sky by points moving at a constant velocity and intersect at
# one second to display the message

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["position=< 9,  1> velocity=< 0,  2>",
            "position=< 7,  0> velocity=<-1,  0>",
            "position=< 3, -2> velocity=<-1,  1>",
            "position=< 6, 10> velocity=<-2, -1>",
            "position=< 2, -4> velocity=< 2,  2>",
            "position=<-6, 10> velocity=< 2, -2>",
            "position=< 1,  8> velocity=< 1, -1>",
            "position=< 1,  7> velocity=< 1,  0>",
            "position=<-3, 11> velocity=< 1, -2>",
            "position=< 7,  6> velocity=<-1, -1>",
            "position=<-2,  3> velocity=< 1,  0>",
            "position=<-4,  3> velocity=< 2,  0>",
            "position=<10, -3> velocity=<-1,  1>",
            "position=< 5, 11> velocity=< 1, -2>",
            "position=< 4,  7> velocity=< 0, -1>",
            "position=< 8, -2> velocity=< 0,  1>",
            "position=<15,  0> velocity=<-2,  0>",
            "position=< 1,  6> velocity=< 1,  0>",
            "position=< 8,  9> velocity=< 0, -1>",
            "position=< 3,  3> velocity=<-1,  1>",
            "position=< 0,  5> velocity=< 0, -1>",
            "position=<-2,  2> velocity=< 2,  0>",
            "position=< 5, -2> velocity=< 1,  2>",
            "position=< 1,  4> velocity=< 2,  1>",
            "position=<-2,  7> velocity=< 2, -2>",
            "position=< 3,  6> velocity=<-1, -1>",
            "position=< 5,  0> velocity=< 1,  0>",
            "position=<-6,  0> velocity=< 2,  0>",
            "position=< 5,  9> velocity=< 1, -2>",
            "position=<14,  7> velocity=<-2,  0>",
            "position=<-3,  6> velocity=< 2, -1>"]

if __name__ == '__main__':
    print("Starting Day10-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

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

    # Print out the initial state
    '''
    for row in range(min_y - 2, max_y + 3):
        for col in range(min_x - 2, max_x + 3):
            if (col,row) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print('', flush=True)
    print()
    '''

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
    print("Number of seconds it took: {0!s}".format(seconds))
