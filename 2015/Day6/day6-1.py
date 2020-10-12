# Turn on or turn off lights based on instructions

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            items = line.split()
            if len(items) > 4:
                items.pop(0)
            values.append(items)

    return values

def test_data():
    return [["on", "0,0", "through", "999,999"],
            ["toggle", "0,0", "through", "999,0"],
            ["off", "499,499", "through", "500,500"]]

if __name__ == '__main__':
    print("Starting Day6-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Create 1000x1000 grid
    lights = [[' ']*1000 for i in range(1000)]

    # Iterate and apply values to grid
    for val in values:
        start_coords = list(map(int, val[1].split(',')))
        end_coords = list(map(int, val[3].split(',')))
        if val[0] == "on":
            for i in range(start_coords[1], end_coords[1]+1):
                for j in range(start_coords[0], end_coords[0]+1):
                    lights[i][j] = '#'
        elif val[0] == "off":
            for i in range(start_coords[1], end_coords[1]+1):
                for j in range(start_coords[0], end_coords[0]+1):
                    lights[i][j] = ' '
        elif val[0] == "toggle":
            for i in range(start_coords[1], end_coords[1]+1):
                for j in range(start_coords[0], end_coords[0]+1):
                    if lights[i][j] == ' ':
                        lights[i][j] = '#'
                    else:
                        lights[i][j] = ' '

    # Go through grid and determine number of lights on
    lights_on = 0
    for row in lights:
        for cell in row:
            if cell == '#':
                lights_on += 1

    # Print out answer
    for row in lights:
        print(''.join(row))

    print("The number of lights on is: {0}".format(str(lights_on)))