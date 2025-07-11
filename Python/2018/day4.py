# Find the guard that is asleep the most and the minute where they are asleep the most

def find_guard(values, use_part2=False):
    # Create a dictionary to hold the sleeping minutes for each guard
    guards = {}
    index = 0
    current_guard = ""
    while index < len(values):
        note = values[index].split()
        if "Guard" in note:
            current_guard = note[3].replace('#', '')
            if current_guard not in guards:
                guards[current_guard] = [0]*60
        elif "asleep" in note:
            start_minute = int(note[1][3:5])
            end_minute = 60
            if "wakes" in values[index+1]:
                end_minute = int(values[index+1].split()[1][3:5])
            for minute in range(start_minute, end_minute):
                guards[current_guard][minute] += 1

        index += 1

    sleepiest_guard = ""
    guard_total = 0
    sleepiest_minute = 0
    highest_minute = 0
    for key,minutes in guards.items():
        total_minutes = 0
        highest = 0
        highest_index = 0
        for index in range(len(minutes)):
            total_minutes += minutes[index]
            if minutes[index] > highest:
                highest = minutes[index]
                highest_index = index

        if not use_part2:
            if total_minutes > guard_total:
                guard_total = total_minutes
                sleepiest_guard = key
                sleepiest_minute = highest_index
        else:
            if highest > highest_minute:
                highest_minute = highest
                sleepiest_guard = key
                sleepiest_minute = highest_index

    # Print out answer
    return int(sleepiest_guard) * sleepiest_minute


def part1(values):
    return find_guard(values)


def part2(values):
    return find_guard(values, True)
