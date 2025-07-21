# Get total energy of a set of moons
from math import gcd


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0


def moon_energy(values):
    steps = int(values.pop(0))
    moons = []
    for val in values:
        coords = list(map(int, val.split(',')))
        moons.append(Moon(coords[0], coords[1], coords[2]))

    for i in range(steps):
        # Calculate velocities based on gravity of other moons
        for moon in moons:
            for other in moons:
                if moon == other:
                    continue

                if other.x > moon.x:
                    moon.vx += 1
                elif other.x < moon.x:
                    moon.vx -= 1

                if other.y > moon.y:
                    moon.vy += 1
                elif other.y < moon.y:
                    moon.vy -= 1

                if other.z > moon.z:
                    moon.vz += 1
                elif other.z < moon.z:
                    moon.vz -= 1

        # Now apply velocity to positions
        for moon in moons:
            moon.x += moon.vx
            moon.y += moon.vy
            moon.z += moon.vz

    # Now calculate the energy of the final state
    total_energy = 0
    for moon in moons:
        potential = abs(moon.x) + abs(moon.y) + abs(moon.z)
        kinetic = abs(moon.vx) + abs(moon.vy) + abs(moon.vz)
        total_energy += potential * kinetic

    print("The total energy of the moons is: {0:d}".format(total_energy))
    return total_energy


def repeat_steps(values):

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)

    _ = int(values.pop(0))
    moons = []
    for val in values:
        coords = list(map(int, val.split(',')))
        moons.append(Moon(coords[0], coords[1], coords[2]))

    found_x = set()
    repeat_x = None
    found_y = set()
    repeat_y = None
    found_z = set()
    repeat_z = None
    steps = 0

    while not (repeat_x and repeat_y and repeat_z):
        if not repeat_x:
            state_x = ''.join([str(value) for moon in moons for value in (moon.x, moon.vx)])
            if state_x in found_x:
                repeat_x = steps
            else:
                found_x.add(state_x)

        if not repeat_y:
            state_y = ''.join([str(value) for moon in moons for value in (moon.y, moon.vy)])
            if state_y in found_y:
                repeat_y = steps
            else:
                found_y.add(state_y)

        if not repeat_z:
            state_z = ''.join([str(value) for moon in moons for value in (moon.z, moon.vz)])
            if state_z in found_z:
                repeat_z = steps
            else:
                found_z.add(state_z)

        # Calculate velocities based on gravity of other moons
        for moon in moons:
            for other in moons:
                if moon == other:
                    continue

                if other.x > moon.x:
                    moon.vx += 1
                elif other.x < moon.x:
                    moon.vx -= 1

                if other.y > moon.y:
                    moon.vy += 1
                elif other.y < moon.y:
                    moon.vy -= 1

                if other.z > moon.z:
                    moon.vz += 1
                elif other.z < moon.z:
                    moon.vz -= 1

        # Now apply velocity to positions
        for moon in moons:
            moon.x += moon.vx
            moon.y += moon.vy
            moon.z += moon.vz

        steps += 1

    full_repeat = lcm(repeat_x, lcm(repeat_y, repeat_z))
    return full_repeat


def part1(values):
    return moon_energy(values)


def part2(values):
    return repeat_steps(values)
