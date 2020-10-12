# Change frequency based on inputs from file
# Positive frequency change adds to current value, negative change subtracts
# Find first repeated frequency based on input, can loop through list multiple times to get there

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            if line[0] == '+':
                values.append(int(line[1:]))
            elif line[0] == '-':
                values.append(int(line[1:]) * -1)

    return values

def test_data():
    return [1, -2, 3, 1]

if __name__ == '__main__':
    print("Starting Day1-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and apply values to frequency
    past_frequencies = [0]
    current = 0
    found_past = False
    loops = 0
    while not found_past:
        print("Number of frequencies calculated: {0}".format(str(len(past_frequencies))))
        for val in values:
            loops += 1
            current += val
            if current not in past_frequencies:
                past_frequencies.append(current)
            else:
                print("Number of loops occurred: {0}".format(str(loops)))
                found_past = True
                break


    # Print out answer
    print("The first repeated frequency is : {0}".format(str(current)))
