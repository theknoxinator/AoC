# Calculate the checksum of inputs from file
# Checksum is calculated by taking the only integer result of dividing each number in each line

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["5 9 2 8", "9 4 7 3", "3 8 6 5"]

if __name__ == '__main__':
    print("Starting Day2-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and find which values divide into an int
    checksum = 0
    for val in values:
        numbers = list(map(int, val.split()))

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                result = numbers[i] / numbers[j]
                if result.is_integer():
                    checksum += int(result)
                result = numbers[j] / numbers[i]
                if result.is_integer():
                    checksum += int(result)

    # Print out answer
    print("The checksum is: {0}".format(str(checksum)))