# Determine the smallest amount of gold the player can spend and still beat the boss assuming each takes
# turns and does consistent damage each round

'''
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''
class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

WEAPONS = [Item("Dagger", 8, 4, 0),
           Item("Shortsword", 10, 5, 0),
           Item("Warhammer", 25, 6, 0),
           Item("Longsword", 40, 7, 0),
           Item("Greataxe", 74, 8, 0)]

ARMOR = [Item("No Armor", 0, 0, 0),
         Item("Leather", 13, 0, 1),
         Item("Chainmail", 31, 0, 2),
         Item("Splintmail", 53, 0, 3),
         Item("Bandedmail", 75, 0, 4),
         Item("Platemail", 102, 0, 5)]

RINGS = [Item("No Ring", 0, 0, 0),
         Item("Damage +1", 25, 1, 0),
         Item("Damage +2", 50, 2, 0),
         Item("Damage +3", 100, 3, 0),
         Item("Defense +1", 20, 0, 1),
         Item("Defense +2", 40, 0, 2),
         Item("Defense +3", 80, 0, 3)]

class Character:
    def __init__(self, name, hit_points, damage, armor):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor

    def take_damage(self, damage):
        self.hit_points -= damage

    def is_dead(self):
        return self.hit_points <= 0


def do_fight():
    # First, we need to determine all possible combinations of equipment for the player that we can simulate
    weapon_options = WEAPONS
    armor_options = ARMOR
    ring_options = []
    for first in range(len(RINGS)):
        for second in range(first, len(RINGS)):
            if first == second and first > 0:
                # Cannot get two of the same
                continue
            ring_options.append((RINGS[first], RINGS[second]))

    full_options = []
    for weapon in weapon_options:
        for armor in armor_options:
            for ring in ring_options:
                full_options.append((weapon, armor, ring))

    # Make some helper functions for determining player stats
    def get_player(option):
        total_damage = option[0].damage + option[1].damage + option[2][0].damage + option[2][1].damage
        total_armor = option[0].armor + option[1].armor + option[2][0].armor + option[2][1].armor
        return Character("Player", 100, total_damage, total_armor)

    # Now that we have all the possible combinations, we simulate each fight and determine which ones win
    winning_options = []
    losing_options = []
    for option in full_options:
        # Get our player and boss
        player = get_player(option)
        boss = Character("Boss", 104, 8, 1)

        # Run the simulation
        while True:
            # Player goes first
            damage_to_boss = player.damage - boss.armor
            if damage_to_boss < 1:
                damage_to_boss = 1
            boss.take_damage(damage_to_boss)
            if boss.is_dead():
                # Player wins, so add to winning options
                winning_options.append(option)
                break

            # Boss goes next
            damage_to_player = boss.damage - player.armor
            if damage_to_player < 1:
                damage_to_player = 1
            player.take_damage(damage_to_player)
            if player.is_dead():
                # Player loses, so add to losing options
                losing_options.append(option)
                break

    # Now figure out which combination costs the least for winning
    smallest_cost = 99999
    for option in winning_options:
        smallest_cost = min(smallest_cost, option[0].cost + option[1].cost + option[2][0].cost + option[2][1].cost)

    # Also figure out which combination costs the most for losing
    highest_cost = 0
    for option in losing_options:
        highest_cost = max(highest_cost, option[0].cost + option[1].cost + option[2][0].cost + option[2][1].cost)

    return smallest_cost, highest_cost


def part1(_values):
    return do_fight()[0]


def part2(_values):
    return do_fight()[1]
