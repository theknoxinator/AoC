# Determine the password for a door using increasing MD5 hashes based on a prefix
import hashlib

def make_password(values, use_part2=False):
    # Starting with 1, increment and append to the secret key and calculate a hash starting with 5 zeroes
    # Once found, append the first non-zero character of the hash to the password
    secret_key = values[0]
    password = [None] * 8
    characters = 0
    position = 0
    number = 0
    while characters < 8:
        md5 = hashlib.new('md5')
        value = secret_key + str(number)
        md5.update(value.encode('utf-8'))
        hash = md5.hexdigest()
        if hash[:5] == '00000':
            if not use_part2:
                password[position] = hash[5]
                position += 1
                characters += 1
            else:
                position = int(hash[5], 16)
                if position < len(password) and password[position] is None:
                    password[position] = hash[6]
                    characters += 1
        number += 1

    return ''.join(password)


def part1(values):
    return make_password(values)


def part2(values):
    return make_password(values, True)
