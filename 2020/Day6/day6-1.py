# Parse bulk file of customs answer and determine how many questions were answered yes

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b"]


print("Starting Day6-1")
values = read_file("input.txt")
# values = test_data()

# Just like with the passports, we parse each group in place and add their question total to a list that we will sum
# at the end
values.append("")
groups = []
current_group = set()
for line in values:
    if len(line) < 1:
        # We have reached an empty line, so compute current group
        print(current_group)
        groups.append(len(current_group))
        current_group = set()
    else:
        # To make it easy we are using a set of chars, so just add each char to the set as we go and get the length
        for char in line:
            current_group.add(char)

print("Lengths of groups is:", groups);
print("The sum of groups is: {0!s}".format(sum(groups)))
