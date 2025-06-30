# Determine the smallest amount of mana the player can spend and still beat the boss assuming each takes
# turns and spell effects trigger each turn
from collections import deque

'''
Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
'''
SPELLS = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229
}

'''
Game State must contain:
- The history of spells cast by the player
- The amount of mana used so far
- The current HP for player and boss
- The current mana for player
- The remaining turns for each active spell
- The next spell to be cast by the player
'''
class GameState:
    def __init__(self, player_hp, boss_hp, player_mana, next_spell="", spell_history=[], mana_spent=0, effect_turns={}):
        self.player_hp = player_hp
        self.boss_hp = boss_hp
        self.player_mana = player_mana
        self.next_spell = next_spell
        self.spell_history = spell_history
        self.mana_spent = mana_spent
        self.effect_turns = effect_turns

    def copy(self):
        return GameState(self.player_hp, self.boss_hp, self.player_mana, self.next_spell, self.spell_history.copy(),
                         self.mana_spent, self.effect_turns.copy())


def do_fight(hard_mode=False):
    # First, set up a queue and the initial starting states
    game_states = deque()
    start_state = GameState(50, 55, 500)
    for spell in SPELLS.keys():
        new_state = start_state.copy()
        new_state.next_spell = spell
        game_states.append(new_state)

    # Create some helpers for common things
    def reduce_effect(current_state, effect_name):
        current_state.effect_turns[effect_name] -= 1
        if current_state.effect_turns[effect_name] <= 0:
            del current_state.effect_turns[effect_name]

    # Now we have a loop that pulls each game state, executes its spell and adds new future states to the
    # queue if applicable
    smallest_mana = 99999
    while len(game_states) > 0:
        current_state = game_states.pop()

        # If current state is already over smallest, just ignore and move on
        if current_state.mana_spent > smallest_mana or len(current_state.spell_history) >= 15:
            continue

        # Execute player turn first
        if hard_mode:
            # Player loses 1 HP before any other effects if hard mode
            current_state.player_hp -= 1
            if current_state.player_hp <= 0:
                continue

        # Effects happen first
        if "Shield" in current_state.effect_turns:
            # On player turn, shield does nothing, so just decrease turns
            reduce_effect(current_state, "Shield")
        if "Poison" in current_state.effect_turns:
            # On player turn, poison will still hurt boss, so do so and decrease turns
            current_state.boss_hp -= 3
            reduce_effect(current_state, "Poison")
        if "Recharge" in current_state.effect_turns:
            # On player turn, recharge will increase mana, so do so and decrease turns
            current_state.player_mana += 101
            reduce_effect(current_state, "Recharge")

        # Check to see if player has won
        if current_state.boss_hp <= 0:
            if current_state.mana_spent < smallest_mana:
                smallest_mana = current_state.mana_spent
            continue

        # Now cast the spell if possible and apply it
        spell = current_state.next_spell
        if current_state.player_mana < SPELLS[spell] or spell in current_state.effect_turns:
            # Cannot cast spell, invalid state so ignore and move on
            continue
        if spell == "Magic Missile":
             # Magic missile just does instant damage
             current_state.boss_hp -= 4
        elif spell == "Drain":
            # Drain takes damage from boss and adds to player HP
            current_state.boss_hp -= 2
            current_state.player_hp += 2
        elif spell == "Shield":
            # Apply new shield effect
            current_state.effect_turns[spell] = 6
        elif spell == "Poison":
            # Apply poison to boss
            current_state.effect_turns[spell] = 6
        elif spell == "Recharge":
            # Apply recharge to player
            current_state.effect_turns[spell] = 5

        # For all spells, reduce the player mana and add to total spent
        current_state.player_mana -= SPELLS[spell]
        current_state.mana_spent += SPELLS[spell]
        current_state.spell_history.append(spell)

        # Check to see if player has won
        if current_state.boss_hp <= 0:
            if current_state.mana_spent < smallest_mana:
                smallest_mana = current_state.mana_spent
                smallest_state = current_state
            continue

        # Execute boss turn second
        # Effects happen first
        if "Shield" in current_state.effect_turns:
            # On player turn, shield does nothing, so just decrease turns
            reduce_effect(current_state, "Shield")
        if "Poison" in current_state.effect_turns:
            # On player turn, poison will still hurt boss, so do so and decrease turns
            current_state.boss_hp -= 3
            reduce_effect(current_state, "Poison")
        if "Recharge" in current_state.effect_turns:
            # On player turn, recharge will increase mana, so do so and decrease turns
            current_state.player_mana += 101
            reduce_effect(current_state, "Recharge")

        # Check to see if player has won
        if current_state.boss_hp <= 0:
            if current_state.mana_spent < smallest_mana:
                smallest_mana = current_state.mana_spent
                smallest_state = current_state
            continue

        # Now have boss actually deal damage to the player
        boss_damage = 8
        if "Shield" in current_state.effect_turns:
            # Shield is currently active, so reduce damage
            boss_damage -= 7
        current_state.player_hp -= boss_damage

        # Check to see if player has lost
        if current_state.player_hp <= 0:
            # Player lost, so not a valid run, just move on
            continue

        # At this point, the player has not won or lost, so create new states for each possible next spell
        try:
            for spell in SPELLS.keys():
                new_state = current_state.copy()
                new_state.next_spell = spell
                game_states.append(new_state)
        except MemoryError as error:
            print(error)

    return smallest_mana


def part1(_values):
    return do_fight()


def part2(_values):
    return do_fight(True)
