# Determine the sum of all metadata in a tree represented by a file containing a sequence of numbers

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    return "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

if __name__ == '__main__':
    print("Starting Day8-1")
    # Read file into values
    values = read_file('input.txt')
    #values = test_data()

    # First, split values into an array of ints for easy reading and navigating
    numbers = list(map(int, values.split()))
    print("[{0}]".format(','.join(map(str, numbers))))

    # Define a node class
    class Node:
        def __init__(self, name):
            self.name = name
            self.children = []
            self.metadata = []

        def add_child(self, node):
            self.children.append(node)

        def add_metadata(self, metadata):
            self.metadata.append(metadata)

    # Set up the global index
    index = 0
    name_index = 0

    # Define a recursive function that will create nodes based on the data and use a global index
    def create_node():
        global index
        global name_index
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
            child_node = create_node()
            new_node.add_child(child_node)

        # If metadata > 0, add those to the node
        for data in range(metadata):
            new_node.add_metadata(numbers[index])
            index += 1

        return new_node

    # Start the recursion
    root = create_node()

    # Debug print out the nodes
    def print_node(node, level):
        print("{0}{1}: [{2}]".format(' '.join(['' for i in range(level * 2)]), node.name, ','.join(map(str, node.metadata))))
        for child in node.children:
            print_node(child, level + 1)
    print_node(root, 0)

    # Print out answer
    def sum_metadata(node):
        sum = 0
        for child in node.children:
            sum += sum_metadata(child)

        for metadata in node.metadata:
            sum += metadata

        return sum
    total_sum = sum_metadata(root)

    print("The sum of all metadata is: {0!s}".format(total_sum))

