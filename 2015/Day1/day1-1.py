# Change floors based on inputs from file
# Left paren ( goes up one floor, right paren ) goes down one floor
# No limit on up or down

def read_file(filename):
    with open(filename, 'r') as f:
        return f.readline()

def test_data():
    return "()()((("

if __name__ == '__main__':
    print("Starting Day1")
    # Read file for line of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate and apply values to floor
    floor = 0
    for val in values:
        if val == '(':
            floor += 1
        elif val == ')':
            floor -= 1

    # Print out answer
    print("The final floor is : {0}".format(str(floor)))
