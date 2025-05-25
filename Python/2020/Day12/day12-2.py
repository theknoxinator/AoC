# Determine how far the ship gets after following a bunch of movement instructions

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["F10", "N3", "F7", "R90", "F11"]


print("Starting Day12-2")
values = read_file("input.txt")
# values = test_data()

# Ship starts at 0,0, looking to the E
# Waypoint starts at 10, -1 (east 10, north 1)
direction = 'E'
x, y = 0, 0
point_x, point_y = 10, -1
for val in values:
    instruction = val[0]
    number = int(val[1:])

    # If the instruction is F, then we move that number of waypoints
    if instruction == 'F':
        for times in range(number):
            x += point_x
            y += point_y

    if instruction == 'N':
        # Move waypoint north (negative y)
        point_y -= number
    elif instruction == 'S':
        # Move waypoint south (positive y)
        point_y += number
    elif instruction == 'W':
        # Move waypoint west (negative x)
        point_x -= number
    elif instruction == 'E':
        # Move waypoint east (positive x)
        point_x += number

    # For the R and L instructions, we convert the degrees into turns then loop that number of times in the direction
    turns = int(number / 90)
    for turn in range(turns):
        if instruction == 'L':
            # 10, -4 -> -4, -10 -> -10, 4 -> 4, 10 -> 10, -4
            old_x, old_y = point_x, point_y
            point_x = old_y
            point_y = -old_x
        elif instruction == 'R':
            # 10, -4 -> 4, 10 -> -10, 4 -> -4, -10 -> 10, -4
            old_x, old_y = point_x, point_y
            point_x = -old_y
            point_y = old_x

# After doing all the movements, figure out the distance traveled
print("Ending location is: {0!s}, {1!s}".format(x, y))
print("Ending distance is: {0!s}".format(abs(x) + abs(y)))
