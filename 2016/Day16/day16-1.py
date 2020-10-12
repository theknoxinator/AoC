# Fill a disc with random data and get a checksum for the randomly created data

input_data = "11011110011011101"
# length = 272
length = 35651584 # This is the second problem's length
# input_data = "10000"
# length = 20


if __name__ == '__main__':
    print("Starting Day 16-1")

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

    # Run some tests to make sure we are doing it right
    print("Expect: {0}".format("100"))
    print("Actual: {0}".format('1' + '0' + get_b('1')))
    print("Expect: {0}".format("001"))
    print("Actual: {0}".format('0' + '0' + get_b('0')))
    print("Expect: {0}".format("11111000000"))
    print("Actual: {0}".format('11111' + '0' + get_b('11111')))
    print("Expect: {0}".format("1111000010100101011110000"))
    print("Actual: {0}".format('111100001010' + '0' + get_b('111100001010')))

    print("For 110010110100, the checksum is {0}".format(get_checksum("110010110100")))

    # Now run the real thing
    data = input_data
    while len(data) <= length:
        data = data + '0' + get_b(data)

    data = data[:length]

    checksum = get_checksum(data)
    print("The checksum for input {0} is {1}".format(input_data, checksum))
