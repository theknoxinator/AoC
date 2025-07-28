# Part 1: Given a set of programs and a set of dancing instructions, determine the order of the programs after the dance
# Part 2: Same as part 1 but execute the instructions 1 billion times

def perform_dance(values, loops=1):
    dancers = values[0]
    instructions = values[1].split(',')

    # In order to make all operations as efficient as possible, instead of an array we will store dance and position in
    # two dictionaries that point in each direction
    pos_map = dict()
    dnc_map = dict()
    for i, dnc in enumerate(list(dancers)):
        pos_map[i] = dnc
        dnc_map[dnc] = i

    # Now iterate through each dance instruction
    result = dancers
    for i in range(loops):
        for instr in instructions:
            if instr[0] == 's':
                # For the spin move, we add the amount to the position of each dancer, and mod by number of dancers to get
                # their new positions. We then update both maps based on this.
                spin = int(instr[1:])
                for dnc in dnc_map.keys():
                    new_pos = (dnc_map[dnc] + spin) % len(dancers)
                    dnc_map[dnc] = new_pos
                    pos_map[new_pos] = dnc
            elif instr[0] == 'x':
                # For the exchange move, we swap the dancers at the given positions, then update the dancer map as well
                left_pos, right_pos = (int(x) for x in instr[1:].split('/'))
                left_dnc = pos_map[left_pos]
                right_dnc = pos_map[right_pos]
                pos_map[left_pos] = right_dnc
                pos_map[right_pos] = left_dnc
                dnc_map[left_dnc] = right_pos
                dnc_map[right_dnc] = left_pos
            elif instr[0] == 'p':
                # For the partner move, it's the same as the exchange move but we update dancer map first
                left_dnc, right_dnc = instr[1:].split('/')
                left_pos = dnc_map[left_dnc]
                right_pos = dnc_map[right_dnc]
                dnc_map[left_dnc] = right_pos
                dnc_map[right_dnc] = left_pos
                pos_map[left_pos] = right_dnc
                pos_map[right_pos] = left_dnc

        # After all dances are done, push them out in order using pos map
        result = ''.join([pos_map[i] for i in range(len(dancers))])

    return result


def part1(values):
    return perform_dance(values)


def part2(values):
    # The problem asks for 1 billion loops, but running the loop determined that it cycles through the same positions
    # every 60 loops, so we only run it 1 billion % 60 = 40 times
    return perform_dance(values, 40)
