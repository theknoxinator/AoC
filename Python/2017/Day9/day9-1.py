# Determine the score of all the groups within an input of characters that are grouped by brackets


def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    # return ["{}"]
    # return ["{{{}}}"]
    # return ["{{},{}}"]
    # return ["{{{},{},{{}}}}"]
    # return ["{<a>,<a>,<a>,<a>}"]
    # return ["{{<ab>},{<ab>},{<ab>},{<ab>}}"]
    # return ["{{<!!>},{<!!>},{<!!>},{<!!>}}"]
    return ["{{<a!>},{<a!>},{<a!>},{<ab>}}"]


if __name__ == "__main__":
    print("Starting Day 9-1")
    values = read_file("input.txt")
    # values = test_data()

    input = values[0]

    # This is a simple stacking problem with a couple twists
    stack = []
    score = 0
    index = 0
    is_garbage = False
    while index < len(input):
        if input[index] == '{' and not is_garbage:
            # We found the start of a new group
            stack.append('{')
        elif input[index] == '}' and not is_garbage:
            # We found the end of a group, so score and pop from stack
            score += len(stack)
            stack.pop()
        elif input[index] == '<' and not is_garbage:
            # We found the start of some garbage, so set the flag to true
            is_garbage = True
        elif input[index] == '>':
            # We found the end of some garbage, so set the flag to false
            is_garbage = False
        elif input[index] == '!':
            # We found a bang, which means we always skip the next character
            index += 1
        index += 1

    print("The score of this input is: {0!s}".format(score))
