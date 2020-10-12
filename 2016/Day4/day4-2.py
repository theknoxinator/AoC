# Determine the sum of the sector IDs of all valid rooms in a given input
# Second part: decrypt the valid rooms and determine which sector ID belongs to the north pole objects
from operator import itemgetter

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["qzmt-zixmtkozy-ivhz-343[zimth]"]


if __name__ == '__main__':
    print("Starting Day 4-2")
    # Read file into list of values
    values = read_file('input.txt')
    # values = test_data()

    # Iterate and check each value to see if it's a valid room, and if so, decrypt the name and print
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

        # Last, if the checksums match, then decrypt the room
        if result_checksum == checksum:
            offset = int(sector_id) % 26
            room_name = ""
            for part in name:
                for letter in part:
                    new_letter = ord(letter) + offset
                    if new_letter > ord('z'):
                        new_letter -= 26
                    room_name += chr(new_letter)
                room_name += " "

            print("Sector ID: {0}, {1}".format(sector_id, room_name))
