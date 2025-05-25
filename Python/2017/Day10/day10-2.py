# Determine the knot hash based on a series of twists using an input string


# input = ""
# input = "AoC 2017"
# input = "1,2,3"
# input = "1,2,4"
input = "14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244"

# SIZE = 5
SIZE = 256


if __name__ == "__main__":
    print("Starting Day 10-2")

    # Start by creating the array we are changing
    values = []
    for i in range(SIZE):
        values.append(i)

    # Next, we need to convert the input string into the sequence of lengths to switch
    lengths = []
    for i in input:
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
                swap = values[lower % SIZE]
                values[lower % SIZE] = values[upper % SIZE]
                values[upper % SIZE] = swap
                lower += 1
                upper -= 1

            # Now move the index up by the length + skip
            index = (index + length + skip) % SIZE

            # Last, increment the skip
            skip += 1

    # Next, perform an XOR on each block of 16 numbers to reduce to 16 values
    reduced_values = []
    for i in range(16):
        start = 16 * i
        end = start + 16
        subvalues = values[start:end]
        xor_value = subvalues[0]
        for subvalue in subvalues[1:]:
            xor_value = xor_value ^ subvalue
        reduced_values.append(xor_value)

    # Finally, convert the reduced values to a hex string
    hex_string = ''.join(['{0:02x}'.format(x) for x in reduced_values])

    print("The list at the end looks like this: {0}".format(','.join(map(str, values))))
    print("The hex string at the end is: {0}".format(hex_string))
