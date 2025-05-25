# Calculate the difference between code memory and in-app memory. Code memory refers to the number
# of characters in the string literal, in-app memory refers to the string representation in the app.

def part1(values):
    # Iterate and calculate the different memories for each string literal, and add them all up
    literal_total = 0
    string_total = 0
    for val in values:
        # print("Length of literal for {0} is {1}".format(val, str(len(val))))
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

        # print("Length of string for {0} is {1}".format(val, str(count)))
        string_total += count

    return literal_total - string_total


def part2(values):
    # Iterate and calculate the different memories for each string literal, and add them all up
    literal_total = 0
    string_total = 0
    for val in values:
        # print("Length of literal for {0} is {1}".format(val, str(len(val))))
        literal_total += len(val)

        count = 2  # default because entire literal is now quoted
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

        # print("Length of encoded string for {0} is {1}".format(val, str(count)))
        string_total += count

    return abs(literal_total - string_total)
