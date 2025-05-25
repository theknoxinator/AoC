# Determine how long it takes for us to find a duplicate pattern in the memory banks


# input = [0, 2, 7, 0]
input = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]


if __name__ == "__main__":
    print("Starting Day 6-2")

    def to_pattern(banks):
        return ','.join(map(str, banks))

    # Keep track of the patterns
    seen = {}
    pattern = to_pattern(input)
    print(pattern)
    cycles = 0
    seen[pattern] = cycles

    while True:
        # Choose which bank to empty
        highest = 0
        for i in range(len(input)):
            if input[i] > input[highest]:
                highest = i

        # Now get the number of blocks in the bank
        to_shift = input[highest]
        input[highest] = 0

        # Now distribute the blocks
        index = highest + 1
        for _ in range(to_shift):
            if index >= len(input):
                index = 0
            input[index] += 1
            index += 1
        cycles += 1

        # Check the pattern against the seen bucket
        pattern = to_pattern(input)
        print(pattern)
        if pattern in seen:
            cycles = cycles - seen[pattern]
            break
        else:
            seen[pattern] = cycles

    print("The number of cycles was: {0!s}".format(cycles))
