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


def test_data():
    # return [Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)]
    return [Moon(-8, -10, 0), Moon(5, 5, 10), Moon(2, -7, 3), Moon(9, -8, -3)]


def real_data():
    return [Moon(-13, 14, -7), Moon(-18, 9, 0), Moon(0, -3, -3), Moon(-15, 3, -13)]


def printMoons(moons):
    for moon in moons:
        print("pos=<x={0:3d}, y={1:3d}, z={2:3d}>, vel=<x={3:3d}, y={4:3d}, z={5:3d}>".format(moon.x, moon.y, moon.z,
                                                                                              moon.vx, moon.vy,
                                                                                              moon.vz))
    print()


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


print("Starting Day12-2")
# moons = test_data()
moons = real_data()

found_x = set()
repeat_x = None
found_y = set()
repeat_y = None
found_z = set()
repeat_z = None
steps = 0

while not (repeat_x and repeat_y and repeat_z):
    # printMoons(moons)

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
print("The first repeat is at {0!s} steps".format(full_repeat))
