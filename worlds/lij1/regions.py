from BaseClasses import Region

def create_regions(world):
    menu_region = Region("Menu", world.player, world)
    world.regions.append(menu_region)


