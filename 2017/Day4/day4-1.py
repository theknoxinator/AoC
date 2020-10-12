# Determine which passphrases are valid assuming that they cannot contain duplicate words


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["aa bb cc dd ee",
            "aa bb cc dd aa",
            "aa bb cc dd aaa"]


if __name__ == "__main__":
    print("Starting Day 4-1")
    values = read_file('input.txt')
    # values = test_data()

    # Iterate through each and do a simple split, then throw each word into a set
    good = 0
    bad = 0
    for val in values:
        words = val.split()
        unique = set()
        has_dup = False
        for word in words:
            if word not in unique:
                unique.add(word)
            else:
                has_dup = True
                break

        if has_dup:
            bad += 1
        else:
            good += 1

    print("Number of good passphrases: {0!s}".format(good))
    print("Number of bad passphrases: {0!s}".format(bad))