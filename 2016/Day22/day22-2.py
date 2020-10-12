# Find the smallest number of steps it takes to move data from the top-right corner to the top-left corner

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


if __name__ == "__main__":
    print("Starting Day 22-2")
    values = read_file("input.txt")

    class Node:
        def __init__(self, used, avail, total):
            self.used = used
            self.avail = avail
            self.total = total

    # We need to set up the grid of nodes with the space stats
    grid = [[None]*37 for i in range(27)]
    full_list = []
    # Skip the first couple lines
    for val in values[2:]:
        # First, determine which node it is
        parts = val.split()
        _, x, y = parts[0].split('-')
        x = int(x[1:])
        y = int(y[1:])

        # Now create the node in the grid
        used = int(parts[2][:-1])
        avail = int(parts[3][:-1])
        total = int(parts[1][:-1])
        grid[y][x] = Node(used, avail, total)
        full_list.append(Node(used, avail, total))

    # Print out stuff
    for row in grid:
        print(', '.join(["{0!s}({1!s})".format(node.total, node.used) for node in row]))


