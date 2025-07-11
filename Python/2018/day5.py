# Remove all matching units from a long string of characters. Matching units are considered to be a
# lower-case and upper-case of the same character.
import sys


def find_polymer(values, use_part2=False):
    pattern = values[0]

    def modify_polymer(p):
        has_changed = True
        while has_changed:
            has_changed = False
            index = 0
            while index < len(p) - 1:
                char = ord(p[index])
                if char >= 65 and char <= 90:
                    # Uppercase
                    if ord(p[index+1]) == char + 32:
                        p = p[:index] + p[index+2:]
                        has_changed = True
                    else:
                        index += 1
                elif char >= 97 and char <= 122:
                    # Lowercase
                    if ord(p[index+1]) == char - 32:
                        p = p[:index] + p[index+2:]
                        has_changed = True
                    else:
                        index += 1
                else:
                    index += 1
        return p

    if not use_part2:
        result = modify_polymer(pattern)
        return len(result)
    else:
        shortest_length = sys.maxsize
        for remove_char in range(ord('A'), ord('Z') + 1):
            polymer = pattern.replace(chr(remove_char), '').replace(chr(remove_char + 32), '')
            polymer = modify_polymer(polymer)
            shortest_length = min(shortest_length, len(polymer))
        return shortest_length


def part1(values):
    return find_polymer(values)


def part2(values):
    return find_polymer(values, True)
