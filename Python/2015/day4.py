# Determine the lowest number that creates a MD5 hash that starts with multiple zeroes
import hashlib


def find_hash(secret_key, prefix):
    number = 1
    while True:
        md5 = hashlib.new('md5')
        value = secret_key + str(number)
        md5.update(value.encode('utf-8'))
        hash = md5.hexdigest()
        if hash[:len(prefix)] == prefix:
            return number
        else:
            number += 1


def part1(values):
    return find_hash(values[0], '00000')

def part2(values):
    return find_hash(values[0], '000000')
