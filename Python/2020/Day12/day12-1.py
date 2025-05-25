# Determine how far the ship gets after following a bunch of movement instructions

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["F10", "N3", "F7", "R90", "F11"]


print("Starting Day12-1")
values = read_file("input.txt")
# values = test_data()

# Ship starts at 0,0, looking to the E
direction = 'E'
x, y = 0, 0
for val in values:
    instruction = val[0]
    number = int(val[1:])
    # If the instruction is F, then we just convert it to the direction we are facing
    if instruction == 'F':
        instruction = direction

    if instruction == 'N':
        # Go north (negative y)
        y = y - number
    elif instruction == 'S':
        # Go south (positive y)
        y = y + number
    elif instruction == 'W':
        # Go west (negative x)
        x = x - number
    elif instruction == 'E':
        # Go east (positive x)
        x = x + number

    # For the R and L instructions, we convert the degrees into turns then loop that number of times in the direction
    turns = int(number / 90)
    for turn in range(turns):
        if instruction == 'L':
            if direction == 'N':
                direction = 'W'
            elif direction == 'W':
                direction = 'S'
            elif direction == 'S':
                direction = 'E'
            elif direction == 'E':
                direction = 'N'
        elif instruction == 'R':
            if direction == 'N':
                direction = 'E'
            elif direction == 'E':
                direction = 'S'
            elif direction == 'S':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'

# After doing all the movements, figure out the distance traveled
print("Ending location is: {0!s}, {1!s}".format(x, y))
print("Ending distance is: {0!s}".format(abs(x) + abs(y)))
