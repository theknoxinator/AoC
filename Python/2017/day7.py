# Determine the bottom disc in a list where the discs above each is listed out

class Node:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None
        self.total_weight = 0


def create_tree(values):
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

    return root


def find_bottom(values):
    root = create_tree(values)
    return root.name


def find_weight(values):
    root = create_tree(values)

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

    # Now go through the tree and figure out which is the bad node
    runner = root
    diff = 0
    while runner:
        outlier = None
        for child in runner.children:
            has_match = False
            for other in runner.children:
                if child == other:
                    continue
                diff = max(diff, abs(child.total_weight - other.total_weight))
                if child.total_weight == other.total_weight:
                    has_match = True
                    break
            if not has_match:
                outlier = child
        if outlier:
            runner = outlier
        else:
            break

    return runner.weight - diff


def part1(values):
    return find_bottom(values)


def part2(values):
    return find_weight(values)
