# Parse bulk file of customs answer and determine how many questions were answered yes by everyone in group

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


print("Starting Day6-2")
values = read_file("input.txt")
# values = test_data()

# Just like with the passports, we parse each group in place and add their question total to a list that we will sum
# at the end
values.append("")
groups = []
current_group = None
for line in values:
    if len(line) < 1:
        # We have reached an empty line, so compute current group
        print(current_group)
        groups.append(len(current_group))
        current_group = None
    else:
        # This time around we are finding the union of each set of questions
        if current_group is None:
            current_group = set(line)
        else:
            current_group = current_group & set(line)

print("Lengths of groups is:", groups)
print("The sum of groups is: {0!s}".format(sum(groups)))
