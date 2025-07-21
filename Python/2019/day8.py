# Decode an image

def check_image(values):
    pixels = list(values[0])
    width = 25
    height = 6
    if len(pixels) == 12:
        width = 3
        height = 2

    # We only need to get the values for each layer, dimensions don't matter yet
    layers = []
    for start in range(0, len(pixels), (width * height)):
        layers.append(pixels[start:start + (width * height)])

    lowest_layer = layers[0]
    for index, layer in enumerate(layers):
        if layer.count('0') < lowest_layer.count('0'):
            lowest_layer = layer

    return lowest_layer.count('1') * lowest_layer.count('2')


def print_image(values):
    pixels = list(values[0])
    width = 25
    height = 6

    # We only need to get the values for each layer, dimensions don't matter yet
    layers = []
    for start in range(0, len(pixels), (width * height)):
        layers.append(pixels[start:start + (width * height)])

    # Determine the first visible value for each position in the layer
    final_layer = []
    for index in range(len(layers[0])):
        for depth in range(len(layers)):
            if layers[depth][index] != '2':
                final_layer.append(layers[depth][index])
                break

    # Now print out the layer
    message = [' ' if x == '0' else '#' for x in final_layer]
    print()
    for row in range(height):
        print(''.join(message[width * row:width * row + width]))


def part1(values):
    return check_image(values)


def part2(values):
    return print_image(values)
