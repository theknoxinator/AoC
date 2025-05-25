# Find distance from start to end based on inputs from file
# Left and Right rotate 90 degrees in that direction, number indicates number of blocks to go in the current direction
# Find first intersection that is passed twice and get the distance

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        line = f.readline().replace(' ', '')
        values = line.split(',')

    return values

def test_data():
    return ['R8', 'R4', 'R4', 'R8']

if __name__ == '__main__':
    print("Starting Day1-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and apply values to location
    x_coord = 0
    y_coord = 0
    direction = 0 # modulo: north = 0, east = 1, south = 2, west = 3
    past_intersections = [(0,0)]
    found_repeat = False
    for val in values:
        if val[0] == 'R':
            direction += 1
        elif val[0] == 'L':
            direction -= 1

        if direction % 4 == 0:
            # Going north
            for num in range(int(val[1:])):
                y_coord += 1
                intersection = (x_coord, y_coord)
                if intersection in past_intersections:
                    found_repeat = True
                    break
                else:
                    past_intersections.append(intersection)
        elif direction % 4 == 1:
            # Going east
            for num in range(int(val[1:])):
                x_coord += 1
                intersection = (x_coord, y_coord)
                if intersection in past_intersections:
                    found_repeat = True
                    break
                else:
                    past_intersections.append(intersection)
        elif direction % 4 == 2:
            # Going south
            for num in range(int(val[1:])):
                y_coord -= 1
                intersection = (x_coord, y_coord)
                if intersection in past_intersections:
                    found_repeat = True
                    break
                else:
                    past_intersections.append(intersection)
        elif direction % 4 == 3:
            # Going west
            for num in range(int(val[1:])):
                x_coord -= 1
                intersection = (x_coord, y_coord)
                if intersection in past_intersections:
                    found_repeat = True
                    break
                else:
                    past_intersections.append(intersection)

        if found_repeat:
            break

    print("Location is at {0}, {1}".format(x_coord, y_coord))
    total_blocks = abs(x_coord) + abs(y_coord)

    # Print out answer
    print("The number of blocks away is: {0}".format(str(total_blocks)))