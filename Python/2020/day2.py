# Determine which passwords are valid based on occurrence of characters

def valid_passwords(values, use_part2=False):
    # For this first part of the problem, we are just iterating through the list, determining the rule and checking the
    # password, and counting the results
    total_count = 0
    for val in values:
        # Split the line into rule and password
        rule, password = val.split(':')
        # Now split the rule into positions and character
        rule_positions, rule_character = rule.split(' ')
        # Now split positions into first and second (low and high in first part)
        rule_first, rule_second = rule_positions.split('-')

        # Now we can check the password for the number of characters it needs to have
        count = 0
        if use_part2:
            password_first = password.strip()[int(rule_first) - 1]
            password_second = password.strip()[int(rule_second) - 1]
            if (password_first == rule_character and password_second != rule_character) or \
                    (password_first != rule_character and password_second == rule_character):
                total_count += 1
        else:
            for char in password:
                if char == rule_character:
                    count += 1
            if int(rule_first) <= count <= int(rule_second):
                total_count += 1

    return total_count


def part1(values):
    return valid_passwords(values)


def part2(values):
    return valid_passwords(values, True)
