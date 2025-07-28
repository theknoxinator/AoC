# Part 1: Given a set of particles moving and accelerating in a direction, determine which one will stay closest to center
# Part 2: Using same particles, determine how many particles will remain after collisions take certain particles out
import re


class Particle:

    def __init__(self, line):
        self.pos = self._parse_pos(line)
        self.vel = self._parse_vel(line)
        self.acl = self._parse_acl(line)

    def _parse_pos(self, line):
        m = re.search(r'p=<([0-9\-,]+)>', line)
        return list(map(int, m.group(1).split(',')))

    def _parse_vel(self, line):
        m = re.search(r'v=<([0-9\-,]+)>', line)
        return list(map(int, m.group(1).split(',')))

    def _parse_acl(self, line):
        m = re.search(r'a=<([0-9\-,]+)>', line)
        return list(map(int, m.group(1).split(',')))

    def tick(self):
        # Perform one tick of movement
        self.vel[0] += self.acl[0]
        self.vel[1] += self.acl[1]
        self.vel[2] += self.acl[2]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]

    def get_pos(self):
        return tuple(self.pos)


def get_closest(values):
    particles = [Particle(val) for val in values]

    # Position and velocity is a bit misleading here, the only thing that matters here is the overall acceleration since
    # over the long term compounding will make the smallest acceleration the closest
    closest_particle = None
    for i, p in enumerate(particles):
        acceleration = abs(p.acl[0]) + abs(p.acl[1]) + abs(p.acl[2])
        if closest_particle is None or acceleration < closest_particle[1]:
            closest_particle = (i, acceleration)

    # Return the particle with the smallest acceleration
    return closest_particle[0]


def handle_collisions(values):
    particles = [Particle(val) for val in values]

    # Tick a certain number of times, and remove any particles that happen to collide after each tick
    for _ in range(1000):
        collisions = set()
        all_pos = dict()
        for i, p in enumerate(particles):
            p.tick()
            new_pos = p.get_pos()
            if new_pos in all_pos:
                collisions.add(new_pos)
                all_pos[new_pos].append(i)
            else:
                all_pos[new_pos] = [i]
        to_remove = []
        for c in collisions:
            to_remove.extend(all_pos[c])
        for i in sorted(to_remove, reverse=True):
            particles.pop(i)

    return len(particles)


def part1(values):
    return get_closest(values)


def part2(values):
    return handle_collisions(values)
