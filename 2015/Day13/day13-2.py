# Find the maximum amount of happiness for the table seating arrangement, including yourself who
# has no happiness value

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["Alice would gain 54 happiness units by sitting next to Bob.",
            "Alice would lose 79 happiness units by sitting next to Carol.",
            "Alice would lose 2 happiness units by sitting next to David.",
            "Bob would gain 83 happiness units by sitting next to Alice.",
            "Bob would lose 7 happiness units by sitting next to Carol.",
            "Bob would lose 63 happiness units by sitting next to David.",
            "Carol would lose 62 happiness units by sitting next to Alice.",
            "Carol would gain 60 happiness units by sitting next to Bob.",
            "Carol would gain 55 happiness units by sitting next to David.",
            "David would gain 46 happiness units by sitting next to Alice.",
            "David would lose 7 happiness units by sitting next to Bob.",
            "David would gain 41 happiness units by sitting next to Carol."]

if __name__ == '__main__':
    print("Starting Day13-2")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # Compile data into a dictionary for each directional pair
    people = []
    happiness = {}
    for val in values:
        items = val.replace('.','').split()
        person = items[0]
        if person not in people:
            people.append(person)
        neighbor = items[10]
        units = int(items[3])
        if "lose" == items[2]:
            units = -units

        happiness[(person,neighbor)] = units

    # Add yourself in with happiness values of 0 for each relationship
    for person in people:
        happiness[(person,"You")] = 0
        happiness[("You",person)] = 0
    people.append("You")

    # Print out the happiness dictionary
    for key,value in happiness.items():
        print("{0}: {1}".format('->'.join(key), str(value)))

    # Compile all the different possible table permutations
    arrangements = []
    for person in people:
        if len(arrangements) == 0:
            arrangements.append([person])
            continue
        new_arrangements = []
        for arrangement in arrangements:
            for index in range(len(arrangement)+1):
                new_arrangement = arrangement.copy()
                new_arrangement.insert(index, person)
                new_arrangements.append(new_arrangement)

        arrangements = new_arrangements

    # Print out arrangements
    for arrangement in arrangements:
        print(" ".join(arrangement))
    print("Total number of arrangements: {0}".format(str(len(arrangements))))

    highest_happiness = 0
    highest_arr = []
    for arr in arrangements:
        total = 0
        for index in range(len(arr)):
            next = (index + 1) % len(arr)
            total += happiness[(arr[index], arr[next])]
            total += happiness[(arr[next], arr[index])]

        if total > highest_happiness:
            highest_happiness = total
            highest_arr = arr

    print("The highest happiness is {0} for arrangement: {1}".format(str(highest_happiness), " ".join(highest_arr)))
