# Determine which passwords are valid based on position of characters

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc"]


print("Starting Day2-2")
values = read_file("input.txt")
# values = test_data()

# For this first part of the problem, we are just iterating through the list, determining the rule and checking the
# password, and counting the results
total_count = 0
for val in values:
    # Split the line into rule and password
    rule, password = val.split(':')
    # Now split the rule into positions and character
    rule_positions, rule_character = rule.split(' ')
    # Now split positions into first and second
    rule_first, rule_second = rule_positions.split('-')

    # Now we can check the password for the positions of characters it needs to have
    count = 0
    password_first = password.strip()[int(rule_first) - 1]
    password_second = password.strip()[int(rule_second) - 1]
    if (password_first == rule_character and password_second != rule_character) or \
            (password_first != rule_character and password_second == rule_character):
        print("Y: {0!s}".format(val))
        total_count += 1
    else:
        print("N: {0!s}".format(val))

print("Total valid passwords: {0!s}".format(total_count))