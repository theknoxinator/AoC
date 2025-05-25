# Decode an image

def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            return line.strip()


def test_data():
    pass


print("Starting Day 8-2")
values = read_file('input.txt')

width = 25
height = 6

# We only need to get the values for each layer, dimensions don't matter yet
layers = []
for start in range(0, len(values), (width * height)):
    layers.append(values[start:start + (width * height)])

# Determine the first visible value for each position in the layer
final_layer = []
for index in range(len(layers[0])):
    for depth in range(len(layers)):
        if layers[depth][index] != '2':
            final_layer.append(layers[depth][index])
            break

# Now print out the layer
message = [' ' if x == '0' else '#' for x in final_layer]
for row in range(height):
    print(''.join(message[width * row:width * row + width]))
