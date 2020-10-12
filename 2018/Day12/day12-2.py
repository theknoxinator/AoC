# Determine the number of pots that have plants after a number of generations where new plants appear
# based on defined rules and an initial state

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["initial state: #..#.#..##......###...###",
            "...## => #",
            "..#.. => #",
            ".#... => #",
            ".#.#. => #",
            ".#.## => #",
            ".##.. => #",
            ".#### => #",
            "#.#.# => #",
            "#.### => #",
            "##.#. => #",
            "##.## => #",
            "###.. => #",
            "###.# => #",
            "####. => #"]

if __name__ == '__main__':
    print("Starting Day 12-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Get all the data from the file and parse it appropriately
    # Unlike the first one, since we need to iterate 50 billion times, an array won't do, we will need to
    # use a linked list
    class Node:
        def __init__(self, index, value):
            self.index = index
            self.value = value
            self.new_value = None
            self.prev = None
            self.next = None

    start_state = []
    transitions = {}
    for val in values:
        if "initial" in val:
            items = val.split()
            start_state = list(items[2])
        else:
            items = val.split()
            transitions[items[0]] = items[2]

    head = None
    tail = None
    for index in range(len(start_state)):
        if index == 0:
            head = Node(index, start_state[index])
            tail = head
        else:
            current_node = Node(index, start_state[index])
            tail.next = current_node
            current_node.prev = tail
            tail = current_node

    # Debug print out input data
    def list_to_string(start_node):
        printed_string = ""
        runner = start_node
        while runner:
            printed_string += runner.value
            runner = runner.next
        return printed_string

    def print_sum(start_node):
        plant_sum = 0
        current_node = start_node
        while current_node:
            if current_node.value == '#':
                plant_sum += current_node.index
            current_node = current_node.next
        print("Total sum is: {0!s}".format(plant_sum))

    # Iterate through each spot, check its surroundings, and determine what the next state looks like
    TOTAL_GENS = 500000
    for gen in range(TOTAL_GENS):
        # Debug print out how far we are
        if gen % 1000 == 0:
            print("[{0!s}]: {1}".format(gen, list_to_string(head)))
            print_sum(head)

        # Start at the head and go backwards if necessary
        while head.value == '#' or head.next.value == '#' or head.next.next.value == '#' or head.next.next.next.value == '#':
            new_node = Node(head.index - 1, '.')
            new_node.next = head
            head.prev = new_node
            head = new_node

        # Alternately, if there is blank space ahead of the head, push it forward
        while head.value == '.' and head.next.value == '.' and head.next.next.value == '.' and head.next.next.next.value == '.' and head.next.next.next.next.value == '.':
            old_node = head
            head = old_node.next
            head.prev = None
            del old_node

        # Start at the tail and go forwards if necessary
        while tail.value == '#' or tail.prev.value == '#' or tail.prev.prev.value == '#' or tail.prev.prev.prev.value == '#':
            new_node = Node(tail.index + 1, '.')
            new_node.prev = tail
            tail.next = new_node
            tail = new_node

        # Now iterate from the head forward
        current_node = head
        while current_node:
            # Don't check nodes that have non-existent parts
            if current_node.prev is None or current_node.prev.prev is None or current_node.next is None or current_node.next.next is None:
                current_node = current_node.next
                continue

            # Get the previous two and next two, concatenate values into a string to key off of
            transition_key = current_node.prev.prev.value + current_node.prev.value + current_node.value + \
                             current_node.next.value + current_node.next.next.value

            # Set the transition to the new value of the node
            if transition_key in transitions:
                current_node.new_value = transitions[transition_key]
            else:
                current_node.new_value = '.'

            # Last, move to the next node
            current_node = current_node.next

        # Set new values to current values
        current_node = head
        while current_node:
            if current_node.new_value:
                current_node.value = current_node.new_value
                current_node.new_value = None
            current_node = current_node.next

    # Print out answer
    print("[{0!s}]: {1}".format(TOTAL_GENS, list_to_string(head)))
    print_sum(head)
