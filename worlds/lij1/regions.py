from BaseClasses import Region
from .locations import get_locations

def create_regions(multiworld, player):
    main_region = Region("Main", player, multiworld)

    for location in get_locations(player):
        location.parent_region = main_region
        main_region.locations.append(location)

    multiworld.regions.append(main_region)
