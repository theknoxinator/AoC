# Determine the numbers that make 2020 when added together

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["1721", "979", "366", "299", "675", "1456"]


print("Starting Day1-2")
values = read_file("input.txt")
# values = test_data()

# Let's brute force this by just doing a simple double runner through the list (n^3)
answer = 0
for index in range(len(values)):
    for first_runner in range(index + 1, len(values)):
        for second_runner in range(first_runner + 1, len(values)):
            if int(values[index]) + int(values[first_runner]) + int(values[second_runner]) == 2020:
                answer = int(values[index]) * int(values[first_runner]) * int(values[second_runner])
                break
        if answer:
            break
    if answer:
        break

print("The answer is: {0!s}".format(answer))