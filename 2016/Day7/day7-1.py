# Determine the number of IPv7 addresses that have an ABBA annotation in them

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["abba[mnop]qrst",
            "abcd[bddb]xyyx",
            "aaaa[qwer]tyui",
            "ioxxoj[asdfgh]zxcvbn"]


if __name__ == '__main__':
    print("Starting Day 7-1")
    values = read_file('input.txt')
    # values = test_data()

    # For this problem, we just need to read each input, iterate over each four characters and determine
    # if there is an ABBA annotation (two different letters followed by its reverse), unless it is within
    # a set of square brackets
    total_ips = 0
    for val in values:
        # Iterate over the string up to the fourth to last position
        in_square = False
        has_abba = False
        for index in range(len(val) - 3):
            # Get the first two characters
            first = val[index]
            second = val[index + 1]

            # First, check to see if the first character is a square bracket since we can ignore them
            if first == '[':
                in_square = True
                continue
            elif first == ']':
                in_square = False
                continue

            # Second, check to make sure the two characters are different
            if first == second:
                continue

            # Now, check for a repeat of its reverse
            if first == val[index + 3] and second == val[index + 2]:
                has_abba = True
                # We have a match, but if it's inside square brackets, it invalidates the whole thing
                if in_square:
                    break

        # If we have an abba match, but it's in a square, we don't count it, otherwise we do
        if has_abba and not in_square:
            total_ips += 1

    # Print out answer
    print("The number of TLS IPs is: {0!s}".format(total_ips))