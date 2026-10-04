from typing import List
from BaseClasses import Location
from .data.levels import LEVEL_DATA, Movies

#define all location names and id's that can be in the world
def get_location_name_to_id():
    location_name_to_id = {
        **{f"{level} Complete": (data.number*100) + 1000 for level, data in LEVEL_DATA.items() if data.movie == Movies.ROTLA}, #ROTLA levels, id = movieNum, levelNum , 00 so first level of first movie = 1100
        **{f"{level} Complete": (data.number*100) + 2000 for level, data in LEVEL_DATA.items() if data.movie == Movies.TOD}, #TOD Levels, go in 2000 id range
        **{f"{level} Complete": (data.number*100) + 3000 for level, data in LEVEL_DATA.items() if data.movie == Movies.TLC}, #TLC levels, go in 3000 id range (Young indy will go in 4000)
        **{f"{level} Minikit {i + 1}": (data.number * 100) + 1000 + i + 1 for level, data in LEVEL_DATA.items() for i, _ in enumerate(data.kitData) if data.movie == Movies.ROTLA}, #Loop through each minikit in each level in ROTLA, go in the ids right after level completion so levelId + 1-10, must add 1 to i becuase indexes start at 0. leaving it would create a minikit 0 which would have the same id as level completion throwing an error
        **{f"{level} Minikit {i + 1}": (data.number * 100) + 2000 + i + 1 for level, data in LEVEL_DATA.items() for i, _ in enumerate(data.kitData) if data.movie == Movies.TOD}, #TOD Minikits
        **{f"{level} Minikit {i + 1}": (data.number * 100) + 3000 + i + 1 for level, data in LEVEL_DATA.items() for i, _ in enumerate(data.kitData) if data.movie == Movies.TLC}, #TLC Minikits
        **{f"{level} Parcel": (data.number * 100) + 1000 + 11 for level, data in LEVEL_DATA.items() if data.movie == Movies.ROTLA}, #ROTLA Parcels
        **{f"{level} Parcel": (data.number * 100) + 2000 + 11 for level, data in LEVEL_DATA.items() if data.movie == Movies.TOD}, #TOD Parcels
        **{f"{level} Parcel": (data.number * 100) + 3000 + 11 for level, data in LEVEL_DATA.items() if data.movie == Movies.TLC} #TLC Parcels
    }
    return location_name_to_id

class LEGOIndianaJonesLocation(Location):
    game = "LEGO Indiana Jones The Original Adventures"

def create_locations(world):
    for level, data in LEVEL_DATA.items():
        region = world.get_region(level)
        #level completion location
        completion_n = f"{level} Complete"
        completion = LEGOIndianaJonesLocation(world.player, completion_n, world.location_name_to_id[completion_n], region)
        #minikit locations
        kits =[LEGOIndianaJonesLocation(world.player,f"{level} Minikit {i+1}",world.location_name_to_id[f"{level} Minikit {i+1}"], region) for i, _ in enumerate(data.kitData)]
        #parcel location
        parcel = LEGOIndianaJonesLocation(world.player, f"{level} Parcel", world.location_name_to_id[f"{level} Parcel"], region)
        #append all locations to the level region
        region.locations.append(completion)
        region.locations.append(parcel)
        region.locations.extend(kits)