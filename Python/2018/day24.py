# Part 1: Given two armies of units attacking each other, determine how many units remain in the winning army
# Part 2: Do the same battle but add boosts every time to figure out how much boost is needed for immune system to win
from collections import defaultdict
import re


# Create a class that represents a specific group of the army (doesn't technically fit the definition of squadron, just
# wanted something more army sounding than "group")
class Squadron:
    def __init__(self, line):
        self.unit_count = 0
        self.unit_hp = 0
        self.vulns = defaultdict(set)
        self.power = 0
        self.attack_type = None
        self.initiative = 0
        self._parse_line(line)

    def _parse_line(self, line):
        m = re.search(r'([0-9]+) units each with ([0-9]+) hit points (.*)with an attack that does ([0-9]+) ([a-z]+) damage at initiative ([0-9]+)', line)
        self.unit_count = int(m.group(1))
        self.unit_hp = int(m.group(2))
        self._parse_vulns(m.group(3))
        self.power = int(m.group(4))
        self.attack_type = m.group(5)
        self.initiative = int(m.group(6))

    def _parse_vulns(self, vulns_list):
        if '(' not in vulns_list:
            return
        vulns_list = re.sub(r'[();,]', '', vulns_list).split()
        is_weak = False
        for val in vulns_list:
            if val == 'weak':
                is_weak = True
            elif val == 'immune':
                is_weak = False
            elif val in ['bludgeoning', 'cold', 'fire', 'radiation', 'slashing']:
                if is_weak:
                    self.vulns['weak'].add(val)
                else:
                    self.vulns['immune'].add(val)

    def add_boost(self, boost):
        self.power += boost

    def get_effective_power(self):
        return self.unit_count * self.power, self.attack_type

    def get_potential_damage(self, enemy_power, enemy_attack_type):
        if enemy_attack_type in self.vulns['immune']:
            return 0
        elif enemy_attack_type in self.vulns['weak']:
            return enemy_power * 2
        else:
            return enemy_power

    def take_damage(self, enemy_power, enemy_attack_type):
        if enemy_attack_type in self.vulns['immune']:
            # We are immune, take no damage
            return
        elif enemy_attack_type in self.vulns['weak']:
            # We are weak, take double damage
            enemy_power *= 2

        killed_units = enemy_power // self.unit_hp
        self.unit_count = max(0, self.unit_count - killed_units)


def army_fight(values, boost=0):
    # Parse the values to get the armies setup, the ID of each army (for purposes of recording turn order) is its init
    immune_system = dict()
    infection = dict()
    parsing_group = 0
    for val in values:
        if 'Immune System' in val:
            parsing_group = 0
            continue
        elif 'Infection' in val:
            parsing_group = 1
            continue
        elif not val:
            continue
        else:
            squad = Squadron(val)
            if parsing_group == 0:
                squad.add_boost(boost)
                immune_system[squad.initiative] = squad
            else:
                infection[squad.initiative] = squad


    # The fight lasts as long as both armies still have squads
    previous_unit_counts = (0, 0)
    while immune_system and infection:
        # Put all the squads into a common list to determine turn order, first by effective power/init on tie
        # Sort by the initiative first since multi-sort needs to be done in reverse priority order
        turn_order = list(immune_system.values()) + list(infection.values())
        turn_order = sorted(turn_order, key=lambda sq: (-sq.get_effective_power()[0], -sq.initiative))

        # Now determine the attack selections, where each squad (in turn order) chooses the enemy squad it will do the
        # most damage to. Once a squad is selected to be targeted, they cannot be targeted again.
        attack_selection = dict()
        for squad in turn_order:
            id = squad.initiative
            if id in immune_system:
                potential_targets = set(infection.keys()) - set(attack_selection.values())
            else:
                potential_targets = set(immune_system.keys()) - set(attack_selection.values())
            highest_potential = (0, 0, 0)
            for t_id in potential_targets:
                target = immune_system[t_id] if t_id in immune_system else infection[t_id]
                target_power = target.get_effective_power()[0]
                effective_power, attack_type = squad.get_effective_power()
                potential = target.get_potential_damage(effective_power, attack_type)
                if potential <= 0:
                    continue
                if potential > highest_potential[0]:
                    highest_potential = (potential, target.initiative, target_power)
                elif potential == highest_potential[0]:
                    if target_power > highest_potential[2]:
                        highest_potential = (potential, target.initiative, target_power)
                    elif target_power == highest_potential[2]:
                        if target.initiative > highest_potential[1]:
                            highest_potential = (potential, target.initiative, target_power)
            attack_selection[id] = highest_potential[1]

        # After selections are done, it is time to attack, and the attacks happen in initiative order regardless of
        # power or side, so re-sort the turn order
        turn_order = sorted(turn_order, key=lambda sq: -sq.initiative)
        for squad in turn_order:
            id = squad.initiative
            if id not in immune_system and id not in infection:
                # Squad was already killed before their turn, so skip
                continue
            t_id = attack_selection[id]
            if t_id == 0:
                # Nothing to attack, so skip
                continue
            target = immune_system[t_id] if t_id in immune_system else infection[t_id]
            effective_power, attack_type = squad.get_effective_power()
            target.take_damage(effective_power, attack_type)
            if target.unit_count == 0:
                if t_id in immune_system:
                    del immune_system[t_id]
                else:
                    del infection[t_id]

        new_unit_counts = (sum(x.unit_count for x in immune_system.values()), sum(x.unit_count for x in infection.values()))
        if new_unit_counts == previous_unit_counts:
            # We've hit a stalemate, just exit from here
            break
        previous_unit_counts = new_unit_counts

    return sum(x.unit_count for x in immune_system.values()), sum(x.unit_count for x in infection.values())


def find_boost(values):
    boost = 1
    while True:
        immune_units, infection_units = army_fight(values, boost)
        if immune_units > 0 >= infection_units:
            return immune_units
        boost += 1


def part1(values):
    return army_fight(values)[1]


def part2(values):
    return find_boost(values)
