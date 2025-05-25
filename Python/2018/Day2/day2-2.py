# Find IDs that are only one letter apart
# The correct IDs can be found by subtracting a letter at the same index from each to get the same remainder

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values

def test_data():
    return ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

if __name__ == '__main__':
    print("Starting Day 2-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Iterate through list and compare each ID to every other ID
    id_pair = (-1, -1)
    common_id = ""
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            first_id = values[i]
            second_id = values[j]
            for k in range(len(first_id)):
                alt_first_id = first_id[:k] + first_id[k+1:]
                alt_second_id = second_id[:k] + second_id[k+1:]
                if alt_first_id == alt_second_id:
                    common_id = alt_first_id
                    id_pair = (i, j)

    # Print out answer
    print("The matching IDs are: {0} and {1}".format(values[id_pair[0]], values[id_pair[1]]))
    print("The common part of the IDs is: {0}".format(common_id))