# Create a bitwise logic circuit and determine the resulting value of a wire after all instructions
# have been completed
from collections import deque

def read_file(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line)

    return values

def test_data():
    return ["123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i"]

if __name__ == '__main__':
    print("Starting Day7-1")
    # Read file into list of values
    values = read_file('input.txt')
    #values = test_data()

    # To start, take all instructions and put them on a queue so that they can be read over and over
    queue = deque()
    for val in values:
        queue.append(val)

    # Now read each instruction, check to see if it can be completed, re-enqueue if not
    wires = {}
    count = 0
    def get_value(key):
        if key.isdigit():
            return int(key)
        else:
            return wires.get(key)

    while len(queue) > 0:
        if count % 50 == 0:
            print("There are currently {0} instructions in the queue".format(str(len(queue))))
        count += 1

        instruction = queue.popleft()
        if "AND" in instruction:
            # Bitwise and the first and second values
            parts = instruction.split()
            first = get_value(parts[0])
            second = get_value(parts[2])
            if first is None or second is None:
                queue.append(instruction)
            else:
                wires[parts[4]] = first & second
        elif "OR" in instruction:
            # Bitwise or the first and second values
            parts = instruction.split()
            first = get_value(parts[0])
            second = get_value(parts[2])
            if first is None or second is None:
                queue.append(instruction)
            else:
                wires[parts[4]] = first | second
        elif "LSHIFT" in instruction:
            # Shift first value to the left
            parts = instruction.split()
            first = get_value(parts[0])
            if first is None:
                queue.append(instruction)
            else:
                wires[parts[4]] = first << int(parts[2])
        elif "RSHIFT" in instruction:
            # Shift first value to the right
            parts = instruction.split()
            first = get_value(parts[0])
            if first is None:
                queue.append(instruction)
            else:
                wires[parts[4]] = first >> int(parts[2])
        elif "NOT" in instruction:
            # Find two's compliment of the first value
            parts = instruction.split()
            first = get_value(parts[1])
            if first is None:
                queue.append(instruction)
            else:
                temp = ~first
                if temp < 0:
                    temp += 65536
                wires[parts[3]] = temp
        else:
            # Simple value is being passed in
            parts = instruction.split()
            first = get_value(parts[0])
            if first is None:
                queue.append(instruction)
            else:
                wires[parts[2]] = first

    # Print out the map
    for key,value in wires.items():
        print("Wire: {0}, Value: {1}".format(key, str(value)))

    # Print out answer
    print("The value of wire a is: {0}".format(wires.get('a')))