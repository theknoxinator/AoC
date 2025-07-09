# Determine which passphrases are valid assuming that they cannot contain duplicate words

def find_valid_phrases(values, use_part2=False):
    # Iterate through each and do a simple split, then throw each word into a set
    good = 0
    bad = 0
    for val in values:
        words = val.split()
        unique = set()
        has_dup = False
        for word in words:
            if use_part2:
                word = ''.join(sorted(word))
            if word not in unique:
                unique.add(word)
            else:
                has_dup = True
                break

        if has_dup:
            bad += 1
        else:
            good += 1

    return good


def part1(values):
    return find_valid_phrases(values)


def part2(values):
    return find_valid_phrases(values, True)
