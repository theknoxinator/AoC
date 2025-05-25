# Based on a simple decompression algorithm in a file, determine the decompressed string

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["(3x3)XYZ",
            "X(8x2)(3x3)ABCY",
            "(27x12)(20x12)(13x14)(7x10)(1x12)A",
            "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]


if __name__ == '__main__':
    print("Starting Day 9-2")
    values = read_file('input.txt')
    # values = test_data()

    # Recursive function for determining the length of a sequence as it expands out
    def get_length(sequence):
        # We basically need to do the same thing here as in the outer loop
        index = 0
        sequence_length = 0
        while index < len(sequence):
            char = sequence[index]
            if char != '(':
                sequence_length += 1
                index += 1
                continue
            else:
                start_index = index + 1
                while sequence[index] != ')':
                    index += 1
                end_index = index
                index += 1

                instruction = sequence[start_index:end_index]
                length,repeat = list(map(int, instruction.split('x')))
                substring = sequence[index:index + length]
                sequence_length += get_length(substring) * repeat

                index = index + length
        return sequence_length

    # Do iteration here just to make checking the test data easier
    for val in values:
        compressed = val

        # The biggest difference here is that we need to decompress until there are no more parentheses
        # but that will take too long for the real input, so we really just need to figure out the length
        # based on the nested instructions

        # Iterate through the compressed string, looking for the instructions in parentheses
        index = 0
        full_length = 0
        while index < len(compressed):
            char = compressed[index]
            if char != '(':
                # We haven't encountered a parenthesis yet, so just copy this over and increment
                full_length += 1
                index += 1
                continue
            else:
                # We have encountered a parenthesis, so find out the instruction, determine how many
                # characters it expands out to, and add it to the total length
                start_index = index + 1
                while compressed[index] != ')':
                    index += 1
                end_index = index   # End index is the index of the closing paren
                index += 1  # Set index to the start of the sequence

                instruction = compressed[start_index:end_index]
                length,repeat = list(map(int, instruction.split('x')))
                substring = compressed[index:index + length]
                sequence_length = get_length(substring)
                full_length += sequence_length * repeat

                index = index + length  # Set index to the next character after the sequence

        # Print out the result of each string
        print("The string {0} decompressed to a length of {1!s}".format(compressed, full_length))
