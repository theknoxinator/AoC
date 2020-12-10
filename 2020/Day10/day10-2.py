# Determine the number of distinct adapter combinations

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


print("Starting Day10-2")
values = read_file("input.txt")
# values = test_data()

# This problem is much more difficult as it's a pathing problem, and the only way I know how to do that is recursion
# First, convert the input to numbers, add in 0 for the outlet and the max + 3 for the device to charge
adapters = [int(x) for x in values]
adapters.append(0)
adapters.append(max(adapters) + 3)
# Now sort
adapters = sorted(adapters)

# This time around we are going to start at the end and work our way backward, calculating the number of possible
# routes for each adapter as we go back
possibilities = {max(adapters): 1}
for i in range(len(adapters) - 2, -1, -1):
    adapter = adapters[i]
    routes = 0
    if (adapter + 1) in adapters:
        routes += possibilities[adapter + 1]
    if (adapter + 2) in adapters:
        routes += possibilities[adapter + 2]
    if (adapter + 3) in adapters:
        routes += possibilities[adapter + 3]
    possibilities[adapter] = routes

print(possibilities)
print("Total number of routes: {0!s}".format(possibilities[0]))
