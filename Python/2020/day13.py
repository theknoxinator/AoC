# Determine the next bus you can take based on their schedules

def bus_schedule(values):
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

    return fastest_bus * shortest_time


def bus_schedule2(values):
    # First parse just the bus information this time around, store in a map by index and bus
    raw_busses = values[1].split(',')
    bus_map = dict()
    for i in range(len(raw_busses)):
        if raw_busses[i] == 'x':
            continue
        bus_map[i] = int(raw_busses[i])

    # Had to look this one up, turns out to be a Chinese remainder theorem problem, so implementing a version I got from
    # someone else
    timestamp = 0
    lcd = 1
    for offset, bus in bus_map.items():
        while (timestamp + offset) % bus != 0:
            timestamp += lcd
        lcd *= bus

    return timestamp


def part1(values):
    return bus_schedule(values)


def part2(values):
    return bus_schedule2(values)
