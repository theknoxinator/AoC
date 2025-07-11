# Determine the sum of all metadata in a tree represented by a file containing a sequence of numbers

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.metadata = []

    def add_child(self, node):
        self.children.append(node)

    def add_metadata(self, metadata):
        self.metadata.append(metadata)


# Define a recursive function that will create nodes based on the data and use a global index
def create_node(numbers, index, name_index):
    new_node = Node(str(name_index))
    name_index += 1

    # Get number of children
    children = numbers[index]
    index += 1

    # Get number of metadata values
    metadata = numbers[index]
    index += 1

    # If children > 0, create those nodes first
    for child in range(children):
        child_node, index, name_index = create_node(numbers, index, name_index)
        new_node.add_child(child_node)

    # If metadata > 0, add those to the node
    for data in range(metadata):
        new_node.add_metadata(numbers[index])
        index += 1

    return new_node, index, name_index


def calc_metadata(values, use_part2=False):
    # First, split values into an array of ints for easy reading and navigating
    numbers = list(map(int, values[0].split()))

    # Start the recursion
    index = 0
    name_index = 0
    root, _, _ = create_node(numbers, index, name_index)

    # Print out answer
    def sum_metadata(node):
        sum = 0
        for child in node.children:
            sum += sum_metadata(child)

        for metadata in node.metadata:
            sum += metadata

        return sum

    def sum_metadata2(node):
        sum = 0

        # If no children, just sum up metadata as before
        if len(node.children) == 0:
            for metadata in node.metadata:
                sum += metadata
            return sum

        # If has children, metadata refers to which children need to be added to sum
        for metadata in node.metadata:
            if metadata > len(node.children):
                continue
            sum += sum_metadata(node.children[metadata - 1])

        return sum

    return sum_metadata2(root) if use_part2 else sum_metadata(root)


def part1(values):
    return calc_metadata(values)


def part2(values):
    return calc_metadata(values, True)
