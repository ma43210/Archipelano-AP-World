from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, Rule

if TYPE_CHECKING:
    from .world import ArchipelanoWorld


def set_all_rules(world: ArchipelanoWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: ArchipelanoWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    level_1_to_level_2 = world.get_entrance("Level 1 to Level 2")
    level_2_to_level_3 = world.get_entrance("Level 2 to Level 3")
    level_3_to_level_4 = world.get_entrance("Level 3 to Level 4")
    level_4_to_level_5 = world.get_entrance("Level 4 to Level 5")
    level_5_to_level_6 = world.get_entrance("Level 5 to Level 6")
    level_6_to_level_7 = world.get_entrance("Level 6 to Level 7")
    level_7_to_level_8 = world.get_entrance("Level 7 to Level 8")
    level_8_to_level_9 = world.get_entrance("Level 8 to Level 9")
    level_9_to_level_10 = world.get_entrance("Level 9 to Level 10")
    level_10_to_victory = world.get_entrance("Level 10 to Victory")

    # An access rule is a function. We can define this function like any other function.
    # This function must accept exactly one parameter: A "CollectionState".
    # A CollectionState describes the current progress of the players in the multiworld, i.e. what items they have,
    # which regions they've reached, etc.
    # In an access rule, we can ask whether the player has a collected a certain item.
    # We can do this via the state.has(...) function.
    # This function takes an item name, a player number, and an optional count parameter (more on that below)
    # Since a rule only takes a CollectionState parameter, but we also need the player number in the state.has call,
    # our function needs to be locally defined so that it has access to the player number from the outer scope.
    # In our case, we are inside a function that has access to the "world" parameter, so we can use world.player.

    # Because the function has to be defined locally, most worlds prefer the lambda syntax.
    world.set_rule(level_1_to_level_2, Has("Key_1"))
    world.set_rule(level_2_to_level_3, Has("Key_2"))
    world.set_rule(level_3_to_level_4, Has("Key_3"))
    world.set_rule(level_4_to_level_5, Has("Key_4"))
    world.set_rule(level_5_to_level_6, Has("Key_5"))
    world.set_rule(level_6_to_level_7, Has("Key_6"))
    world.set_rule(level_7_to_level_8, Has("Key_7"))
    world.set_rule(level_8_to_level_9, Has("Key_8"))
    world.set_rule(level_9_to_level_10, Has("Key_9"))
    world.set_rule(level_10_to_victory, Has("Key_10"))


def set_all_location_rules(world: ArchipelanoWorld) -> None:
    door_1 = world.get_location("Door_1")
    door_2 = world.get_location("Door_2")
    door_3 = world.get_location("Door_3")
    door_4 = world.get_location("Door_4")
    door_5 = world.get_location("Door_5")
    door_6 = world.get_location("Door_6")
    door_7 = world.get_location("Door_7")
    door_8 = world.get_location("Door_8")
    door_9 = world.get_location("Door_9")
    door_10 = world.get_location("Door_10")

    world.set_rule(door_1, Has("Key_1"))
    world.set_rule(door_2, Has("Key_2"))
    world.set_rule(door_3, Has("Key_3"))
    world.set_rule(door_4, Has("Key_4"))
    world.set_rule(door_5, Has("Key_5"))
    world.set_rule(door_6, Has("Key_6"))
    world.set_rule(door_7, Has("Key_7"))
    world.set_rule(door_8, Has("Key_8"))
    world.set_rule(door_9, Has("Key_9"))
    world.set_rule(door_10, Has("Key_10"))


def set_completion_condition(world: ArchipelanoWorld) -> None:
    # Finally, we need to set a completion condition for our world, defining what the player needs to win the game.
    # You can just set a completion condition directly like any other condition, referencing items the player receives:

    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.set_completion_rule(Has("Victory"))