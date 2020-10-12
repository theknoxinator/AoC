# Add sums of repeating digits based on inputs from file
# Digits are only added to the total sum if the following digit is the same
# Digits only count if they repeat halfway through the list

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    #return "1212"
    #return "1221"
    #return "123425"
    #return "123123"
    return "12131415"

if __name__ == '__main__':
    print("Starting Day1-2")
    # Read file into string of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and add repeated digits to sum
    sum = 0
    half_length = int(len(values) / 2)
    for index in range(half_length):
        if values[index] == values[index + half_length]:
            sum += int(values[index])
    sum *= 2

    # Print out answer
    print("The final sum is : {0}".format(str(sum)))
