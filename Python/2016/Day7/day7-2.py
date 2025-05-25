# Determine the number of IPv7 addresses that have an ABA and BAB annotation in them

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["aba[bab]xyz",
            "xyx[xyx]xyx",
            "aaa[kek]eke",
            "zazbz[bzb]cdb"]


if __name__ == '__main__':
    print("Starting Day 7-2")
    values = read_file('input.txt')
    # values = test_data()

    # For this problem, we need to iterate over each three letters and determine if it's an ABA pattern
    # match. We keep all of these matches in a couple lists, one for inside square brackets and one for
    # outside. Then we check each pattern to see if an ABA is in one list and a BAB in the other.
    total_ips = 0
    for val in values:
        in_square = False
        outside_patterns = []
        inside_patterns = []
        # Iterate over the string up to the third to last position
        for index in range(len(val) - 2):
            # Get the three characters
            first = val[index]
            second = val[index + 1]
            third = val[index + 2]

            # First, check to see if the first or second character is a square bracket since we can ignore
            # them
            if first == '[':
                in_square = True
                continue
            elif first == ']':
                in_square = False
                continue
            elif second == '[' or second == ']':
                # We don't want to get a match like 'a[a'
                continue

            # Second, check to make sure the two characters are different
            if first == second:
                continue

            # Now, check to see if it is a pattern
            if first == val[index + 2]:
                # We have a match, so put it in the correct bucket
                if in_square:
                    inside_patterns.append(first + second + third)
                else:
                    outside_patterns.append(first + second + third)

        # Now we need to see if any patterns match
        for aba in outside_patterns:
            bab = aba[1] + aba[0] + aba[1]
            if bab in inside_patterns:
                total_ips += 1
                break

    # Print out answer
    print("The number of SSL IPs is: {0!s}".format(total_ips))