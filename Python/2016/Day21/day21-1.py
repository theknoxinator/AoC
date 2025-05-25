# Scramble a password based on a file with rules in it

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
    print("Starting Day 21-1")
    values = read_file("input.txt")
    # values = test_data()

    # We are starting with a simple password and need to read rules to determine what to do
    password = ['a','b','c','d','e','f','g','h']

    # Iterate through each rule and do what it says
    for val in values:
        words = val.split()
        if "swap position" in val:
            # Swap letters at indexes x and y
            x, y = int(words[2]), int(words[5])
            letter_x, letter_y = password[x], password[y]
            password[x] = letter_y
            password[y] = letter_x
        elif "swap letter" in val:
            # Swap letters by value
            x, y = words[2], words[5]
            index_x, index_y = password.index(x), password.index(y)
            password[index_x] = y
            password[index_y] = x
        elif "rotate left" in val:
            # Rotate string to the left
            turns = int(words[2])
            for i in range(turns):
                password.append(password.pop(0))
        elif "rotate right" in val:
            # Rotate string to the right
            turns = int(words[2])
            for i in range(turns):
                password.insert(0, password.pop())
        elif "rotate based" in val:
            # Rotate right based on index of value
            letter = words[6]
            index = password.index(letter)
            turns = index + 1
            if index >= 4:
                turns += 1
            for i in range(turns):
                password.insert(0, password.pop())
        elif "reverse" in val:
            # Reverse a sub section of the password
            x, y = int(words[2]), int(words[4])
            password = password[:x] + password[x:y+1][::-1] + password[y+1:]
        elif "move" in val:
            # Move a letter
            x, y = int(words[2]), int(words[5])
            password.insert(y, password.pop(x))

        print(''.join(password))

