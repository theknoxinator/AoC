# Determine the IDs of the four corners of a grid of images
import math
import re


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


def find_corners(values):
    tiles = dict()
    index = 0
    while index < len(values):
        tile_number = re.search("[0-9]+", values[index]).group(0)
        tile_image = values[index + 1:index + 11]
        tiles[tile_number] = Tile(tile_number, tile_image)
        index += 12

    # Now we can iterate through each tile and check to see how many edges match up with other tiles
    corners = []
    tile_list = list(tiles.values())
    for first in range(len(tile_list)):
        edge_count = 0
        first_tile = tile_list[first]
        for second in range(len(tile_list)):
            if first == second:
                continue
            second_tile = tile_list[second]
            for first_edge in first_tile.edges.items():
                for second_edge in second_tile.edges.items():
                    if first_edge[1] == second_edge[1] or first_edge[1] == second_edge[1][::-1]:
                        edge_count += 1
        if edge_count == 2:
            corners.append(first_tile.number)

    return math.prod([int(x) for x in corners])


def part1(values):
    return find_corners(values)
