# Find the number of viable pairs of nodes in the server grid based on disc free dump in file

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


if __name__ == "__main__":
    print("Starting Day 22-1")
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
        print(', '.join([str(node.avail) for node in row]))

    # We don't need the grid for this first problem, so we're just going to use the list
    pairs = 0
    for i in range(len(full_list)):
        for j in range(i + 1, len(full_list)):
            first = full_list[i]
            second = full_list[j]
            if first.used > 0 and first.used <= second.avail:
                print("{0!s} is less than {1!s}".format(first.used, second.avail))
                print("Indexes: {0!s}, {1!s}".format(i, j))
                pairs += 1
            elif second.used > 0 and second.used <= first.avail:
                print("{0!s} is less than {1!s}".format(second.used, first.avail))
                print("Indexes: {0!s}, {1!s}".format(i, j))
                pairs += 1

    print("Total number of pairs: {0!s}".format(pairs))
