# Determine the order in which tasks must be completed, and output the order in which to do them

class Node:
    def __init__(self, step):
        self.step = step
        self.parents = []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)


def make_tree(values):
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

    return steps


def check_node(node, step_order):
    if len(node.parents) == 0:
        return True
    else:
        for parent in node.parents:
            if parent.step not in step_order:
                return False
        return True


def find_order(values):
    # First, read the values and determine which steps each step depends on
    steps = make_tree(values)

    # Determine the starting point
    starting_node = None
    for node in steps.values():
        if len(node.parents) == 0:
            starting_node = node

    # Now navigate the graph of nodes and put them into order as a string
    step_order = ""

    ordered_steps = sorted(steps.keys())
    while len(ordered_steps) > 0:
        for step in ordered_steps:
            if check_node(steps[step], step_order):
                step_order += step
                ordered_steps.remove(step)
                break

    return step_order


def find_time(values):
    # First, read the values and determine which steps each step depends on
    steps = make_tree(values)

    # Set up trackers for the task for each worker, and how long each task has left to complete
    num_workers = 5
    if len(values) < 10:
        num_workers = 2
    workers = [' '] * num_workers
    time_left = [0] * num_workers
    finished_tasks = []

    ordered_steps = sorted(steps.keys())
    total_time = 0
    while len(finished_tasks) < len(steps.keys()):
        # First part of loop, see if any tasks can be taken on by a worker
        steps_to_remove = []
        for step in ordered_steps:
            if check_node(steps[step], finished_tasks):
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
        for worker in range(len(workers)):
            if workers[worker] == ' ':
                continue
            time_left[worker] -= 1
            if time_left[worker] <= 0:
                finished_tasks.append(workers[worker])
                workers[worker] = ' '

        total_time += 1

    return total_time


def part1(values):
    return find_order(values)


def part2(values):
    return find_time(values)
