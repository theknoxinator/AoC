# Calculate the sum of fuel needed for many masses

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    # return ["12"]
    # return ["14"]
    # return ["1969"]
    return ["100756"]

print("Starting Day1")
values = read_file('input.txt')
# values = test_data()

# Iterate and calculate individual fuel needs and add to total
total = 0
for val in values:
    mass = int(val)
    fuel = int(mass / 3) - 2
    print("Mass: {0!s} to fuel: {1!s}".format(mass, fuel))
    total += fuel

print("The total amount of fuel is: {0!s}".format(total))