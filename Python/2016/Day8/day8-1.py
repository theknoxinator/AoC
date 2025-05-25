# Determine the two-factor code trying to be displayed based on instructions of how to light up and move
# pixels on a screen

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["rect 3x2",
            "rotate column x=1 by 1",
            "rotate row y=0 by 4",
            "rotate column x=1 by 1"]


if __name__ == '__main__':
    print("Starting Day 8-1")
    values = read_file('input.txt')
    # values = test_data()

    # We start with a blank screen that is 50 columns wide and 6 rows high
    width = 50
    height = 6
    screen = [['.'] * width for i in range(height)]

    # Now go through each instruction and do what it says
    for val in values:
        # Determine what kind of instruction it is and perform the operation
        if "rect" in val:
            # We are just defining a rectangle of pixels to light up
            cols,rows = val.split()[1].split('x')
            for y in range(int(rows)):
                for x in range(int(cols)):
                    screen[y][x] = '#'

        elif "row" in val:
            # We need to rotate a row, which is as easy as splitting the row and recombining it
            row = int(val.split()[2][2:])
            offset = int(val.split()[4])

            screen[row] = screen[row][-offset:] + screen[row][:(width - offset)]

        elif "column" in val:
            # We need to rotate a column, which is much more difficult. We will copy the column into a
            # separate list, rotate that like a row, and then copy it back into the screen
            col = int(val.split()[2][2:])
            offset = int(val.split()[4])

            copy = []
            for y in range(height):
                copy.append(screen[y][col])

            copy = copy[-offset:] + copy[:(height - offset)]
            for y in range(height):
                screen[y][col] = copy[y]

        # Debug print out screen
        for row in screen:
            print(''.join(row))
        print()

    # Print out the number of lit pixels
    total_lit = 0
    for row in screen:
        for cell in row:
            if cell == '#':
                total_lit += 1
    print("The number of lit pixels is: {0!s}".format(total_lit))
