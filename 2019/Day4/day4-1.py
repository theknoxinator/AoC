# Find number of possible passwords in range

min = 357253
max = 892942

print("Starting Day4")

passwords = []
runner = min
while runner <= max:
    # Convert to string and iterate through digits
    check_str = str(runner)
    has_double = False
    is_valid = True
    for index in range(1, len(check_str)):
        if check_str[index] == check_str[index - 1]:
            has_double = True
        elif check_str[index] < check_str[index - 1]:
            is_valid = False
            break
    if is_valid and has_double:
        passwords.append(runner)

    runner += 1

print("The number of valid passwords is: {0!s}".format(len(passwords)))
for password in passwords:
    print(password)