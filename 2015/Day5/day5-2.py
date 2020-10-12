# Determine which strings are good or bad based on specific criteria

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy", "abcdaba", "aaaa"]

if __name__ == '__main__':
    print("Starting Day5-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and check each string for criteria
    good_strings = 0
    double_pairs = []
    doubles = []
    for val in values:
        # First, iterate through and check for doubled pairs of letters
        has_double_pair = False
        pairs = {}
        for i in range(len(val)-1):
            pair = val[i:i+2]
            if pair in pairs:
                if i - pairs[pair] > 1:
                    has_double_pair = True
                    double_pairs.append(val)
                    break
            else:
                pairs[pair] = i

        # Second, iterate through and check for doubled letters with one letter in between
        has_double = False
        for i in range(len(val)-2):
            if val[i] == val[i+2]:
                doubles.append(val)
                has_double = True
                break

        print("String {0} has doubled pair: {1} and has double: {2}".format(val, str(has_double_pair), str(has_double)))
        if has_double_pair and has_double:
            good_strings += 1

    # Print out answer
    print("The number of good strings is: {0}".format(str(good_strings)))
