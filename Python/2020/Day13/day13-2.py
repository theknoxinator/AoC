# Determine the first time all the busses line up in subsequent departures

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


def test_data():
    # return ["939", "7,13,x,x,59,x,31,19"]
    # return ["1", "17,x,13,19"]
    # return ["1", "67,7,59,61"]
    # return ["1", "67,x,7,59,61"]
    # return ["1", "67,7,x,59,61"]
    return ["1", "1789,37,47,1889"]


print("Starting Day13-2")
values = read_file("input.txt")
# values = test_data()

# First parse just the bus information this time around, store in a map by index and bus
raw_busses = values[1].split(',')
bus_map = dict()
for i in range(len(raw_busses)):
    if raw_busses[i] == 'x':
        continue
    bus_map[i] = int(raw_busses[i])

print(bus_map)

# Had to look this one up, turns out to be a Chinese remainder theorem problem, so implementing a version I got from
# someone else
timestamp = 0
lcd = 1
for offset, bus in bus_map.items():
    while (timestamp + offset) % bus != 0:
        timestamp += lcd
    lcd *= bus

print("The first timestamp that fits the staggered schedule is: {0!s}".format(timestamp))
