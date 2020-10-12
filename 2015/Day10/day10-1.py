# Create an algorithm for generating look-and-say sequences of digits
# For each set of consecutive digits in an existing sequence, the new sequence will have the number
# in the set followed by the digit

input = '1321131112'
test_data = '1'

if __name__ == '__main__':
    print("Starting Day10-1")

    current = input
    for _ in range(50):
        new_sequence = ""

        digit = current[0]
        index = 1
        count = 1
        while index < len(current):
            if digit != current[index]:
                new_sequence += str(count) + digit
                count = 1
                digit = current[index]
            else:
                count += 1
            index += 1
        new_sequence += str(count) + digit

        current = new_sequence

    print("Length of final string: {0}".format(str(len(current))))
