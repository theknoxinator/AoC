# Determine the number of combinations of given containers can hold a given amount of liquid

def find_combinations(values):
    target_size = 25 if len(values) == 5 else 150

    # Create a list for containing the different valid collections
    collections = []

    # This algorithm will use bitmasking to determine which containers to use, and check to see if
    # their sum adds up to the target size
    for mask in range(1 << len(values)):
        sum = 0
        get_bit = 1
        collection = []
        for index in range(len(values)):
            if get_bit & mask:
                sum += values[index]
                collection.append(values[index])
            get_bit = get_bit << 1

        if sum == target_size:
            collections.append(collection)

    # Now determine the minimum number of containers needed, and how many combinations there are that
    # use that number
    smallest_size = len(values)
    for collection in collections:
        if len(collection) < smallest_size:
            smallest_size = len(collection)

    min_collections = []
    for collection in collections:
        if len(collection) == smallest_size:
            min_collections.append(collection)

    return len(collections), len(min_collections)


def part1(values):
    return find_combinations(list(map(int, values)))[0]


def part2(values):
    return find_combinations(list(map(int, values)))[1]
