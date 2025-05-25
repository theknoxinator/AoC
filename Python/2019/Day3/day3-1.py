# Plot out two wires and see where they cross, and output the closest cross
import sys

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.split(','))

    return values

def test_data():
    # return [["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]]
    # return [["R75","D30","R83","U83","L12","D49","R71","U7","L72"], ["U62","R66","U55","R34","D71","R55","D58","R83"]]
    return [["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
            ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]]

print("Starting Day3")
values = read_file('input.txt')
# values = test_data()

first_line = values[0]
second_line = values[1]

# We will only plot out the first line, then just go through the second line and determine where the crosses are
crosses = set()
points = set()
x,y = 0,0

print("Plot first line")
for val in first_line:
    direction, amount = val[:1], int(val[1:])
    print("Go {0} for {1!s} spaces".format(direction, amount))
    for i in range(amount):
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        points.add((x, y))

print()
print("Plot second line")
x,y = 0,0
for val in second_line:
    direction, amount = val[:1], int(val[1:])
    print("Go {0} for {1!s} spaces".format(direction, amount))
    for i in range(amount):
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        if (x,y) in points:
            crosses.add((x,y))
            print("Found cross at {0!s},{1!s}".format(x, y))

shortest_distance = sys.maxsize
for val in crosses:
    distance = abs(val[0]) + abs(val[1])
    if distance < shortest_distance:
        shortest_distance = distance

print("The shortest distance is {0!s}".format(shortest_distance))
