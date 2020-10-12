# Find the best monitoring station
from math import gcd


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())
    return values


print("Starting Day10")
values = read_file('input5.txt')

# First, go through the input and capture the coordinates of each asteroid
width = len(values[0])
height = len(values)
coordinates = set()
for y in range(height):
    for x in range(width):
        if values[y][x] == '#':
            coordinates.add((x, y))

# Now go through each coordinate and see how many detections it has
highest_detections = 0
highest_asteroid = None
for asteroid in coordinates:
    targets = dict([(coord, True) for coord in coordinates])
    for target in targets.keys():
        if asteroid == target:
            targets[target] = False
            continue
        diff_x = target[0] - asteroid[0]
        diff_y = target[1] - asteroid[1]
        divider = gcd(diff_x, diff_y)
        diff_x /= divider
        diff_y /= divider
        check_x = target[0] + diff_x
        check_y = target[1] + diff_y
        while 0 <= check_x < width and 0 <= check_y < height:
            if (check_x, check_y) in targets:
                targets[(check_x, check_y)] = False
            check_x += diff_x
            check_y += diff_y
    detections = 0
    for visible in targets.values():
        if visible:
            detections += 1

    if detections > highest_detections:
        highest_detections = detections
        highest_asteroid = asteroid

print("The asteroid with most detected is {0!s} with {1!s} targets".format(highest_asteroid, highest_detections))
