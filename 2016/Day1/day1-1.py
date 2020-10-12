# Find distance from start to end based on inputs from file
# Left and Right rotate 90 degrees in that direction, number indicates number of blocks to go in the current direction

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        line = f.readline().replace(' ', '')
        values = line.split(',')

    return values

def test_data():
    #return ['R2', 'L3']
    #return ['R2', 'R2', 'R2']
    return ['R5', 'L5', 'R5', 'R3']

if __name__ == '__main__':
    print("Starting Day1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and apply values to location
    x_coord = 0
    y_coord = 0
    direction = 0 # modulo: north = 0, east = 1, south = 2, west = 3
    for val in values:
        if val[0] == 'R':
            direction += 1
        elif val[0] == 'L':
            direction -= 1

        if direction % 4 == 0:
            # Going north
            y_coord += int(val[1:])
        elif direction % 4 == 1:
            # Going east
            x_coord += int(val[1:])
        elif direction % 4 == 2:
            # Going south
            y_coord -= int(val[1:])
        elif direction % 4 == 3:
            # Going west
            x_coord -= int(val[1:])

    print("Location is at {0}, {1}".format(x_coord, y_coord))
    total_blocks = abs(x_coord) + abs(y_coord)

    # Print out answer
    print("The number of blocks away is: {0}".format(str(total_blocks)))