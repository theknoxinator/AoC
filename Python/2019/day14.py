# Part 1: Given a set of conversion rules, determine how much ore is required to create one fuel
# Part 2: Using the same algorithm, determine how much fuel can be created with 1 trillion units of ore
from collections import defaultdict, deque
import math


def calculate_ore(values, use_part2=False, starting_fuel=1):
    # Read the values into rules that are read in reverse so that the output is the key and the value is the list of
    # requirements
    reactions = dict()
    for val in values:
        materials, crafted = val.split('=>')
        crafted_amount, crafted_chem = crafted.split()
        reactions[crafted_chem] = {'produces': int(crafted_amount)}
        mats = []
        for mat in materials.split(','):
            mats.append((mat.split()[1], int(mat.split()[0])))
        reactions[crafted_chem]['mats'] = mats

    # To do this we will set up a queue to keep track of what pre-crafts need to be done to get to the goal of 1 fuel
    # Unless most uses of the queue we've done, we want it to be more of a stack where new mats get pushed to the front
    # so that whatever is currently pending will resolve once the requirements are met.
    current_materials = defaultdict(int)
    queue = deque()
    consumed_ore = 0
    fuel_generated = 0
    queue.appendleft(('FUEL', starting_fuel))
    while queue:
        to_craft, required_amount = queue.popleft()
        required_mats = reactions[to_craft]['mats']
        per_craft = reactions[to_craft]['produces']
        multiplier = math.ceil(required_amount / per_craft)
        has_all_mats = True
        for mat_name, mat_amount in required_mats:
            if mat_name == 'ORE':
                # No need to check this, it's infinite
                continue
            if current_materials[mat_name] < mat_amount * multiplier:
                # We don't have enough of this material, so push craft back on and add this as a new craft to do
                queue.appendleft((to_craft, required_amount))
                queue.appendleft((mat_name, mat_amount * multiplier - current_materials[mat_name]))
                has_all_mats = False
                break
        if not has_all_mats:
            continue

        # If we get here, then we have enough mats to make the craft/reaction
        for mat_name, mat_amount in required_mats:
            if mat_name == 'ORE':
                # Ore is the special case where we just add up how much we use since it's an infinite resource
                consumed_ore += mat_amount * multiplier
            else:
                current_materials[mat_name] -= mat_amount * multiplier
        current_materials[to_craft] += per_craft * multiplier

        if use_part2 and len(queue) == 0:
            # For part 2 we want to keep creating fuel until consumed ore is over 1 trillion, so check for that
            # If the ore is still under 1 trillion, add another fuel on
            if consumed_ore >= 1_000_000_000_000:
                # We have crossed the threshold, just do nothing, we don't tick up fuel because we went over the limit
                continue
            else:
                fuel_generated += required_amount if to_craft == 'FUEL' else 1
                queue.appendleft(('FUEL', 1))

    # For part 1, just return the amount of ore that was used along the way
    # For part 2, also return the amount of fuel generated (would just be 1 for part 1)
    return consumed_ore, fuel_generated


def part1(values):
    return calculate_ore(values)[0]


def part2(values):
    # As a way to speed up the process, we want to start with a target that's close to the end so that we get the bulk
    # done in the first pass
    consumed_ore_single = calculate_ore(values)[0]
    target_fuel = 1_000_000_000_000 // consumed_ore_single
    return calculate_ore(values, True, target_fuel)[1]
