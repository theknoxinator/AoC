# Determine the score of all the groups within an input of characters that are grouped by brackets

def bracket_score(values):
    pattern = values[0]

    # This is a simple stacking problem with a couple twists
    stack = []
    score = 0
    index = 0
    garbage = 0
    is_garbage = False
    while index < len(pattern):
        if pattern[index] == '{' and not is_garbage:
            # We found the start of a new group
            stack.append('{')
        elif pattern[index] == '}' and not is_garbage:
            # We found the end of a group, so score and pop from stack
            score += len(stack)
            stack.pop()
        elif pattern[index] == '<' and not is_garbage:
            # We found the start of some garbage, so set the flag to true
            is_garbage = True
        elif pattern[index] == '>':
            # We found the end of some garbage, so set the flag to false
            is_garbage = False
        elif pattern[index] == '!':
            # We found a bang, which means we always skip the next character
            index += 1
        elif is_garbage:
            # This character is not special and contained with a garbage part, so count it
            garbage += 1
        index += 1

    return score, garbage


def part1(values):
    return bracket_score(values)[0]


def part2(values):
    return bracket_score(values)[1]
