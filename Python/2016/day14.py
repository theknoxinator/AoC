# Determine a set of one-time keys using increasing MD5 hashes based on a prefix
import hashlib

def create_hashes(values, use_part2=False):
    secret_key = values[0]

    triplets = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999', 'aaa', 'bbb', 'ccc', 'ddd', 'eee',
                'fff']

    # Starting with 1, increment and see if the hash contains a triplet. If so, keep it in a dictionary to reference
    # later as we need to make sure it is followed by quintuplet within 1000 keys
    possible_indexes = {}
    actual_indexes = []
    hashes = []
    index = 0
    while index < 99999:
        md5 = hashlib.new('md5')
        value = secret_key + str(index)
        md5.update(value.encode('utf-8'))
        hash = md5.hexdigest()
        if use_part2:
            # New to this area, we need to rehash the hash 2016 times
            for repeat in range(2016):
                md5 = hashlib.new('md5')
                md5.update(hash.encode('utf-8'))
                hash = md5.hexdigest()
        hashes.append(hash)


        # First, look to see if any quintuplets are in the hash and remove them from possibles if so
        for possible_index in set(possible_indexes.keys()):
            if possible_index < index - 1000:
                # Index is beyond range now, so just remove
                del possible_indexes[possible_index]
            elif possible_indexes[possible_index] in hash:
                actual_indexes.append((possible_index, index))
                del possible_indexes[possible_index]

        # Next, look to see if triplet is in the hash
        for start in range(len(hash)-2):
            triplet = hash[start:start+3]
            if triplet in triplets:
                possible_indexes[index] = triplet + triplet[:2]
                break

        index += 1

    return sorted(actual_indexes)[63][0]


def part1(values):
    return create_hashes(values)


def part2(values):
    return create_hashes(values, True)
