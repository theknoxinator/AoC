# Determine the sum of the sector IDs of all valid rooms in a given input
from operator import itemgetter

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["aaaaa-bbb-z-y-x-123[abxyz]",
            "a-b-c-d-e-f-g-h-987[abcde]",
            "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]"]


if __name__ == '__main__':
    print("Starting Day 4-1")
    # Read file into list of values
    values = read_file('input.txt')
    # values = test_data()

    # Iterate and check each value to see if it's a valid room, and if so, add to the sector ID sum
    sector_sum = 0
    for val in values:
        # First split the room name by hyphen to separate the letters from the sector ID and checksum
        items = val.split('-')
        sector_checksum = items[-1]
        name = items[:-1]

        # Second, separate the sector ID and checksum
        sector_id,checksum = sector_checksum.replace('[', ' ').replace(']', '').split()

        # Third, run through the name and count up all the letters
        letter_count = {}
        for part in name:
            for letter in part:
                if letter not in letter_count:
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1

        # Fourth, determine what the checksum should be
        sorted_counts = sorted(sorted(letter_count.items(), key=itemgetter(0)), key=itemgetter(1), reverse=True)
        result_checksum = ''.join([item[0] for item in sorted_counts[:5]])

        # Last, if the checksums match, then add sector ID to sum
        if result_checksum == checksum:
            print("Valid room: {0}".format(val))
            sector_sum += int(sector_id)


    # Print out answer
    print("The sector sum is: {0!s}".format(sector_sum))
