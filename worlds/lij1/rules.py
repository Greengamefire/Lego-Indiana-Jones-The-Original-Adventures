from BaseClasses import MultiWorld
from rule_builder.rules import *
from .data.levels import LEVEL_DATA
from .data.characters import CHARACTERS
#ToDo do rule logic here
def set_rules(world):
    for level, data in LEVEL_DATA.items():
        rule = Has(world, f"{level} Unlock")
        entrance = world.multiworld.get_entrance(f"menu -> {level}")
        entrance.add_rule(rule)