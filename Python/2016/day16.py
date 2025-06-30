# Fill a disc with random data and get a checksum for the randomly created data

def calc_checksum(values):
    def get_b(a):
        reverse_a = a[::-1]
        b = ""
        for char in reverse_a:
            b += '0' if char == '1' else '1'
        return b

    def get_checksum(data):
        checksum = data
        while len(checksum) % 2 == 0:
            new_checksum = ""
            for index in range(0, len(checksum), 2):
                if checksum[index] == checksum[index + 1]:
                    new_checksum += '1'
                else:
                    new_checksum += '0'
            checksum = new_checksum

        return checksum

    input_data = values[0]
    length = int(values[1])

    # Now run the real thing
    data = input_data
    while len(data) <= length:
        data = data + '0' + get_b(data)

    data = data[:length]

    checksum = get_checksum(data)
    return checksum


def part1(values):
    return calc_checksum(values)


def part2(values):
    values[1] = "35651584"
    return calc_checksum(values)
