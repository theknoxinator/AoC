# Determine how long it takes to complete all steps, assuming that there are 5 workers who can work in
# parallel, and each step must wait for an available worker and/or parent steps to be done first

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
    print("Starting Day7-2")
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
        print("Node {0} has children: [{1}]".format(step, ','.join(child.step for child in node.children)))

    # This time instead of putting down a fixed order, we can do things in parallel, so the instant a task
    # has its dependencies finished and there is an available worker, we need to start it

    # Set up trackers for the task for each worker, and how long each task has left to complete
    num_workers = 5
    workers = [' ']*num_workers
    time_left = [0]*num_workers
    finished_tasks = []

    def check_node(node):
        if len(node.parents) == 0:
            return True
        else:
            for parent in node.parents:
                if parent.step not in finished_tasks:
                    return False
            return True

    ordered_steps = sorted(steps.keys())
    total_time = 0
    while len(finished_tasks) < len(steps.keys()):
        # First part of loop, see if any tasks can be taken on by a worker
        steps_to_remove = []
        for step in ordered_steps:
            if check_node(steps[step]):
                for worker in range(len(workers)):
                    if workers[worker] == ' ' and time_left[worker] <= 0:
                        workers[worker] = step
                        time_left[worker] = ord(step) - 4
                        steps_to_remove.append(step)
                        break
        for step in steps_to_remove:
            ordered_steps.remove(step)

        # Second part of loop, decrement time left as we tick up total time, and see if any tasks are
        # finished
        print("{0!s:>4}  {1}  {2}".format(total_time, '  '.join(workers), ''.join(finished_tasks)))
        for worker in range(len(workers)):
            if workers[worker] == ' ':
                continue
            time_left[worker] -= 1
            if time_left[worker] <= 0:
                finished_tasks.append(workers[worker])
                workers[worker] = ' '

        total_time += 1

    print("{0!s:>4}  {1}  {2}".format(total_time, '  '.join(workers), ''.join(finished_tasks)))

    # Print out answer
    print("The total time taken is: {0}".format(total_time))
