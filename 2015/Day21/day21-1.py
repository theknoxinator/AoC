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

if __name__ == '__main__':
    print("Starting Day21-1")

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

    # Debug print out all options
    #for option in full_options:
    #    print("{0}, {1}, {2}, {3}".format(option[0].name, option[1].name, option[2][0].name, option[2][1].name))

    # Make some helper functions for determining player stats
    def get_player(option):
        total_damage = option[0].damage + option[1].damage + option[2][0].damage + option[2][1].damage
        total_armor = option[0].armor + option[1].armor + option[2][0].armor + option[2][1].armor
        return Character("Player", 100, total_damage, total_armor)

    # Now that we have all the possible combinations, we simulate each fight and determine which ones win
    winning_options = []
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
            #print("Boss takes {0!s} damage to go to {1!s} HP".format(damage_to_boss, boss.hit_points))
            if boss.is_dead():
                # Player wins, so add to winning options
                print("Player wins with combination: {0}, {1}, {2}, {3}"
                      .format(option[0].name, option[1].name, option[2][0].name, option[2][1].name))
                winning_options.append(option)
                break

            # Boss goes next
            damage_to_player = boss.damage - player.armor
            if damage_to_player < 1:
                damage_to_player = 1
            player.take_damage(damage_to_player)
            #print("Player takes {0!s} damage to go to {1!s} HP".format(damage_to_player, player.hit_points))
            if player.is_dead():
                # Player loses, so stop simulation and move on
                break

    # Now figure out which combination costs the least
    smallest_cost = 99999
    smallest_cost_option = None
    for option in winning_options:
        cost = option[0].cost + option[1].cost + option[2][0].cost + option[2][1].cost
        if cost < smallest_cost:
            smallest_cost = cost
            smallest_cost_option = option

    # Print out answer
    print("The cheapest winning combination is {0}, {1}, {2}, {3} which costs: {4}"
          .format(smallest_cost_option[0].name, smallest_cost_option[1].name, smallest_cost_option[2][0].name,
                  smallest_cost_option[2][1].name, smallest_cost))
