from dataclasses import dataclass
from typing import List
from BaseClasses import Location
from .data.levels import LEVEL_DATA, Movies

class LocationIds:
    ROTLA = 1000
    TOD = 2000
    TLC = 3000

class LocationTypes:
    LEVEL_COMPLETION = "Level Completion"
    MINIKIT = "Minikit"
    PARCEL = "Parcel"

class LEGOIndianaJonesLocation(Location):
    game = "LEGO Indiana Jones The Original Adventures"

@dataclass
class LocationData:
    type: str
    id: int
    region: str

locations_dict = {
    **{f"{level} Complete": LocationData(type = LocationTypes.LEVEL_COMPLETION, id = (data.number*100) + LocationIds.ROTLA, region = level) for level, data in LEVEL_DATA.items() if data.movie == Movies.ROTLA},
    **{f"{level} Complete": LocationData(type = LocationTypes.LEVEL_COMPLETION, id = (data.number*100) + LocationIds.TOD, region = level) for level, data in LEVEL_DATA.items() if data.movie == Movies.TOD},
    **{f"{level} Complete": LocationData(type = LocationTypes.LEVEL_COMPLETION, id = (data.number*100) + LocationIds.TLC, region = level) for level, data in LEVEL_DATA.items() if data.movie == Movies.TLC},
    **{f"{level} Minikit {i + 1}": LocationData(type = LocationTypes.MINIKIT, id = (data.number * 100) + LocationIds.ROTLA + i + 1, region = level) for level, data in LEVEL_DATA.items() for i, _ in enumerate(data.kitData) if data.movie == Movies.ROTLA},
    **{f"{level} Minikit {i + 1}": LocationData(type = LocationTypes.MINIKIT, id = (data.number * 100) + LocationIds.TOD + i + 1, region = level) for level, data in LEVEL_DATA.items() for i, _ in enumerate(data.kitData) if data.movie == Movies.TOD},
    **{f"{level} Minikit {i + 1}": LocationData(type = LocationTypes.MINIKIT, id = (data.number * 100) + LocationIds.TLC + i + 1, region = level) for level, data in LEVEL_DATA.items() for i, _ in enumerate(data.kitData) if data.movie == Movies.TLC},
    **{f"{level} Parcel": LocationData(type = LocationTypes.PARCEL, id = (data.number*100) + LocationIds.ROTLA + 11, region = level) for level, data in LEVEL_DATA.items() if data.movie == Movies.ROTLA},
    **{f"{level} Parcel": LocationData(type = LocationTypes.PARCEL, id = (data.number*100) + LocationIds.TOD + 11, region = level) for level, data in LEVEL_DATA.items() if data.movie == Movies.TOD},
    **{f"{level} Parcel": LocationData(type = LocationTypes.PARCEL, id = (data.number*100) + LocationIds.TLC + 11, region = level) for level, data in LEVEL_DATA.items() if data.movie == Movies.TLC},
}

#define all location names and id's that can be in the world
def get_location_name_to_id():
    return {**{location: data.id for location, data in locations_dict.items()},}

def create_locations(world):
    for location, data in locations_dict.items():
        region = world.get_region(data.region)
        region.locations.append(LEGOIndianaJonesLocation(world.player, location, data.id, region))