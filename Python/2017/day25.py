# Part 1: Given a set of Turing machine instructions, find the diagnostic checksum after executing steps
# Part 2: FREE!

def run_machine(values):
    # Read values in (I have modified the files to be easier to parse from the original)
    current_state = values[0]
    checksum_steps = int(values[1])
    state_action_map = dict()
    for i in range(2, len(values)):
        left, right = values[i].split(' : ')
        state = (left.split(',')[0], int(left.split(',')[1]))
        action = {
            'set': int(right.split(',')[0]),
            'move': right.split(',')[1],
            'new_state': right.split(',')[2],
        }
        state_action_map[state] = action

    # Start with a blank tape (assumed that no value in the map is 0)
    tape = {0: 0}
    cursor = 0

    # Now execute the steps enough times to get the diagnostic checksum
    for _ in range(checksum_steps):
        current_value = tape[cursor] if cursor in tape else 0
        action_to_do = state_action_map[(current_state, current_value)]

        # Set the new value
        tape[cursor] = action_to_do['set']

        # Move the cursor
        cursor = cursor + 1 if action_to_do['move'] == 'R' else cursor - 1

        # Update the state
        current_state = action_to_do['new_state']

    # To get the checksum, just count the number of ones on the tapes
    return sum(tape.values())


def part1(values):
    return run_machine(values)
