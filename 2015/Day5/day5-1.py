# Determine which strings are good or bad based on specific criteria

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]

if __name__ == '__main__':
    print("Starting Day5-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and check each string for criteria
    good_strings = 0
    for val in values:
        # First, check to see if disallowed parts are in it
        has_disallowed = False
        for check in ['ab', 'cd', 'pq', 'xy']:
            if check in val:
                has_disallowed = True
                break
        if has_disallowed:
            print("String {0} has disallowed part".format(val))
            continue

        # Second, iterate through and check for vowels
        vowels = 0
        for i in range(len(val)):
            if val[i] in 'aeiou':
                vowels += 1

        # Third, iterate through and check for doubled letters
        has_double = False
        for i in range(len(val)-1):
            if val[i] == val[i+1]:
                has_double = True
                break

        print("String {0} has {1} vowels and has double: {2}".format(val, str(vowels), str(has_double)))
        if vowels >= 3 and has_double:
            good_strings += 1

    # Print out answer
    print("The number of good strings is: {0}".format(str(good_strings)))
