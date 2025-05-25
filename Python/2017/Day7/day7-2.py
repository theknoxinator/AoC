# Determine the program with the wrong weight, and what that weight should be


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
    print("Starting Day 7-2")
    values = read_file("input.txt")
    # values = test_data()


    class Node:
        def __init__(self, name, weight):
            self.name = name
            self.weight = weight
            self.children = []
            self.parent = None
            self.total_weight = 0


    # Parse each line into a map of nodes with their references
    nodes = {}
    children = {}
    for val in values:
        # Split line by the arrow if it exists
        parts = val.split('->')
        node_name, weight = parts[0].replace('(', '').replace(')', '').split()
        nodes[node_name] = Node(node_name, int(weight))
        if len(parts) > 1:
            # This node has children
            children[node_name] = parts[1].replace(' ', '').split(',')
        else:
            children[node_name] = []

    # Debug print out nodes
    for name, node in nodes.items():
        print("Node: {0} ({1!s}), Children: {2}".format(name, node.weight, children[name]))

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

    # With the root we can determine the weights of each child all the way down
    def get_total_weight(sub_root):
        total_weight = 0
        for child in sub_root.children:
            if child.total_weight == 0:
                get_total_weight(child)
            total_weight += child.total_weight
        total_weight += sub_root.weight
        sub_root.total_weight = total_weight

    get_total_weight(root)

    # Debug print out nodes with total weights
    for name, node in nodes.items():
        print("Node: {0}, Total weight: {1!s}".format(name, node.total_weight))

    # Now go through the tree and figure out which is the bad node
    runner = root
    while runner:
        print("For node: {0}, the children are:".format(runner.name))
        outlier = None
        for child in runner.children:
            print("   {0} with a total weight of {1!s}".format(child.name, child.total_weight))
            has_match = False
            for other in runner.children:
                if child == other:
                    continue
                if child.total_weight == other.total_weight:
                    has_match = True
                    break
            if not has_match:
                print("   {0} is an outlier, so go in there".format(child.name))
                outlier = child
        if outlier:
            runner = outlier
        else:
            print("{0} is the node with the wrong value".format(runner.name))
            break

    print("Node: {0} has the wrong value of {1!s}".format(runner.name, runner.weight))
