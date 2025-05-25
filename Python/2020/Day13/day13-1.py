# Determine the next bus you can take based on their schedules

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    return ["939", "7,13,x,x,59,x,31,19"]


print("Starting Day13-1")
values = read_file("input.txt")
# values = test_data()

# First parse the input to get the earliest timestamp we can do and the list of busses
start_time = int(values[0])
busses = []
for bus in values[1].split(','):
    if bus != 'x':
        busses.append(int(bus))

# Now we go through each bus schedule, determine the next departure for each bus compared to the start time
next_busses = []
for bus in busses:
    next_busses.append((int(start_time / bus) + 1) * bus)

# Figure out which bus comes soonest
shortest_time = 9999999
fastest_bus = 0
for index in range(len(next_busses)):
    wait_time = next_busses[index] - start_time
    if wait_time < shortest_time:
        fastest_bus = busses[index]
        shortest_time = wait_time

print("The fastest bus is: {0!s} which is {1!s} minutes away".format(fastest_bus, shortest_time))
print("The bus ID times minutes is: {0!s}".format(fastest_bus * shortest_time))
