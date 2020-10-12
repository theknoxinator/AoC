# Add sums of repeating digits based on inputs from file
# Digits are only added to the total sum if the following digit is the same

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    #return "1122"
    #return "1111"
    #return "1234"
    return "91212129"

if __name__ == '__main__':
    print("Starting Day1")
    # Read file into string of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and add repeated digits to sum
    sum = 0
    for index in range(len(values)):
        if index == len(values) - 1:
            # Last digit, check first digit
            if values[index] == values[0]:
                sum += int(values[index])
        elif values[index] == values[index+1]:
            sum += int(values[index])

    # Print out answer
    print("The final sum is : {0}".format(str(sum)))
