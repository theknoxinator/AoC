# Determine the number of combinations of given containers can hold a given amount of liquid

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(int(line))

    return values

def test_data():
    return [20, 15, 10, 5, 5]

if __name__ == '__main__':
    print("Starting Day17-1")
    # Read file into list of values
    values = sorted(read_file('input.txt'))
    #values = sorted(test_data())
    print(' '.join(map(str, values)))

    target_size = 150
    #target_size = 25

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

    # Print out answer
    for collection in collections:
        print("{0}".format(' '.join(map(str, collection))))
    print("Total number of combinations is: {0}".format(str(len(collections))))
