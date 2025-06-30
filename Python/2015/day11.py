# Calculate the next password based on incrementing each letter by one and fitting the assigned
# criteria

test_data = "ghijklmn"

def increment_password(password):
    carryover = 1
    index = len(password) - 1
    while carryover > 0 and index > 0:
        carryover = 0
        char = password[index]
        if char == 'z':
            carryover = 1
            password = password[:index] + 'a' + password[index+1:]
        else:
            password = password[:index] + chr(ord(char)+1) + password[index+1:]
        index -= 1
    return password

def calc_password(start):
    is_valid = False
    new_password = start
    while not is_valid:
        new_password = increment_password(new_password)

        if any((c in 'iol') for c in new_password):
            # Disallowed characters
            continue

        # Check for pairs of characters
        pairs = set()
        has_pairs = False
        for index in range(len(new_password)-1):
            if new_password[index] == new_password[index+1]:
                pairs.add(new_password[index:index+2])
        if len(pairs) >= 2:
            has_pairs = True

        # Check for increasing straight
        has_straight = False
        for index in range(len(new_password)-2):
            first = ord(new_password[index])
            if ord(new_password[index+1]) == first + 1 and ord(new_password[index+2]) == first + 2:
                has_straight = True
                break

        if has_pairs and has_straight:
            is_valid = True

    return new_password

def part1(values):
    return calc_password(values[0])


def part2(values):
    return calc_password(calc_password(values[0]))
