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
    print("Starting Day 12-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Get all the data from the file and parse it appropriately
    start_state = []
    transitions = {}
    for val in values:
        if "initial" in val:
            items = val.split()
            start_state = ['.'] * 20 + list(items[2]) + ['.'] * 30
        else:
            items = val.split()
            transitions[items[0]] = items[2]

    # Debug print out input data
    print("[{0}]".format(','.join(start_state)))
    for key,value in transitions.items():
        print("[{0}] -> {1}".format(key, value))
    print()

    # Iterate through each spot, check its surroundings, and determine what the next state looks like
    current_state = start_state
    print("[0]: {0}".format(''.join(current_state)))
    for gen in range(20):
        # Create a new state and figure out where plants are
        new_state = ['.'] * len(current_state)
        for index in range(2, len(current_state) - 2):
            plant_check = str(''.join(current_state[index-2:index+3]))
            if plant_check in transitions:
                new_state[index] = transitions[plant_check]

        # Set new state to current and go again
        current_state = new_state
        print("[{0!s}]: {1}".format(gen + 1, ''.join(current_state)))

    # Print out answer
    plant_sum = 0
    for index in range(len(current_state)):
        if current_state[index] == '#':
            plant_sum += (index - 20)
    print("Total sum is: {0!s}".format(plant_sum))
