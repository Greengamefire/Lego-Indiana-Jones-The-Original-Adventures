from BaseClasses import Region, Entrance

def create_regions(world):
    menu_region = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    region = Region("Region", world.player, world.multiworld)
    world.multiworld.regions.append(region)

    entrance = Entrance(world.player, "menu -> region", menu_region)
    menu_region.exits.append(entrance)
    entrance.connect(region)


