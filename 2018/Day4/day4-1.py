# Find the guard that is asleep the most and the minute where they are asleep the most

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["[1518-11-01 00:00] Guard #10 begins shift",
            "[1518-11-01 00:05] falls asleep",
            "[1518-11-01 00:25] wakes up",
            "[1518-11-01 00:30] falls asleep",
            "[1518-11-01 00:55] wakes up",
            "[1518-11-01 23:58] Guard #99 begins shift",
            "[1518-11-02 00:40] falls asleep",
            "[1518-11-02 00:50] wakes up",
            "[1518-11-03 00:05] Guard #10 begins shift",
            "[1518-11-03 00:24] falls asleep",
            "[1518-11-03 00:29] wakes up",
            "[1518-11-04 00:02] Guard #99 begins shift",
            "[1518-11-04 00:36] falls asleep",
            "[1518-11-04 00:46] wakes up",
            "[1518-11-05 00:03] Guard #99 begins shift",
            "[1518-11-05 00:45] falls asleep",
            "[1518-11-05 00:55] wakes up"]

if __name__ == '__main__':
    print("Starting Day4-1")
    # Read file into sorted list of values
    values = sorted(read_file('input.txt'))
    #values = sorted(test_data())

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
    for key,minutes in guards.items():
        print("Guard #{0}: [{1}]".format(key, ','.join(map(str, minutes))))
        total_minutes = 0
        highest = 0
        highest_index = 0
        for index in range(len(minutes)):
            total_minutes += minutes[index]
            if minutes[index] > highest:
                highest = minutes[index]
                highest_index = index

        if total_minutes > guard_total:
            guard_total = total_minutes
            sleepiest_guard = key
            sleepiest_minute = highest_index

    # Print out answer
    print("The sleepiest guard is #{0}, who slept the most at 00:{1} for a total of {2}".format(sleepiest_guard, str(sleepiest_minute), str(int(sleepiest_guard) * sleepiest_minute)))

