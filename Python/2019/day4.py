# Find number of possible passwords in range

def find_passwords(values, use_part2=False):

    def check_password(pw):
        if use_part2:
            return check_password2(pw)
        check_str = str(pw)
        has_double = False
        is_valid = True
        for index in range(1, len(check_str)):
            if check_str[index] == check_str[index - 1]:
                has_double = True
            elif check_str[index] < check_str[index - 1]:
                is_valid = False
                break
        return is_valid and has_double

    def check_password2(pw):
        check_str = str(pw)
        is_valid = True
        counts = {}
        for index in range(len(check_str)):
            if index > 0 and check_str[index] < check_str[index - 1]:
                is_valid = False
                break
            counts[check_str[index]] = counts.get(check_str[index], 0) + 1

        has_double = False
        for count in counts.values():
            if count == 2:
                has_double = True
        return is_valid and has_double

    passwords = []
    if len(values) == 3:
        for val in values:
            if check_password(val):
                passwords.append(val)
    else:
        runner = int(values[0])
        end = int(values[1])
        while runner <= end:
            # Convert to string and iterate through digits
            if check_password(runner):
                passwords.append(runner)

            runner += 1

    return len(passwords)


def part1(values):
    return find_passwords(values)


def part2(values):
    return find_passwords(values, True)
