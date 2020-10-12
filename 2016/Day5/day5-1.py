# Determine the password for a door using increasing MD5 hashes based on a prefix
import hashlib

secret_key = "cxdnnyjw"
test_data = "abc"

if __name__ == '__main__':
    print("Starting Day 5-1")

    # Starting with 1, increment and append to the secret key and calculate a hash starting with 5 zeroes
    # Once found, append the first non-zero character of the hash to the password
    password = ""
    number = 0
    while len(password) < 8:
        md5 = hashlib.new('md5')
        value = secret_key + str(number)
        md5.update(value.encode('utf-8'))
        hash = md5.hexdigest()
        if hash[:5] == '00000':
            print("Hash for value: {0} is: {1}".format(value, hash))
            password += hash[5]
        number += 1

    # Print out answer
    print("The password is: {0}".format(password))
