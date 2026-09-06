from typing import List
from BaseClasses import Location

def get_location_name_to_id():
    location_name_to_id = {
        "The Lost Temple - 1 Minikit": 1
    }
    return location_name_to_id

class LEGOIndianaJonesLocation(Location):
    game = "LEGO Indiana Jones The Original Adventures"

def create_locations(world):
    for location, lID in world.location_name_to_id.items():
        menu = world.get_region("Region")
        location = LEGOIndianaJonesLocation(world.player, location, lID, menu)
        menu.locations.append(location)
