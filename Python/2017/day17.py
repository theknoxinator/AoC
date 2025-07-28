# Part 1: Insert a sequence of values into a circular array after stepping X number of times each insert, return node after end
# Part 2: Doing the same inserts, find the value of the second node after a very large number of inserts (50 million)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def create_list(max_value, steps):
    root = Node(0)
    current = root
    current.next = current
    for i in range(1, max_value + 1):
        for _ in range(steps):
            current = current.next
        current.next = Node(i, current.next)
        current = current.next
    return root, current # Return the last node that was created plus the root


def find_next_value(values, max_value=2017):
    steps = int(values[0])
    # For this first implementation, we do want to create the actual list since it's practical and fast to do
    root_node, last_node = create_list(max_value, steps)
    return last_node.next.data, root_node.next.data


def find_second_value(values, max_value=2017):
    steps = int(values[0])
    # For the second implementation, 50 million inserts will take a very long time and a lot of memory, and since we
    # only care about the second value in the last anyway, we can just track and only insert when the position returns
    # to the first node
    root_node = Node(0)
    current = 0
    for i in range(1, max_value + 1):
        # Move the position forward and modulo by the current size to get the current position
        current = (current + steps) % i
        # Only add if the current is back to the root
        if current == 0:
            root_node.next = Node(i, root_node.next)
        current += 1
    return root_node.next.data


def part1(values):
    return find_next_value(values)[0]


def part2(values):
    return find_second_value(values, 50_000_000)
