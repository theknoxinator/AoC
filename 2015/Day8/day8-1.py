# Calculate the difference between code memory and in-app memory. Code memory refers to the number
# of characters in the string literal, in-app memory refers to the string representation in the app.

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']

if __name__ == '__main__':
    print("Starting Day8-1")
    # Read file into list of vlaues
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and calculate the different memories for each string literal, and add them all up
    literal_total= 0
    string_total = 0
    for val in values:
        print("Length of literal for {0} is {1}".format(val, str(len(val))))
        literal_total += len(val)

        count = 0
        index = 0
        while index < len(val):
            char = val[index]
            if char == '"':
                pass
            elif char == '\\':
                if val[index + 1] == '\\' or val[index + 1] == '"':
                    count += 1
                    index += 1
                elif val[index + 1] == 'x':
                    count += 1
                    index += 3
            else:
                count += 1
            index += 1

        print("Length of string for {0} is {1}".format(val, str(count)))
        string_total += count

    # Print out answer
    print("Total length of literals is {0}".format(str(literal_total)))
    print("Total length of strings is {0}".format(str(string_total)))
    print("Difference is {0}".format(str(literal_total - string_total)))
