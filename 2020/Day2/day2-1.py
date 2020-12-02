# Determine which passwords are valid based on occurence of characters

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


print("Starting Day2-1")
values = read_file("input.txt")
# values = test_data()

# For this first part of the problem, we are just iterating through the list, determining the rule and checking the
# password, and counting the results
total_count = 0
for val in values:
    # Split the line into rule and password
    rule, password = val.split(':')
    # Now split the rule into range and character
    rule_range, rule_character = rule.split(' ')
    # Now split range into low and high
    rule_low, rule_high = rule_range.split('-')

    # Now we can check the password for the number of characters it needs to have
    count = 0
    for char in password:
        if char == rule_character:
            count += 1
    if int(rule_low) <= count <= int(rule_high):
        print("Y: {0!s}".format(val))
        total_count += 1
    else:
        print("N: {0!s}".format(val))

print("Total valid passwords: {0!s}".format(total_count))