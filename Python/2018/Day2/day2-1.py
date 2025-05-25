# Create checksum using IDs from a file
# Checksum is created by multiplying the number of IDs with at least one letter that occurs twice
# with the number of IDs with at least one letter that occurs thrice

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

if __name__ == '__main__':
    print("Starting Day 2-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and check to see if value has letters that repeat twice or thrice
    twice = 0
    thrice = 0
    for val in values:
        # Initialize array
        counts = [0] * 26

        # Count each letter in ID
        for letter in val:
            index = ord(letter) - 97
            counts[index] += 1

        # Check to see if there are repeats
        has_twice = False
        has_thrice = False
        for count in counts:
            if count == 2:
                has_twice = True
            elif count == 3:
                has_thrice = True

        if has_twice:
            twice += 1
        if has_thrice:
            thrice += 1

        print("For ID: {0}, counts: {1}".format(val, ','.join(map(str, counts))))
        print("For ID: {0}, has twice: {1}, has thrice: {2}".format(val, str(has_twice), str(has_thrice)))

    # Calculate the checksum
    checksum = twice * thrice

    # Print out answer
    print("The final checksum is: {0}".format(str(checksum)))