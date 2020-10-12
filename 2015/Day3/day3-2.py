# Determine how many locations on an infinite grid get visited using the defined instructions
# Second part: Two units are moving, taking turns

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    #return "^v"
    #return "^>v<"
    return "^v^v^v^v^v"

if __name__ == '__main__':
    print("Starting Day3-2")
    # Read file into single line of values
    values = read_file('input.txt')
    #values = test_data()

    # Visited locations will be determined by a dictionary with keys as coordinates
    # Starts automatically with the origin location
    locations = {(0,0): 1}

    # Iterate through each instruction and add the coordinates to the locations map
    x_coord = [0,0]
    y_coord = [0,0]
    iteration = 0
    for direction in values:
        unit = iteration % 2
        if direction == '^':
            y_coord[unit] += 1
        elif direction == 'v':
            y_coord[unit] -= 1
        elif direction == '<':
            x_coord[unit] -= 1
        elif direction == '>':
            x_coord[unit] += 1

        current = (x_coord[unit], y_coord[unit])
        if current in locations:
            locations[current] += 1
        else:
            locations[current] = 1

        iteration += 1

    # Print out answer
    print("The number of houses visited is: {0}".format(str(len(locations.keys()))))
