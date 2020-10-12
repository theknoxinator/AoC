# Get total energy of a set of moons


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


print("Starting Day12")
# moons = test_data()
moons = real_data()

printMoons(moons)

for i in range(1000):

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

    if i % 10 == 9:
        print("After {!s} steps:".format(i + 1))
        printMoons(moons)

# Now calculate the energy of the final state
total_energy = 0
for moon in moons:
    potential = abs(moon.x) + abs(moon.y) + abs(moon.z)
    kinetic = abs(moon.vx) + abs(moon.vy) + abs(moon.vz)
    total_energy += potential * kinetic

print("The total energy of the moons is: {0:d}".format(total_energy))
