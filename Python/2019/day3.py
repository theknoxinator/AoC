# Plot out two wires and see where they cross, and output the closest cross
import sys

def cross_wires(values, use_part2=False):
    first_line = values[0].split(',')
    second_line = values[1].split(',')

    # We will only plot out the first line, then just go through the second line and determine where the crosses are
    crosses = dict()
    points = dict()
    x,y = 0,0
    steps = 0

    for val in first_line:
        direction, amount = val[:1], int(val[1:])
        for i in range(amount):
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            steps += 1
            points[(x,y)] = steps

    x,y = 0,0
    steps = 0
    for val in second_line:
        direction, amount = val[:1], int(val[1:])
        for i in range(amount):
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            steps += 1
            if (x,y) in points:
                crosses[(x,y)] = steps + points[(x,y)]

    shortest_distance = sys.maxsize
    if not use_part2:
        for val in crosses.keys():
            distance = abs(val[0]) + abs(val[1])
            shortest_distance = min(shortest_distance, distance)
    else:
        for val in crosses.values():
            shortest_distance = min(shortest_distance, val)

    return shortest_distance


def part1(values):
    return cross_wires(values)


def part2(values):
    return cross_wires(values, True)
