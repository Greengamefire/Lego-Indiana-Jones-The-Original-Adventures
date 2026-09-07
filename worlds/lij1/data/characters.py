from dataclasses import dataclass, field

#This holds constants containing all Character names, this way if a name is incorrect or we need to reference the name elsewhere we can change/point to this version of the name
class CharacterNames:
    HAN_SOLO = "Han Solo"

#Same thing as character Names but for the name of abilities
class Abilities:
    FEMALE = "Female"

#this is basically a structure that we will call back to that will contain the information for each character we need
@dataclass
class CharacterData:
    id: int
    abilities: list[str] = field(default_factory=list)

#The Dictionary containing all the needed information for characters. Key is the name, which gives character data. Items will iterate through this to create all characters and logic will use it when it comes to locations that need characters with certain abilities
CHARACTERS: dict[str, CharacterData] = {
    CharacterNames.HAN_SOLO: CharacterData(id = 1, abilities = [Abilities.FEMALE,Abilities.FEMALE,Abilities.FEMALE]),
}


