# Determine the number of IPv7 addresses that have an ABBA annotation in them

def find_annotations(values):
    # For this problem, we just need to read each input, iterate over each four characters and determine
    # if there is an ABBA annotation (two different letters followed by its reverse), unless it is within
    # a set of square brackets
    total_ips = 0
    for val in values:
        # Iterate over the string up to the fourth to last position
        in_square = False
        has_abba = False
        for index in range(len(val) - 3):
            # Get the first two characters
            first = val[index]
            second = val[index + 1]

            # First, check to see if the first character is a square bracket since we can ignore them
            if first == '[':
                in_square = True
                continue
            elif first == ']':
                in_square = False
                continue

            # Second, check to make sure the two characters are different
            if first == second:
                continue

            # Now, check for a repeat of its reverse
            if first == val[index + 3] and second == val[index + 2]:
                has_abba = True
                # We have a match, but if it's inside square brackets, it invalidates the whole thing
                if in_square:
                    break

        # If we have an abba match, but it's in a square, we don't count it, otherwise we do
        if has_abba and not in_square:
            total_ips += 1

    return total_ips


def find_annotations2(values):
    # For this problem, we need to iterate over each three letters and determine if it's an ABA pattern
    # match. We keep all of these matches in a couple lists, one for inside square brackets and one for
    # outside. Then we check each pattern to see if an ABA is in one list and a BAB in the other.
    total_ips = 0
    for val in values:
        in_square = False
        outside_patterns = []
        inside_patterns = []
        # Iterate over the string up to the third to last position
        for index in range(len(val) - 2):
            # Get the three characters
            first = val[index]
            second = val[index + 1]
            third = val[index + 2]

            # First, check to see if the first or second character is a square bracket since we can ignore
            # them
            if first == '[':
                in_square = True
                continue
            elif first == ']':
                in_square = False
                continue
            elif second == '[' or second == ']':
                # We don't want to get a match like 'a[a'
                continue

            # Second, check to make sure the two characters are different
            if first == second:
                continue

            # Now, check to see if it is a pattern
            if first == val[index + 2]:
                # We have a match, so put it in the correct bucket
                if in_square:
                    inside_patterns.append(first + second + third)
                else:
                    outside_patterns.append(first + second + third)

        # Now we need to see if any patterns match
        for aba in outside_patterns:
            bab = aba[1] + aba[0] + aba[1]
            if bab in inside_patterns:
                total_ips += 1
                break

    return total_ips


def part1(values):
    return find_annotations(values)


def part2(values):
    return find_annotations2(values)
