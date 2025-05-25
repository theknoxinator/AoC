# Calculate the difference between code memory and encoded memory. Code memory refers to the number
# of characters in the string literal, encoded memory refers to the number of characters after each
# character is encoded

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']

if __name__ == '__main__':
    print("Starting Day8-2")
    # Read file into list of vlaues
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and calculate the different memories for each string literal, and add them all up
    literal_total = 0
    string_total = 0
    for val in values:
        print("Length of literal for {0} is {1}".format(val, str(len(val))))
        literal_total += len(val)

        count = 2 # default because entire literal is now quoted
        index = 0
        while index < len(val):
            char = val[index]
            if char == '"':
                count += 2
            elif char == '\\':
                count += 2
            else:
                count += 1
            index += 1

        print("Length of encoded string for {0} is {1}".format(val, str(count)))
        string_total += count

    # Print out answer
    print("Total length of literals is {0}".format(str(literal_total)))
    print("Total length of encoded strings is {0}".format(str(string_total)))
    print("Difference is {0}".format(str(literal_total - string_total)))
