# Increase or decrease brightness of lights based on inputs

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
    return [["on", "0,0", "through", "0,0"],
            ["toggle", "0,0", "through", "999,999"]]

if __name__ == '__main__':
    print("Starting Day6-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Create 1000x1000 grid
    lights = [[0]*1000 for i in range(1000)]

    # Iterate and apply values to grid
    for val in values:
        start_coords = list(map(int, val[1].split(',')))
        end_coords = list(map(int, val[3].split(',')))
        if val[0] == "on":
            for i in range(start_coords[1], end_coords[1]+1):
                for j in range(start_coords[0], end_coords[0]+1):
                    lights[i][j] += 1
        elif val[0] == "off":
            for i in range(start_coords[1], end_coords[1]+1):
                for j in range(start_coords[0], end_coords[0]+1):
                    if lights[i][j] == 0:
                        continue
                    lights[i][j] -= 1
        elif val[0] == "toggle":
            for i in range(start_coords[1], end_coords[1]+1):
                for j in range(start_coords[0], end_coords[0]+1):
                    lights[i][j] += 2

    # Go through grid and determine the brightness of all lights
    brightness = 0
    for row in lights:
        for cell in row:
            brightness += cell

    # Print out answer
    print("The brightness of lights on is: {0}".format(str(brightness)))