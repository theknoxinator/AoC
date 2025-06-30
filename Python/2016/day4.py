# Determine the sum of the sector IDs of all valid rooms in a given input
from operator import itemgetter

def get_sector_ids(values):
    # Iterate and check each value to see if it's a valid room, and if so, add to the sector ID sum or decrypt the room
    sector_sum = 0
    target_room = 0
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

        # Last, if the checksums match, then add sector ID to sum and decrypt the room
        if result_checksum == checksum:
            sector_sum += int(sector_id)
            offset = int(sector_id) % 26
            room_name = ""
            for part in name:
                for letter in part:
                    new_letter = ord(letter) + offset
                    if new_letter > ord('z'):
                        new_letter -= 26
                    room_name += chr(new_letter)
                room_name += " "

            if room_name.strip() == "northpole object storage":
                target_room = sector_id

    return sector_sum, target_room


def part1(values):
    return get_sector_ids(values)[0]


def part2(values):
    return get_sector_ids(values)[1]
