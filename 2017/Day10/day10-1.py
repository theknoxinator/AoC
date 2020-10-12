# Determine the result of multiplying the first two values of a circular list that has had a bunch of operations performed
# on it based on an input of lengths


# input = [3, 4, 1, 5]
input = [14, 58, 0, 116, 179, 16, 1, 104, 2, 254, 167, 86, 255, 55, 122, 244]

# SIZE = 5
SIZE = 256


if __name__ == "__main__":
    print("Starting Day 10-1")

    # Start by creating the array we are changing
    values = []
    for i in range(SIZE):
        values.append(i)

    # Now perform the operations based on the input
    index = 0
    skip = 0
    for length in input:
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

    print("The list at the end looks like this: {0}".format(','.join(map(str, values))))
    print("The multiple of {0!s} and {1!s} is {2!s}".format(values[0], values[1], values[0] * values[1]))
