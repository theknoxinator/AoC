# Determine the distribution of differences for your adapters

def find_differences(values):
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

    return differences[1] * differences[3], possibilities[0]


def part1(values):
    return find_differences(values)[0]


def part2(values):
    return find_differences(values)[1]
