# Determine the fewest number of movements of the elevator it takes to move all components to the top floor
# of the facility
from collections import deque
from itertools import combinations

if __name__ == "__main__":
    print("Starting Day 11-1")

    # Since this is a path finding algorithm, it makes the most sense to have a state object that shows
    # where things are for the current path, and a queue to hold the existing states
    class State:
        def __init__(self, steps=0, elevator=0, floor_1=[], floor_2=[], floor_3=[], floor_4=[]):
            self.floors = [floor_1, floor_2, floor_3, floor_4]
            self.elevator = elevator
            self.steps = steps

        def is_complete(self):
            return len(self.floors[0]) == 0 and len(self.floors[1]) == 0 and len(self.floors[2]) == 0

        def as_hash(self):
            return ','.join([str(floor) + '-' + str(sorted(floor)) for floor in self.floors])


    queue = deque()

    # Put the starting state on the queue
    # start_state = State(floor_1=["HM", "LM"], floor_2=["HG"], floor_3=["LG"])
    start_state = State(floor_1=["PmG", "PmM"], floor_2=["CoG", "CmG", "RuG", "PuG"], floor_3=["CoM", "CmM", "RuM", "PuM"])
    queue.append(start_state)

    minimum_steps = 100
    visited = {}
    while len(queue) > 0:
        current_state = queue.pop()

        # First we want to see if this path is already going beyond the shortest path found, if it is then
        # we just dump it and move on
        if current_state.steps >= minimum_steps:
            # print("Steps is over max of {0!s}".format(minimum_steps))
            continue

        # Debug print state
        for floor in reversed(range(len(current_state.floors))):
            if floor == current_state.elevator:
                print("E: ", end='')
            else:
                print("   ", end='')
            print(current_state.floors[floor])
        print("Number of steps so far: {0!s}".format(current_state.steps))

        # Next we want to check to see if the current state is the completed state, if so then set it as
        # the new minimum steps required and continue on
        if current_state.is_complete():
            if current_state.steps < minimum_steps:
                print("We found the end!")
                minimum_steps = current_state.steps
                continue

        # Next we want to check to see if the current state has happened before, then check count
        if current_state.as_hash() in visited:
            if current_state.steps < visited[current_state.as_hash()]:
                visited[current_state.as_hash()] = current_state.steps
            else:
                print("This state has already been seen before")
                continue
        else:
            visited[current_state.as_hash()] = current_state.steps

        # Next we want to check to see if the current state is valid or not, we do so by looking at each
        # floor for generator/chip mismatches
        invalid = False
        for floor in current_state.floors:
            # Chips are only safe if the matching generator is on the floor as well, or if there are no other
            # generators
            chips = []
            gens = []
            for object in floor:
                if object[-1:] == 'M':
                    chips.append(object)
                elif object[-1:] == 'G':
                    gens.append(object)

            for chip in chips:
                element = chip[:-1]
                if element + 'G' in gens:
                    # Matching generator is here, so we are good
                    continue
                elif len(gens) > 0:
                    # Matching generator is not there, but there are other generators, so we are invalid
                    invalid = True
                    break

        if invalid:
            # There was an invalid state, so we just drop this state and get the next one
            print("This state is invalid")
            continue

        # Okay, we have a valid state but it's not done yet, so let's calculate the different routes we can
        # take and add them to the queue

        # First, try to move each part individually
        current_floor = current_state.floors[current_state.elevator]
        for part in current_floor:
            if current_state.elevator < 3:
                # We can move up
                new_floors = [floor.copy() for floor in current_state.floors]
                new_floors[current_state.elevator].remove(part)
                new_floors[current_state.elevator + 1].append(part)
                new_state = State(current_state.steps + 1, current_state.elevator + 1, new_floors[0], new_floors[1],
                                  new_floors[2], new_floors[3])
                queue.append(new_state)
            if current_state.elevator > 0:
                # We can move down
                new_floors = [floor.copy() for floor in current_state.floors]
                new_floors[current_state.elevator].remove(part)
                new_floors[current_state.elevator - 1].append(part)
                new_state = State(current_state.steps + 1, current_state.elevator - 1, new_floors[0], new_floors[1],
                                  new_floors[2], new_floors[3])
                queue.append(new_state)

        # Second, try each pair of parts
        for pair in combinations(current_floor, 2):
            if current_state.elevator < 3:
                # We can move up
                new_floors = [floor.copy() for floor in current_state.floors]
                new_floors[current_state.elevator].remove(pair[0])
                new_floors[current_state.elevator].remove(pair[1])
                new_floors[current_state.elevator + 1].append(pair[0])
                new_floors[current_state.elevator + 1].append(pair[1])
                new_state = State(current_state.steps + 1, current_state.elevator + 1, new_floors[0], new_floors[1],
                                  new_floors[2], new_floors[3])
                queue.append(new_state)
            if current_state.elevator > 0:
                # We can move down
                new_floors = [floor.copy() for floor in current_state.floors]
                new_floors[current_state.elevator].remove(pair[0])
                new_floors[current_state.elevator].remove(pair[1])
                new_floors[current_state.elevator - 1].append(pair[0])
                new_floors[current_state.elevator - 1].append(pair[1])
                new_state = State(current_state.steps + 1, current_state.elevator - 1, new_floors[0], new_floors[1],
                                  new_floors[2], new_floors[3])
                queue.append(new_state)

    # Print out answer
    print("The number of visited states is: {0!s}".format(len(visited)))
    print("The minimum number of steps is: {0!s}".format(minimum_steps))
