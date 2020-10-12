# Change floors based on inputs from file
# Left paren ( goes up one floor, right paren ) goes down one floor
# Find position where floor goes below 0

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    return "()())((("

if __name__ == '__main__':
    print("Starting Day1-2")
    # Read file for line of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and apply values to floor
    floor = 0
    position = 0
    for val in values:
        position += 1
        if val == '(':
            floor += 1
        elif val == ')':
            floor -= 1
        if floor < 0:
            break

    # Print out answer
    print("The first time basement is hit is : {0}".format(str(position)))
