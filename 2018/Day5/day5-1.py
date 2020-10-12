# Remove all matching units from a long string of characters. Matching units are considered to be a
# lower-case and upper-case of the same character.

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    return "dabAcCaCBAcCcaDA"

if __name__ == '__main__':
    print("Starting Day5-1")
    # Read file into value
    value = read_file('input.txt')
    #value = test_data()

    has_changed = True
    while has_changed:
        print(value)
        has_changed = False
        index = 0
        while index < len(value) - 1:
            char = ord(value[index])
            if char >= 65 and char <= 90:
                # Uppercase
                if ord(value[index+1]) == char + 32:
                    value = value[:index] + value[index+2:]
                    has_changed = True
                else:
                    index += 1
            elif char >= 97 and char <= 122:
                # Lowercase
                if ord(value[index+1]) == char - 32:
                    value = value[:index] + value[index+2:]
                    has_changed = True
                else:
                    index += 1
            else:
                index += 1

    # Print out answer
    print("The length of final polymer is: {0}".format(str(len(value))))
