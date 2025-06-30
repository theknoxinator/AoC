# Determine the message trying to be sent via repeated corrupted input

def find_message(values):
    # The message is going to be the most repeated letter in each position, so create an array of maps to
    # store the count of each character in each position
    message_len = len(values[0])
    counts = [dict() for i in range(message_len)]

    # Now go through each corrupted message and add the character to the counts
    for val in values:
        for index in range(len(val)):
            char = val[index]
            if char not in counts[index]:
                counts[index][char] = 0
            counts[index][char] += 1

    # With all the character counts, now determine which character is most repeated in each position
    highest_message = ""
    lowest_message = ""
    for position in range(len(counts)):
        pos_dict = counts[position]
        lowest_count = len(values)
        lowest_letter = None
        highest_count = 0
        highest_letter = None
        for key,value in pos_dict.items():
            if value > highest_count:
                highest_count = value
                highest_letter = key
            if value < lowest_count:
                lowest_count = value
                lowest_letter = key
        highest_message += highest_letter
        lowest_message += lowest_letter

    return highest_message, lowest_message


def part1(values):
    return find_message(values)[0]


def part2(values):
    return find_message(values)[1]
