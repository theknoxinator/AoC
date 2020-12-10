# Determine the distribution of differences for your adapters

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    # return ["16", "10", "15", "5", "1", "11", "7", "19", "6", "12", "4"]

    return ["28", "33", "18", "42", "31", "14", "46", "20", "48", "47", "24", "23", "49", "45", "19", "38", "39", "11",
            "1", "32", "25", "35", "8", "17", "7", "9", "4", "2", "34", "10", "3"]


print("Starting Day10-1")
values = read_file("input.txt")
# values = test_data()

# This problem seems to be as easy as sorting the numbers and just determining the differences between each pair and
# counting them
# First, convert the input to numbers, add in 0 for the outlet and the max + 3 for the device to charge
adapters = [int(x) for x in values]
adapters.append(0)
adapters.append(max(adapters) + 3)
# Now sort
adapters = sorted(adapters)
differences = dict()
for i in range(len(adapters) - 1):
    difference = adapters[i + 1] - adapters[i]
    if difference not in differences:
        differences[difference] = 1
    else:
        differences[difference] += 1

print(differences)
print("The product of the 1-differences and 3-differences is: {0!s}".format(differences[1] * differences[3]))
