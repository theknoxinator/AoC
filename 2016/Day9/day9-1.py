# Based on a simple decompression algorithm in a file, determine the decompressed string

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["ADVENT",
            "A(1x5)BC",
            "(3x3)XYZ",
            "A(2x2)BCD(2x2)EFG",
            "(6x1)(1x3)A",
            "X(8x2)(3x3)ABCY"]


if __name__ == '__main__':
    print("Starting Day 9-1")
    values = read_file('input.txt')
    # values = test_data()

    # Do iteration here just to make checking the test data easier
    for val in values:
        compressed = val

        # Iterate through the compressed string, looking for the instructions in parentheses
        index = 0
        decompressed = ""
        while index < len(compressed):
            char = compressed[index]
            if char != '(':
                # We haven't encountered a parenthesis yet, so just copy this over and increment
                decompressed += char
                index += 1
                continue
            else:
                # We have encountered a parenthesis, so find out the instruction, act on it, and place the
                # index at the end of the sequence
                start_index = index + 1
                while compressed[index] != ')':
                    index += 1
                end_index = index   # End index is the index of the closing paren
                index += 1  # Set index to the start of the sequence

                instruction = compressed[start_index:end_index]
                length,repeat = list(map(int, instruction.split('x')))
                substring = compressed[index:index + length]
                for loop in range(repeat):
                    decompressed += substring

                index = index + length  # Set index to the next character after the sequence

        # Print out the result of each string
        print("The string {0} becomes {1}, which is {2!s} characters long".format(compressed, decompressed, len(decompressed)))
