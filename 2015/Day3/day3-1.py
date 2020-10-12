# Determine how many locations on an infinite grid get visited using the defined instructions

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    #return ">"
    #return "^>v<"
    return "^v^v^v^v^v"

if __name__ == '__main__':
    print("Starting Day3-1")
    # Read file into single line of values
    values = read_file('input.txt')
    #values = test_data()

    # Visited locations will be determined by a dictionary with keys as coordinates
    # Starts automatically with the origin location
    locations = {(0,0): 1}

    # Iterate through each instruction and add the coordinates to the locations map
    x_coord = 0
    y_coord = 0
    for direction in values:
        if direction == '^':
            y_coord += 1
        elif direction == 'v':
            y_coord -= 1
        elif direction == '<':
            x_coord -= 1
        elif direction == '>':
            x_coord += 1

        current = (x_coord, y_coord)
        if current in locations:
            locations[current] += 1
        else:
            locations[current] = 1

    # Print out answer
    print("The number of houses visited is: {0}".format(str(len(locations.keys()))))
