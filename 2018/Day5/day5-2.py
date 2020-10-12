# Remove all matching units from a long string of characters. Matching units are considered to be a
# lower-case and upper-case of the same character.
# Second part: Remove all of a single character before doing the matching unit removal.
import sys

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    return "dabAcCaCBAcCcaDA"

if __name__ == '__main__':
    print("Starting Day5-2")
    # Read file into value
    value = read_file('input.txt')
    #value = test_data()

    shortest_length = sys.maxsize
    for remove_char in range(ord('A'), ord('Z')+1):
        polymer = value.replace(chr(remove_char),'').replace(chr(remove_char+32),'')

        has_changed = True
        while has_changed:
            has_changed = False
            index = 0
            while index < len(polymer) - 1:
                char = ord(polymer[index])
                if char >= 65 and char <= 90:
                    # Uppercase
                    if ord(polymer[index+1]) == char + 32:
                        polymer = polymer[:index] + polymer[index+2:]
                        if index > 0:
                            index -= 1
                        has_changed = True
                    else:
                        index += 1
                elif char >= 97 and char <= 122:
                    # Lowercase
                    if ord(polymer[index+1]) == char - 32:
                        polymer = polymer[:index] + polymer[index+2:]
                        if index > 0:
                            index -= 1
                        has_changed = True
                    else:
                        index += 1
                else:
                    index += 1

        print(polymer)
        print("The length for polymer after removing {0},{1} is: {2}".format(chr(remove_char), chr(remove_char+32), str(len(polymer))))

        if len(polymer) < shortest_length:
            shortest_length = len(polymer)

    # Print out answer
    print("The length of final polymer is: {0}".format(str(shortest_length)))
