from dataclasses import dataclass, field
from .characters import Abilities, CharacterNames
from ...oot.ntype import int32


#Constants for each movie in the game
class Movies:
    TOD = "Temple of Doom"
    ROTLA = "Raiders of the Lost Ark"
    TLC = "The Last Crusade"

#Constants for each level in temple of doom
class TOD_Levels:
    SHANGHAI_SHOWDOWN = "Shanghai Showdown"
    PANKOT_SECRETS = "Pankot Secrets"
    THE_TEMPLE_OF_KALI = "The Temple of Kali"
    FREE_THE_SLAVES = "Free the Slaves"
    ESCAPE_THE_MINES = "Escape the Mines"
    BATTLE_ON_THE_BRIDGE = "Battle on the Bridge"

#Constants for each level in Raiders of the lost Ark
class ROTLA_Levels:
    THE_LOST_TEMPLE = "The Lost Temple"
    INTO_THE_MOUNTAINS = "Into the Mountains"
    CITY_OF_DANGER = "City of Danger"
    THE_WELL_OF_SOULS = "The Well of Souls"
    PURSUING_THE_ARK = "Pursuing the Ark"
    OPENING_THE_ARK = "Opening the Ark"

#Constants for each level in The Last Crusade
class TLC_Levels:
    THE_HUNT_FOR_SIR_RICHARD = "The Hunt for Sir Richard"
    CASTLE_RESCUE = "Castle Rescue"
    MOTORCYCLE_ESCAPE = "Motorcycle Escape"
    TROUBLE_IN_THE_SKY = "Trouble in the Sky"
    DESERT_AMBUSH = "Desert Ambush"
    TEMPLE_OF_THE_GRAIL = "Temple of the Grail"

class Extras:
    SECRET_CHARACTERS = "Secret Characters"

#dataclass for minikit data. pretty much just a list designed to contain the abilities required for a minikit
@dataclass
class MinikitData:
    abilities: list[str] = field(default_factory=list)

#dataclass for level data. holds what movie it's from, what number level in the game it is, and a list of minikit data, which is for you to hold 10 so you can define the abilities required for each minikit
@dataclass
class LevelData:
    movie: str
    number: int
    unlockAddress: int
    FreePlayAddress: int
    parcelAddress: int
    minikitAddress: int
    trueAdventurerAddress: int #the first address
    Parcel: str = "NONE"

    kitData: list[MinikitData] = field(default_factory=list)

 #Might redo this again. level data takes a list of Minikit data which holds a list of abilities. the idea is each instance of Minikit data will hold the abilities to get one of the minikits in the level
LEVEL_DATA: dict[str, LevelData] = {
    TOD_Levels.LEVEL_NAME: LevelData(
        movie = Movies.TOD,
        number = 1,
        kitData = [
            MinikitData([Abilities.FEMALE]),
            MinikitData([Abilities.FEMALE, Abilities.FEMALE])
        ]
    ),
}
