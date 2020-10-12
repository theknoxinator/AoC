# Unscramble a password based on a file with rules in it

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["swap position 4 with position 0",
            "swap letter d with letter b",
            "reverse positions 0 through 4",
            "rotate left 1 step",
            "move position 1 to position 4",
            "move position 3 to position 0",
            "rotate based on position of letter b",
            "rotate based on position of letter d"]


if __name__ == "__main__":
    print("Starting Day 21-2")
    values = read_file("input.txt")
    # values = test_data()

    # We are starting with the scrambled password, and we need to reverse each rule to get back to the original
    password = list("fbgdceah")

    # Iterate through each rule in reverse order and undo what it says
    values.reverse()
    for val in values:
        words = val.split()
        if "swap position" in val:
            # Swap letters at indexes x and y (no change here)
            x, y = int(words[2]), int(words[5])
            letter_x, letter_y = password[x], password[y]
            password[x] = letter_y
            password[y] = letter_x
        elif "swap letter" in val:
            # Swap letters by value (no change here)
            x, y = words[2], words[5]
            index_x, index_y = password.index(x), password.index(y)
            password[index_x] = y
            password[index_y] = x
        elif "rotate left" in val:
            # Now we need to rotate to the right
            turns = int(words[2])
            for i in range(turns):
                password.insert(0, password.pop())
        elif "rotate right" in val:
            # Now we need to rotate to the left
            turns = int(words[2])
            for i in range(turns):
                password.append(password.pop(0))
        elif "rotate based" in val:
            # Now we need to rotate to the left back to its original position
            letter = words[6]
            index = password.index(letter)
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
        elif "reverse" in val:
            # Reverse a sub section of the password (no change here)
            x, y = int(words[2]), int(words[4])
            password = password[:x] + password[x:y+1][::-1] + password[y+1:]
        elif "move" in val:
            # Move a letter, switching the x and y this time
            x, y = int(words[2]), int(words[5])
            password.insert(x, password.pop(y))

        print(''.join(password))
