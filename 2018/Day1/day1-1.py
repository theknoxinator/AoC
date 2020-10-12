# Change frequency based on inputs from file
# Positive frequency change adds to current value, negative change subtracts

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == '+':
                values.append(int(line[1:]))
            elif line[0] == '-':
                values.append(int(line[1:]) * -1)

    return values

if __name__ == '__main__':
    print("Starting Day1")
    # Read file into list of values
    values = read_file('input.txt')

    # Iterate and apply values to frequency
    current = 0
    for val in values:
        current += val

    # Print out answer
    print("The final frequency is : {0}".format(str(current)))
