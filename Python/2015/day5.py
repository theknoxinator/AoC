# Determine which strings are good or bad based on criteria
def part1(values):
    # Good strings do not have disallowed substrings, must have at least 3 vowels, and has at least one double letter
    good_strings = 0
    for text_string in values:
        has_disallowed = False
        for check in ['ab', 'cd', 'pq', 'xy']:
            has_disallowed = has_disallowed or (check in text_string)

        vowels = 0
        for char in text_string:
            if char in 'aeiou':
                vowels += 1
        has_vowels = vowels >= 3

        has_double = False
        for i in range(len(text_string) - 1):
            has_double = has_double or (text_string[i] == text_string[i + 1])

        if not has_disallowed and has_vowels and has_double:
            good_strings += 1

    return good_strings


def part2(values):
    # Good strings must have a pair of characters show up at least twice, and at least one instance of a repeating
    # character with one different character in between
    good_strings = 0
    for text_string in values:
        has_double_pair = False
        pairs = {}
        for i in range(len(text_string) - 1):
            pair = text_string[i:i + 2]
            if pair in pairs:
                if i - pairs[pair] > 1:
                    has_double_pair = True
                    break
            else:
                pairs[pair] = i

        has_double = False
        for i in range(len(text_string) - 2):
            has_double = has_double or (text_string[i] == text_string[i + 2])

        if has_double_pair and has_double:
            good_strings += 1

    return good_strings
