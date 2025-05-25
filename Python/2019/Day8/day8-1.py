# Decode an image

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return line.strip()


def test_data():
    pass


print("Starting Day 8")
values = read_file('input.txt')

width = 25
height = 6

# We only need to get the values for each layer, dimensions don't matter yet
layers = []
for start in range(0, len(values), (width * height)):
    layers.append(values[start:start + (width * height)])

lowest_layer = layers[0]
for index, layer in enumerate(layers):
    print("Layer {0!s}: {1!s}".format(index, layer))
    print("Layer has {0!s} zeroes, {1!s} ones, {2!s} twos".format(layer.count('0'), layer.count('1'), layer.count('2')))
    if layer.count('0') < lowest_layer.count('0'):
        lowest_layer = layer

print("The layer with fewest zeroes is: {0!s}".format(lowest_layer))
print("The ones times twos in this layer is: {0!s}".format(lowest_layer.count('1') * lowest_layer.count('2')))
