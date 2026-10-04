from BaseClasses import Region, Entrance
from .data.levels import LEVEL_DATA

def create_regions(world):
    menu_region = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    for level, data in LEVEL_DATA.items():
        region = Region(level, world.player, world.multiworld)
        world.multiworld.regions.append(region)
        entrance = Entrance(world.player, f"menu -> {level}", menu_region)
        menu_region.exits.append(entrance)
        entrance.connect(region)