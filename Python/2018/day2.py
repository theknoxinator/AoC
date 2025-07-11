# Create checksum using IDs from a file
# Checksum is created by multiplying the number of IDs with at least one letter that occurs twice
# with the number of IDs with at least one letter that occurs thrice

def gen_checksum(values):
    # Iterate and check to see if value has letters that repeat twice or thrice
    twice = 0
    thrice = 0
    for val in values:
        # Initialize array
        counts = [0] * 26

        # Count each letter in ID
        for letter in val:
            index = ord(letter) - 97
            counts[index] += 1

        # Check to see if there are repeats
        has_twice = False
        has_thrice = False
        for count in counts:
            if count == 2:
                has_twice = True
            elif count == 3:
                has_thrice = True

        if has_twice:
            twice += 1
        if has_thrice:
            thrice += 1

    # Calculate the checksum
    checksum = twice * thrice
    return checksum


def find_common_ids(values):
    # Iterate through list and compare each ID to every other ID
    common_id = ""
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            first_id = values[i]
            second_id = values[j]
            for k in range(len(first_id)):
                alt_first_id = first_id[:k] + first_id[k + 1:]
                alt_second_id = second_id[:k] + second_id[k + 1:]
                if alt_first_id == alt_second_id:
                    common_id = alt_first_id

    return common_id


def part1(values):
    return gen_checksum(values)


def part2(values):
    return find_common_ids(values)
