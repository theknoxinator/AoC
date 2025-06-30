# Find the number of viable pairs of nodes in the server grid based on disc free dump in file

class Node:
    def __init__(self, used, avail, total):
        self.used = used
        self.avail = avail
        self.total = total


def find_pairs(values):
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

    # We don't need the grid for this first problem, so we're just going to use the list
    pairs = 0
    for i in range(len(full_list)):
        for j in range(i + 1, len(full_list)):
            first = full_list[i]
            second = full_list[j]
            if first.used > 0 and first.used <= second.avail:
                pairs += 1
            elif second.used > 0 and second.used <= first.avail:
                pairs += 1

    return pairs


def part1(values):
    return find_pairs(values)


def part2(values):
    # Never implemented this
    return 0
