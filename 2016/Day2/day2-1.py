# Get the bathroom passcode based on inputs from file
# Keypad is standard 1-9, arranged in 3x3 grid, instructions show which way to go: up, down, left, right
# Grid does not wrap so moves into wall are ignored

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["ULL", "RRDDD", "LURDL", "UUUUD"]

KEYS = {
    (0,0): "1",
    (1,0): "2",
    (2,0): "3",
    (0,1): "4",
    (1,1): "5",
    (2,1): "6",
    (0,2): "7",
    (1,2): "8",
    (2,2): "9"
}

if __name__ == '__main__':
    print("Starting Day2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Go through directions to find each key to press (start at 5 key)
    x_coord = 1
    y_coord = 1
    passcode = ""
    for val in values:
        # Iterate each direction in line
        for letter in val:
            if letter == 'U':
                if y_coord == 0:
                    pass
                else:
                    y_coord -= 1
            elif letter == 'D':
                if y_coord == 2:
                    pass
                else:
                    y_coord += 1
            elif letter == 'L':
                if x_coord == 0:
                    pass
                else:
                    x_coord -= 1
            elif letter == 'R':
                if x_coord == 2:
                    pass
                else:
                    x_coord += 1

        print("Adding key at location ({0}, {1})".format(str(x_coord), str(y_coord)))
        passcode = passcode + KEYS[(x_coord, y_coord)]

    # Print out answer
    print("The passcode is: {0}".format(passcode))
