# Determine the result of multiplying the first two values of a circular list that has had a bunch of operations performed
# on it based on an input of lengths

def list_numbers(values):
    lengths = list(map(int, values[0].split(',')))
    size = int(values[1])

    # Start by creating the array we are changing
    numbers = []
    for i in range(size):
        numbers.append(i)

    # Now perform the operations based on the input
    index = 0
    skip = 0
    for length in lengths:
        lower = index
        upper = index + length - 1

        # Do the reversal
        while upper > lower:
            swap = numbers[lower % size]
            numbers[lower % size] = numbers[upper % size]
            numbers[upper % size] = swap
            lower += 1
            upper -= 1

        # Now move the index up by the length + skip
        index = (index + length + skip) % size

        # Last, increment the skip
        skip += 1

    return numbers[0] * numbers[1]


def gen_hash(values):
    size = int(values[1])

    numbers = []
    for i in range(size):
        numbers.append(i)

    # Next, we need to convert the input string into the sequence of lengths to switch
    lengths = []
    for i in list(values[0]):
        lengths.append(ord(i))
    lengths += [17, 31, 73, 47, 23]

    # Now perform the operations based on the input
    index = 0
    skip = 0
    for i in range(64):
        for length in lengths:
            lower = index
            upper = index + length - 1

            # Do the reversal
            while upper > lower:
                swap = numbers[lower % size]
                numbers[lower % size] = numbers[upper % size]
                numbers[upper % size] = swap
                lower += 1
                upper -= 1

            # Now move the index up by the length + skip
            index = (index + length + skip) % size

            # Last, increment the skip
            skip += 1

    # Next, perform an XOR on each block of 16 numbers to reduce to 16 values
    reduced_values = []
    for i in range(16):
        start = 16 * i
        end = start + 16
        subvalues = numbers[start:end]
        xor_value = subvalues[0]
        for subvalue in subvalues[1:]:
            xor_value = xor_value ^ subvalue
        reduced_values.append(xor_value)

    # Finally, convert the reduced values to a hex string
    hex_string = ''.join(['{0:02x}'.format(x) for x in reduced_values])

    return hex_string


def part1(values):
    return list_numbers(values)


def part2(values):
    return gen_hash(values)
