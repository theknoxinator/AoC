# Determine the message trying to be sent via repeated corrupted input

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["eedadn",
            "drvtee",
            "eandsr",
            "raavrd",
            "atevrs",
            "tsrnev",
            "sdttsa",
            "rasrtv",
            "nssdts",
            "ntnada",
            "svetve",
            "tesnvt",
            "vntsnd",
            "vrdear",
            "dvrsen",
            "enarar"]


if __name__ == '__main__':
    print("Starting Day 6-1")
    values = read_file('input.txt')
    # values = test_data()

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
    message = ""
    for position in range(len(counts)):
        pos_dict = counts[position]
        highest_count = 0
        highest_letter = None
        for key,value in pos_dict.items():
            if value > highest_count:
                highest_count = value
                highest_letter = key
        message += highest_letter

    # Print out answer
    print("The message is: {0}".format(message))
