# Find the best monitoring station
from math import gcd


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())
    return values


print("Starting Day10-2")
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
highest_targets = None
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
        highest_targets = targets

print("The asteroid with most detected is {0!s} with {1!s} targets".format(highest_asteroid, highest_detections))

print("  {0}".format(' '.join([str(x % 10) for x in range(width)])))
print()
for y in range(height):
    print("{0!s} {1}".format(y % 10, ' '.join(values[y])))
    print()

# Try to break up targets into quadrants and sort by angle
quadrant1 = {}
quadrant2 = {}
quadrant3 = {}
quadrant4 = {}
for target, visible in highest_targets.items():
    if not visible:
        continue
    diff_x = target[0] - highest_asteroid[0]
    diff_y = target[1] - highest_asteroid[1]
    if diff_x == 0 and diff_y < 0:
        quadrant1[target] = height
    elif diff_x > 0 and diff_y < 0:
        quadrant1[target] = abs(diff_y / float(diff_x))
    elif diff_x > 0 and diff_y == 0:
        quadrant2[target] = width
    elif diff_x > 0 and diff_y > 0:
        quadrant2[target] = abs(diff_x / float(diff_y))
    elif diff_x == 0 and diff_y > 0:
        quadrant3[target] = height
    elif diff_x < 0 and diff_y > 0:
        quadrant3[target] = abs(diff_y / float(diff_x))
    elif diff_x < 0 and diff_y == 0:
        quadrant4[target] = width
    elif diff_x < 0 and diff_y < 0:
        quadrant4[target] = abs(diff_x / float(diff_y))

sorted_quadrant1 = {k: v for k, v in sorted(quadrant1.items(), key=lambda item: item[1], reverse=True)}
sorted_quadrant2 = {k: v for k, v in sorted(quadrant2.items(), key=lambda item: item[1], reverse=True)}
sorted_quadrant3 = {k: v for k, v in sorted(quadrant3.items(), key=lambda item: item[1], reverse=True)}
sorted_quadrant4 = {k: v for k, v in sorted(quadrant4.items(), key=lambda item: item[1], reverse=True)}
offset = 1
for item in enumerate(sorted_quadrant1.items()):
    print("{0!s}: {1!s}: {2!s}".format(offset, item[0], item[1]))
    offset += 1
for item in enumerate(sorted_quadrant2.items()):
    print("{0!s}: {1!s}: {2!s}".format(offset, item[0], item[1]))
    offset += 1
for item in enumerate(sorted_quadrant3.items()):
    print("{0!s}: {1!s}: {2!s}".format(offset, item[0], item[1]))
    offset += 1
for item in enumerate(sorted_quadrant4.items()):
    print("{0!s}: {1!s}: {2!s}".format(offset, item[0], item[1]))
    offset += 1
