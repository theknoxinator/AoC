# Determine how far away a hex is


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return [x for x in line.split(',')]


def test_data():
    # return ["ne", "ne", "ne"]
    # return ["ne", "ne", "sw", "sw"]
    # return ["ne", "ne", "s", "s"]
    return ["se", "sw", "se", "sw", "sw"]


print("Starting Day11-1")
values = read_file("input.txt")
# values = test_data()

# The way a hex grid works, moving up or down, you move 2 on the y axis, and any other direction moves 1 in both axes
x,y = 0,0
for val in values:
    if val == 'n':
        y += 2
    elif val == 's':
        y -= 2
    elif val == 'nw':
        x -= 1
        y += 1
    elif val == 'ne':
        x += 1
        y += 1
    elif val == 'sw':
        x -= 1
        y -= 1
    elif val == 'se':
        x += 1
        y -= 1

# To get the distance, it is as simple as adding the x and y ranges, then dividing by 2
distance = int((abs(x) + abs(y)) / 2)

print("The distance is: {0!s}".format(distance))