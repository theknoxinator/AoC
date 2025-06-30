# Determine the lowest IP address from a list of blocked addresses, IPs are given as raw numbers

def find_ips(values):
    # Create a list of start and end values from the input
    blocks = []
    max_address = 4294967296
    max_end = 0
    for val in values:
        start,end = val.split('-')
        blocks.append((int(start), int(end)))
        max_end = max(max_end, int(end))
    if max_end < 10:
        max_address = 9

    # Now start at 0 and keep incrementing it until we are not in any block in the list above
    address = 0
    unblocked = []
    while address < max_address:
        is_blocked = False
        for block in blocks:
            start,end = block
            if address >= start and address <= end:
                address = end + 1
                is_blocked = True
                break
        if not is_blocked:
            unblocked.append(address)
            address += 1

    return min(unblocked), len(unblocked)


def part1(values):
    return find_ips(values)[0]


def part2(values):
    return find_ips(values)[1]
