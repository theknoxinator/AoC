# Determine the bottom disc in a list where the discs above each is listed out


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["pbga (66)",
            "xhth (57)",
            "ebii (61)",
            "havc (66)",
            "ktlj (57)",
            "fwft (72) -> ktlj, cntj, xhth",
            "qoyq (66)",
            "padx (45) -> pbga, havc, qoyq",
            "tknk (41) -> ugml, padx, fwft",
            "jptl (61)",
            "ugml (68) -> gyxo, ebii, jptl",
            "gyxo (61)",
            "cntj (57)"]


if __name__ == "__main__":
    print("Starting Day 7-1")
    values = read_file("input.txt")
    # values = test_data()

    class Node:
        def __init__(self, name):
            self.name = name
            self.children = []
            self.parent = None

    # Parse each line into a map of nodes with their references
    nodes = {}
    children = {}
    for val in values:
        # Split line by the arrow if it exists
        parts = val.split('->')
        node_name = parts[0].split()[0]
        nodes[node_name] = Node(node_name)
        if len(parts) > 1:
            # This node has children
            children[node_name] = parts[1].replace(' ', '').split(',')
        else:
            children[node_name] = []

    # Debug print out nodes
    for name in nodes.keys():
        print("Node: {0}, Children: {1}".format(name, children[name]))

    # Next we need to create the actual tree structure
    for name, node in nodes.items():
        for child_name in children[name]:
            child = nodes[child_name]
            child.parent = node
            node.children.append(child)

    # Now find the root
    root = nodes[list(nodes)[0]]
    while root.parent:
        root = root.parent

    print("The root of the tree is: {0}".format(root.name))
