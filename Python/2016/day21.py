# Scramble a password based on a file with rules in it

def scramble_password(values, start="abcdefgh", use_part2=False):
    # We are starting with a simple password and need to read rules to determine what to do
    password = list(start)
    if len(values) < 10:
        password = list("abcde")

    # Iterate through each rule and do what it says
    if use_part2:
        values.reverse()
    for val in values:
        words = val.split()
        if "swap position" in val:
            # Swap letters at indexes x and y (does same in part2)
            x, y = int(words[2]), int(words[5])
            letter_x, letter_y = password[x], password[y]
            password[x] = letter_y
            password[y] = letter_x
        elif "swap letter" in val:
            # Swap letters by value (does same in part2)
            x, y = words[2], words[5]
            index_x, index_y = password.index(x), password.index(y)
            password[index_x] = y
            password[index_y] = x
        elif "rotate left" in val:
            # Rotate string to the left (or right if part2)
            turns = int(words[2])
            for i in range(turns):
                if use_part2:
                    password.insert(0, password.pop())
                else:
                    password.append(password.pop(0))
        elif "rotate right" in val:
            # Rotate string to the right (or left if part2)
            turns = int(words[2])
            for i in range(turns):
                if use_part2:
                    password.append(password.pop(0))
                else:
                    password.insert(0, password.pop())
        elif "rotate based" in val:
            # Rotate right based on index of value (or left if part2)
            letter = words[6]
            index = password.index(letter)
            if use_part2:
                if index == 1:
                    turns = 1
                elif index == 3:
                    turns = 2
                elif index == 5:
                    turns = 3
                elif index == 7:
                    turns = 4
                elif index == 2:
                    turns = 6
                elif index == 4:
                    turns = 7
                elif index == 6:
                    turns = 8
                else:
                    turns = 9
                for i in range(turns):
                    password.append(password.pop(0))
            else:
                turns = index + 1
                if index >= 4:
                    turns += 1
                for i in range(turns):
                    password.insert(0, password.pop())
        elif "reverse" in val:
            # Reverse a sub section of the password (does same in part2)
            x, y = int(words[2]), int(words[4])
            password = password[:x] + password[x:y+1][::-1] + password[y+1:]
        elif "move" in val:
            # Move a letter (switching x and y if part2)
            x, y = int(words[2]), int(words[5])
            if use_part2:
                password.insert(x, password.pop(y))
            else:
                password.insert(y, password.pop(x))

    return ''.join(password)


def part1(values):
    return scramble_password(values)


def part2(values):
    return scramble_password(values, "fbgdceah", True)
