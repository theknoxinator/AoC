# Determine the total number of IP addresses that are not blocked

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values


def test_data():
    return ["5-8", "0-2", "4-7"]


if __name__ == "__main__":
    print("Starting Day 20-2")
    values = read_file('input.txt')
    # values = test_data()

    # Create a list of start and end values from the input
    blocks = []
    for val in values:
        start,end = val.split('-')
        blocks.append((int(start), int(end)))

    # Now start at 0 and keep incrementing it until we hit the limit of 2^32
    address = 0
    unblocked = 0
    while address < 4294967296:
        is_blocked = False
        for block in blocks:
            start,end = block
            if address >= start and address <= end:
                address = end + 1
                is_blocked = True
                break
        if not is_blocked:
            unblocked += 1
            address += 1

    # Print out total number of addresses
    print("The number of non-blocked addresses is: {0!s}".format(unblocked))
