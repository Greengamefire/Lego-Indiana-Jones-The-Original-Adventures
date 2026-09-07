from dataclasses import dataclass, field
from .characters import Abilities, CharacterNames

#Constants for each movie in the game
class Movies:
    TOD = "Temple of Doom"
    ROTLA = "Raiders of the Lost Ark"
    TLC = "The Last Crusade"

#Constants for each level in temple of doom
class TOD_Levels:
    LEVEL_NAME = "level"

#Constants for each level in Raiders of the lost Ark
class ROTLA_Levels:
    LEVEL_NAME = "level"

#Constants for each level in The Last Crusade
class TLC_Levels:
    LEVEL_NAME = "level"

#dataclass for minikit data. pretty much just a list designed to contain the abilities required for a minikit
@dataclass
class MinikitData:
    abilities: list[str] = field(default_factory=list)

#dataclass for level data. holds what movie it's from, what number level in the game it is, and a list of minikit data, which is for you to hold 10 so you can define the abilities required for each minikit
@dataclass
class LevelData:
    movie: str
    number: int
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
