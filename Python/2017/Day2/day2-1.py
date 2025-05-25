# Calculate the checksum of inputs from file
# Checksum is calculated by taking biggest difference between numbers in each line and summing the differences
import sys

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["5 1 9 5", "7 5 3", "2 4 6 8"]

if __name__ == '__main__':
    print("Starting Day2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and calculate largest difference in each line
    checksum = 0
    for val in values:
        min = sys.maxsize
        max = 0
        for num in list(map(int, val.split())):
            if num < min:
                min = num
            if num > max:
                max = num

        checksum += max - min

    # Print out answer
    print("The checksum is: {0}".format(str(checksum)))