# Determine the IDs of the four corners of a grid of images
import math
import re


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return read_file("sample.txt")


print("Starting Day20-1")
values = read_file("input.txt")
# values = test_data()


# For this problem we are essentially looking for the four tiles with two unmatching edges
# We will store each tile in a class to easily get the edges
class Tile:
    def __init__(self, number, image):
        self.number = number
        self.image = image
        self.edges = self.get_edges()

    def __repr__(self):
        return str(self.edges)

    def get_edges(self):
        edges = dict()
        # Get the top and bottom edges
        edges['T'] = self.image[0]
        edges['B'] = self.image[9]
        # Get the left and right edges
        left_edge, right_edge = "", ""
        for row in self.image:
            left_edge = left_edge + row[0]
            right_edge = right_edge + row[9]
        edges['L'] = left_edge
        edges['R'] = right_edge
        return edges


tiles = dict()
index = 0
while index < len(values):
    tile_number = re.search("[0-9]+", values[index]).group(0)
    tile_image = values[index + 1:index + 11]
    tiles[tile_number] = Tile(tile_number, tile_image)
    index += 12

print(tiles)

# Now we can iterate through each tile and check to see how many edges match up with other tiles
corners = []
tile_list = list(tiles.values())
for first in range(len(tile_list)):
    edge_count = 0
    first_tile = tile_list[first]
    print("Checking for tile: {0!s}".format(first_tile.number))
    for second in range(len(tile_list)):
        if first == second:
            continue
        second_tile = tile_list[second]
        print("Checking against tile: {0!s}".format(second_tile.number))
        for first_edge in first_tile.edges.items():
            for second_edge in second_tile.edges.items():
                if first_edge[1] == second_edge[1] or first_edge[1] == second_edge[1][::-1]:
                    print("{0!s} edge of {1!s} matches {2!s} edge of {3!s}".format(first_edge[0], first_tile.number,
                                                                                   second_edge[0], second_tile.number))
                    print(first_edge)
                    print(second_edge)
                    edge_count += 1
    if edge_count == 2:
        corners.append(first_tile.number)

print(corners)
print("The product of all four corners is: {0!s}".format(math.prod([int(x) for x in corners])))
