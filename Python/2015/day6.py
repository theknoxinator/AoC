# Turn on or turn off lights based on instructions
def parse_instructions(instructions):
    parts = instructions.split()
    if len(parts) > 4:
        parts.pop(0)
    return parts


def part1(values):
    # Create 1000x1000 grid
    lights = [[' '] * 1000 for i in range(1000)]

    # Iterate and apply instructions to grid
    for instructions in values:
        parts = parse_instructions(instructions)
        start_coords = list(map(int, parts[1].split(',')))
        end_coords = list(map(int, parts[3].split(',')))
        if parts[0] == "on":
            for i in range(start_coords[1], end_coords[1] + 1):
                for j in range(start_coords[0], end_coords[0] + 1):
                    lights[i][j] = '#'
        elif parts[0] == "off":
            for i in range(start_coords[1], end_coords[1] + 1):
                for j in range(start_coords[0], end_coords[0] + 1):
                    lights[i][j] = ' '
        elif parts[0] == "toggle":
            for i in range(start_coords[1], end_coords[1] + 1):
                for j in range(start_coords[0], end_coords[0] + 1):
                    if lights[i][j] == ' ':
                        lights[i][j] = '#'
                    else:
                        lights[i][j] = ' '

    # Go through grid and determine number of lights on
    lights_on = 0
    for row in lights:
        for cell in row:
            if cell == '#':
                lights_on += 1

    # Print out answer
    # for row in lights:
    #     print(''.join(row))

    return lights_on


def part2(values):
    # Create 1000x1000 grid
    lights = [[0] * 1000 for i in range(1000)]

    # Iterate and apply instructions to grid
    for instructions in values:
        parts = parse_instructions(instructions)
        start_coords = list(map(int, parts[1].split(',')))
        end_coords = list(map(int, parts[3].split(',')))
        if parts[0] == "on":
            for i in range(start_coords[1], end_coords[1] + 1):
                for j in range(start_coords[0], end_coords[0] + 1):
                    lights[i][j] += 1
        elif parts[0] == "off":
            for i in range(start_coords[1], end_coords[1] + 1):
                for j in range(start_coords[0], end_coords[0] + 1):
                    if lights[i][j] == 0:
                        continue
                    lights[i][j] -= 1
        elif parts[0] == "toggle":
            for i in range(start_coords[1], end_coords[1] + 1):
                for j in range(start_coords[0], end_coords[0] + 1):
                    lights[i][j] += 2

    # Go through grid and determine the brightness of all lights
    brightness = 0
    for row in lights:
        for cell in row:
            brightness += cell

    return brightness
