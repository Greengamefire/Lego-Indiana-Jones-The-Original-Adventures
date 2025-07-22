from typing import List
from BaseClasses import Location

location_table = [
    "Lost Temple Entrance",
    "Motorcycle Chase",
    "Knight's Tomb",
    "Library Puzzle",
    "Train Escape",
    "Mine Cart Chase"
]

class LEGOIndianaJonesLocation(Location):
    game = "LEGO Indiana Jones"

def get_locations(player: int) -> List[LEGOIndianaJonesLocation]:
    return [LEGOIndianaJonesLocation(player, name, None) for name in location_table]
