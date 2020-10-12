# Find number of possible passwords in range

min = 357253
max = 892942

print("Starting Day4-2")

passwords = []
runner = min
while runner <= max:
    # Convert to string and iterate through digits
    check_str = str(runner)
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

    if is_valid and has_double:
        passwords.append(runner)

    runner += 1

print("The number of valid passwords is: {0!s}".format(len(passwords)))
# for password in passwords:
#     print(password)
