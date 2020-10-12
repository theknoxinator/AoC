# Determine an MD5 hash that fits the criteria of starting with 5 zeroes based on a given secret key
import hashlib

secret_key = "iwrupvqb"
test_data = "abcdef"

if __name__ == '__main__':
    print("Starting Day4-1")

    # Starting with 1, increment and append to the secret key and calculate a hash
    found_hash = False
    number = 1
    while not found_hash:
        md5 = hashlib.new('md5')
        value = secret_key + str(number)
        md5.update(value.encode('utf-8'))
        hash = md5.hexdigest()
        if hash[:5] == '00000':
            found_hash = True
        else:
            number += 1

    # Print out answer
    print("The lowest number for hashing is: {0}".format(str(number)))
