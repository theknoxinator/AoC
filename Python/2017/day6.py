# Determine how long it takes for us to find a duplicate pattern in the memory banks

def find_pattern(values):
    banks = list(map(int, values[0].split()))

    def to_pattern(banks):
        return ','.join(map(str, banks))

    # Keep track of the patterns
    seen = {}
    pattern = to_pattern(banks)
    cycles = 0
    seen[pattern] = cycles

    while True:
        # Choose which bank to empty
        highest = 0
        for i in range(len(banks)):
            if banks[i] > banks[highest]:
                highest = i

        # Now get the number of blocks in the bank
        to_shift = banks[highest]
        banks[highest] = 0

        # Now distribute the blocks
        index = highest + 1
        for _ in range(to_shift):
            if index >= len(banks):
                index = 0
            banks[index] += 1
            index += 1
        cycles += 1

        # Check the pattern against the seen bucket
        pattern = to_pattern(banks)
        if pattern in seen:
            break
        else:
            seen[pattern] = cycles

    return cycles, cycles - seen[pattern]


def part1(values):
    return find_pattern(values)[0]


def part2(values):
    return find_pattern(values)[1]
