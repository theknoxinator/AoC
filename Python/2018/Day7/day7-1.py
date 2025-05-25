# Determine the order in which tasks must be completed, and output the order in which to do them

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["Step C must be finished before step A can begin.",
            "Step C must be finished before step F can begin.",
            "Step A must be finished before step B can begin.",
            "Step A must be finished before step D can begin.",
            "Step B must be finished before step E can begin.",
            "Step D must be finished before step E can begin.",
            "Step F must be finished before step E can begin."]

if __name__ == '__main__':
    print("Starting Day7-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    class Node:
        def __init__(self, step):
            self.step = step
            self.parents = []
            self.children = []

        def add_child(self, child):
            self.children.append(child)

        def add_parent(self, parent):
            self.parents.append(parent)

    # First, read the values and determine which steps each step depends on
    # Store these relationships as double-linked referenced nodes, put in a dict for each lookup
    steps = {}
    for val in values:
        items = val.split()
        parent_step = items[1]
        child_step = items[7]

        if parent_step not in steps:
            steps[parent_step] = Node(parent_step)
        parent_node = steps[parent_step]

        if child_step not in steps:
            steps[child_step] = Node(child_step)
        child_node = steps[child_step]

        parent_node.add_child(child_node)
        child_node.add_parent(parent_node)


    # Debug print out all nodes and their children
    for step,node in steps.items():
        print("Node {0} has parents: [{1}]".format(step, ','.join(parent.step for parent in node.parents)))

    # Determine the starting point
    starting_node = None
    for node in steps.values():
        if len(node.parents) == 0:
            starting_node = node
    print("The starting node is: {0}".format(starting_node.step))

    # Now navigate the graph of nodes and put them into order as a string
    step_order = ""

    def check_node(node):
        if len(node.parents) == 0:
            return True
        else:
            for parent in node.parents:
                if parent.step not in step_order:
                    return False
            return True

    ordered_steps = sorted(steps.keys())
    while len(ordered_steps) > 0:
        for step in ordered_steps:
            if check_node(steps[step]):
                step_order += step
                ordered_steps.remove(step)
                break

    # Print out answer
    print("The order is: {0}".format(step_order))
