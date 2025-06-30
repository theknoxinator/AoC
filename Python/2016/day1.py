# Find distance from start to end based on inputs from file
# Left and Right rotate 90 degrees in that direction, number indicates number of blocks to go in the current direction

def get_location(values):
    # Iterate and apply values to location
    x_coord = 0
    y_coord = 0
    direction = 0 # modulo: north = 0, east = 1, south = 2, west = 3
    past_intersections = {(0, 0)}
    repeat_intersections = []
    for val in values:
        if val[0] == 'R':
            direction += 1
        elif val[0] == 'L':
            direction -= 1

        if direction % 4 == 0:
            # Going north
            for num in range(int(val[1:])):
                y_coord += 1
                intersection = (x_coord, y_coord)
                if intersection in past_intersections:
                    repeat_intersections.append(intersection)
                past_intersections.add(intersection)
        elif direction % 4 == 1:
            # Going east
            for num in range(int(val[1:])):
                x_coord += 1
                intersection = (x_coord, y_coord)
                if intersection in past_intersections:
                    repeat_intersections.append(intersection)
                past_intersections.add(intersection)
        elif direction % 4 == 2:
            # Going south
            for num in range(int(val[1:])):
                y_coord -= 1
                intersection = (x_coord, y_coord)
                if intersection in past_intersections:
                    repeat_intersections.append(intersection)
                past_intersections.add(intersection)
        elif direction % 4 == 3:
            # Going west
            for num in range(int(val[1:])):
                x_coord -= 1
                intersection = (x_coord, y_coord)
                if intersection in past_intersections:
                    repeat_intersections.append(intersection)
                past_intersections.add(intersection)

    total_blocks = abs(x_coord) + abs(y_coord)
    repeat_blocks = abs(repeat_intersections[0][0]) + abs(repeat_intersections[0][1]) if repeat_intersections else 0
    return total_blocks, repeat_blocks


def part1(values):
    return get_location(values[0].replace(' ', '').split(','))[0]


def part2(values):
    return get_location(values[0].replace(' ', '').split(','))[1]
