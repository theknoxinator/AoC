# Get the bathroom passcode based on inputs from file
# Keypad is 1-9 and A-D, arranged in 5x5 diamond, instructions show which way to go: up, down, left, right
# Grid does not wrap so moves onto spaces where there is no key are ignored

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["ULL", "RRDDD", "LURDL", "UUUUD"]

KEYS = {
    (2,0): "1",
    (1,1): "2",
    (2,1): "3",
    (3,1): "4",
    (0,2): "5",
    (1,2): "6",
    (2,2): "7",
    (3,2): "8",
    (4,2): "9",
    (1,3): "A",
    (2,3): "B",
    (3,3): "C",
    (2,4): "D"
}

if __name__ == '__main__':
    print("Starting Day2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Go through directions to find each key to press (start at 5 key)
    x_coord = 0
    y_coord = 2
    passcode = ""
    for val in values:
        # Iterate each direction in line
        for letter in val:
            if letter == 'U':
                temp = y_coord - 1
                if (x_coord, temp) in KEYS:
                    y_coord = temp
            elif letter == 'D':
                temp = y_coord + 1
                if (x_coord, temp) in KEYS:
                    y_coord = temp
            elif letter == 'L':
                temp = x_coord - 1
                if (temp, y_coord) in KEYS:
                    x_coord = temp
            elif letter == 'R':
                temp = x_coord + 1
                if (temp, y_coord) in KEYS:
                    x_coord = temp

        print("Adding key at location ({0}, {1})".format(str(x_coord), str(y_coord)))
        passcode = passcode + KEYS[(x_coord, y_coord)]

    # Print out answer
    print("The passcode is: {0}".format(passcode))
