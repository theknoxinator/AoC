# Find the maximum amount of happiness for the table seating arrangement

def find_happiness(values, insert_self=False):
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

    if insert_self:
        # Add yourself in with happiness values of 0 for each relationship
        for person in people:
            happiness[(person, "You")] = 0
            happiness[("You", person)] = 0
        people.append("You")

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

    highest_happiness = 0
    for arr in arrangements:
        total = 0
        for index in range(len(arr)):
            next = (index + 1) % len(arr)
            total += happiness[(arr[index], arr[next])]
            total += happiness[(arr[next], arr[index])]

        if total > highest_happiness:
            highest_happiness = total

    return highest_happiness


def part1(values):
    return find_happiness(values)


def part2(values):
    # For this part, we need to insert ourselves, who has a happiness score of 0 next to anyone
    return find_happiness(values, True)
