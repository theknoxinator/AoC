# Determine the lowest IP address from a list of blocked addresses, IPs are given as raw numbers

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values


def test_data():
    return ["5-8", "0-2", "4-7"]


if __name__ == "__main__":
    print("Starting Day 20-1")
    values = read_file('input.txt')
    # values = test_data()

    # Create a list of start and end values from the input
    blocks = []
    for val in values:
        start,end = val.split('-')
        blocks.append((int(start), int(end)))

    # Now start at 0 and keep incrementing it until we are not in any block in the list above
    address = 0
    is_blocked = True
    while is_blocked:
        is_blocked = False
        for block in blocks:
            start,end = block
            if address >= start and address <= end:
                address = end + 1
                is_blocked = True
                break

    # Print out lowest non-blocked address
    print("The first non-blocked address is: {0!s}".format(address))
