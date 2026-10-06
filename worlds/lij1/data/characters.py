from dataclasses import dataclass, field

#This holds constants containing all Character names, this way if a name is incorrect or we need to reference the name elsewhere we can change/point to this version of the name
class CharacterNames:
    BANDIT = "Bandit"
    BANDIT_SWORDSMAN = "Bandit Swordsman"
    BARRANCA = "Barranca"
    BAZOOKA_TROOPER_CRUSADE = "Bazooka Trooper (Crusade)"
    BAZOOKA_TROOPER_RAIDERS = "Bazooka Trooper (Raiders)"
    BELLOQ = "Belloq"
    BELLOQ_JUNGLE = "Belloq (Jungle)"
    BELLOQ_ROBES = "Belloq (Robes)"
    BRITISH_COMMANDER = "British Commander"
    BRITISH_OFFICER = "British Officer"
    BRITISH_SOLDIER = "British Soldier"
    BRODY = "Brody"
    CAPTAIN_KATANGA = "Captain Katanga"
    CHATTAR_LAL = "Chattar Lal"
    CHATTAR_LAL_THUGGEE = "Chattar Lal (Thuggee)"
    CHEN = "Chen"
    COLONEL_DIETRICH = "Colonel Dietrich"
    COLONEL_VOGEL = "Colonel Vogel"
    DANCING_GIRL = "Dancing Girl"
    DONOVAN = "Donovan"
    ELSA = "Elsa"
    ELSA_DESERT = "Elsa (Desert)"
    ELSA_OFFICER = "Elsa (Officer)"
    ENEMY_BOXER = "Enemy Boxer"
    ENEMY_BUTLER = "Enemy Butler"
    ENEMY_GUARD = "Enemy Guard"
    ENEMY_GUARD_MOUNTAINS = "Enemy Guard (Mountains)"
    ENEMY_OFFICER = "Enemy Officer"
    ENEMY_OFFICER_DESERT = "Enemy Officer (Desert)"
    ENEMY_PILOT = "Enemy Pilot"
    ENEMY_RADIO_OPERATOR = "Enemy Radio Operator"
    ENEMY_SOLDIER = "Enemy Soldier"
    FIRST_MATE = "First Mate"
    GRAIL_KNIGHT = "Grail Knight"
    HENRY_JONES_SR = "Henry Jones Sr."
    HOVITOS_TRIBESMAN = "Hovitos Tribesman"
    INDIANA_JONES = "Indiana Jones"
    INDIANA_JONES_ARMY_DISGUISE = "Indiana Jones (Army Disguise)"
    INDIANA_JONES_DESERT = "Indiana Jones (Desert)"
    INDIANA_JONES_DESERT_DISGUISE = "Indiana Jones (Desert Disguise)"
    INDIANA_JONES_DINNER_SUIT = "Indiana Jones (Dinner Suit)"
    INDIANA_JONES_KALI = "Indiana Jones (Kali)"
    INDIANA_JONES_OFFICER = "Indiana Jones (Officer)"
    INDIANA_JONES_PROFESSOR = "Indiana Jones (Professor)"
    JOCK = "Jock"
    JUNGLE_GUIDE = "Jungle Guide"
    KAO_KAN = "Kao Kan"
    KAZIM = "Kazim"
    KAZIM_DESERT = "Kazim (Desert)"
    LAO_CHE = "Lao Che"
    MAHARAJAH = "Maharajah"
    MAJOR_TOHT = "Major Toht"
    MARION = "Marion"
    MARION_CAIRO = "Marion (Cairo)"
    MARION_EVENING_DRESS = "Marion (Evening Dress)"
    MARION_NIGHTGOWN = "Marion (Nightgown)"
    MASKED_BANDIT = "Masked Bandit"
    MOLA_RAM = "Mola Ram"
    MONKEY_MAN = "Monkey Man"
    PANKOT_ASSASSIN = "Pankot Assassin"
    PANKOT_GUARD = "Pankot Guard"
    SALLAH_DESERT = "Sallah (Desert)"
    SALLAH_FEZ = "Sallah (Fez)"
    SATIPO = "Satipo"
    SHERPA_BRAWLER = "Sherpa Brawler"
    SHERPA_GUNNER = "Sherpa Gunner"
    SHORT_ROUND = "Short Round"
    SLAVE_CHILD = "Slave Child"
    THUGGEE = "Thuggee"
    THUGGEE_ACOLYTE = "Thuggee Acolyte"
    THUGGEE_SLAVE_DRIVER = "Thuggee Slave Driver"
    VILLAGE_DIGNITARY = "Village Dignitary"
    VILLAGE_ELDER = "Village Elder"
    WILLIE = "Willie"
    WILLIE_CEREMONY = "Willie (Ceremony)"
    WILLIE_DINNER_SUIT = "Willie (Dinner Suit)"
    WILLIE_EVENING_DRESS = "Willie (Evening Dress)"
    WILLIE_PAJAMAS = "Willie (Pajamas)"
    WU_HAN = "Wu Han"

#Same thing as character Names but for the name of abilities
class Abilities:
    HIGH_JUMP = "High Jump"
    BUMS = "Bums"
    EVIL = "Evil"
    SHORT = "Short"
    GLASS_BREAK = "Glass Break"
    SHOVEL = "Shovel"
    EXPLOSIVE = "Explosive"
    ACADEMIC = "Academic"
    ENEMY_ACCESS = "Enemy Access"
    MECHANIC = "Mechanic"
    NEUTRAL_SPECIAL = "Neutral Special"
    INDY = "Indy"

#this is basically a structure that we will call back to that will contain the information for each character we need
@dataclass
class CharacterData:
    id: int
    character_index: int #what part of the character array this character is stored -1. for example indiana jones is at the first spot so his index is 0. han solo is at spot 2 with index 1
    abilities: list[str] = field(default_factory=list)

#The Dictionary containing all the needed information for characters. Key is the name, which gives character data. Items will iterate through this to create all characters and logic will use it when it comes to locations that need characters with certain abilities
CHARACTERS: dict[str, CharacterData] = {
    CharacterNames.BANDIT: CharacterData(id=1, character_index=1, abilities=[]),
    CharacterNames.BANDIT_SWORDSMAN: CharacterData(id=2, character_index=2, abilities=[]),
    CharacterNames.BARRANCA: CharacterData(id=3, character_index=3, abilities=[]),
    CharacterNames.BAZOOKA_TROOPER_CRUSADE: CharacterData(id=4, character_index=4, abilities=[]),
    CharacterNames.BAZOOKA_TROOPER_RAIDERS: CharacterData(id=5, character_index=5, abilities=[]),
    CharacterNames.BELLOQ: CharacterData(id=6, character_index=6, abilities=[]),
    CharacterNames.BELLOQ_JUNGLE: CharacterData(id=7, character_index=7, abilities=[]),
    CharacterNames.BELLOQ_ROBES: CharacterData(id=8, character_index=8, abilities=[]),
    CharacterNames.BRITISH_COMMANDER: CharacterData(id=9, character_index=9, abilities=[]),
    CharacterNames.BRITISH_OFFICER: CharacterData(id=10, character_index=10, abilities=[]),
    CharacterNames.BRITISH_SOLDIER: CharacterData(id=11, character_index=11, abilities=[]),
    CharacterNames.BRODY: CharacterData(id=12, character_index=12, abilities=[]),
    CharacterNames.CAPTAIN_KATANGA: CharacterData(id=13, character_index=13, abilities=[]),
    CharacterNames.CHATTAR_LAL: CharacterData(id=14, character_index=14, abilities=[]),
    CharacterNames.CHATTAR_LAL_THUGGEE: CharacterData(id=15, character_index=15, abilities=[]),
    CharacterNames.CHEN: CharacterData(id=16, character_index=16, abilities=[]),
    CharacterNames.COLONEL_DIETRICH: CharacterData(id=17, character_index=17, abilities=[]),
    CharacterNames.COLONEL_VOGEL: CharacterData(id=18, character_index=18, abilities=[]),
    CharacterNames.DANCING_GIRL: CharacterData(id=19, character_index=19, abilities=[]),
    CharacterNames.DONOVAN: CharacterData(id=20, character_index=20, abilities=[]),
    CharacterNames.ELSA: CharacterData(id=21, character_index=21, abilities=[]),
    CharacterNames.ELSA_DESERT: CharacterData(id=22, character_index=22, abilities=[]),
    CharacterNames.ELSA_OFFICER: CharacterData(id=23, character_index=23, abilities=[]),
    CharacterNames.ENEMY_BOXER: CharacterData(id=24, character_index=24, abilities=[]),
    CharacterNames.ENEMY_BUTLER: CharacterData(id=25, character_index=25, abilities=[]),
    CharacterNames.ENEMY_GUARD: CharacterData(id=26, character_index=26, abilities=[]),
    CharacterNames.ENEMY_GUARD_MOUNTAINS: CharacterData(id=27, character_index=27, abilities=[]),
    CharacterNames.ENEMY_OFFICER: CharacterData(id=28, character_index=28, abilities=[]),
    CharacterNames.ENEMY_OFFICER_DESERT: CharacterData(id=29, character_index=29, abilities=[]),
    CharacterNames.ENEMY_PILOT: CharacterData(id=30, character_index=30, abilities=[]),
    CharacterNames.ENEMY_RADIO_OPERATOR: CharacterData(id=31, character_index=31, abilities=[]),
    CharacterNames.ENEMY_SOLDIER: CharacterData(id=32, character_index=32, abilities=[]),
    CharacterNames.FIRST_MATE: CharacterData(id=33, character_index=33, abilities=[]),
    CharacterNames.GRAIL_KNIGHT: CharacterData(id=34, character_index=34, abilities=[]),
    CharacterNames.HENRY_JONES_SR: CharacterData(id=35, character_index=35, abilities=[]),
    CharacterNames.HOVITOS_TRIBESMAN: CharacterData(id=36, character_index=36, abilities=[]),
    CharacterNames.INDIANA_JONES: CharacterData(id=37, character_index=37, abilities=[]),
    CharacterNames.INDIANA_JONES_ARMY_DISGUISE: CharacterData(id=38, character_index=38, abilities=[]),
    CharacterNames.INDIANA_JONES_DESERT: CharacterData(id=39, character_index=39, abilities=[]),
    CharacterNames.INDIANA_JONES_DESERT_DISGUISE: CharacterData(id=40, character_index=40, abilities=[]),
    CharacterNames.INDIANA_JONES_DINNER_SUIT: CharacterData(id=41, character_index=41, abilities=[]),
    CharacterNames.INDIANA_JONES_KALI: CharacterData(id=42, character_index=42, abilities=[]),
    CharacterNames.INDIANA_JONES_OFFICER: CharacterData(id=43, character_index=43, abilities=[]),
    CharacterNames.INDIANA_JONES_PROFESSOR: CharacterData(id=44, character_index=44, abilities=[]),
    CharacterNames.JOCK: CharacterData(id=45, character_index=45, abilities=[]),
    CharacterNames.JUNGLE_GUIDE: CharacterData(id=46, character_index=46, abilities=[]),
    CharacterNames.KAO_KAN: CharacterData(id=47, character_index=47, abilities=[]),
    CharacterNames.KAZIM: CharacterData(id=48, character_index=48, abilities=[]),
    CharacterNames.KAZIM_DESERT: CharacterData(id=49, character_index=49, abilities=[]),
    CharacterNames.LAO_CHE: CharacterData(id=50, character_index=50, abilities=[]),
    CharacterNames.MAHARAJAH: CharacterData(id=51, character_index=51, abilities=[]),
    CharacterNames.MAJOR_TOHT: CharacterData(id=52, character_index=52, abilities=[]),
    CharacterNames.MARION: CharacterData(id=53, character_index=53, abilities=[]),
    CharacterNames.MARION_CAIRO: CharacterData(id=54, character_index=54, abilities=[]),
    CharacterNames.MARION_EVENING_DRESS: CharacterData(id=55, character_index=55, abilities=[]),
    CharacterNames.MARION_NIGHTGOWN: CharacterData(id=56, character_index=56, abilities=[]),
    CharacterNames.MASKED_BANDIT: CharacterData(id=57, character_index=57, abilities=[]),
    CharacterNames.MOLA_RAM: CharacterData(id=58, character_index=58, abilities=[]),
    CharacterNames.MONKEY_MAN: CharacterData(id=59, character_index=59, abilities=[]),
    CharacterNames.PANKOT_ASSASSIN: CharacterData(id=60, character_index=60, abilities=[]),
    CharacterNames.PANKOT_GUARD: CharacterData(id=61, character_index=61, abilities=[]),
    CharacterNames.SALLAH_DESERT: CharacterData(id=62, character_index=62, abilities=[]),
    CharacterNames.SALLAH_FEZ: CharacterData(id=63, character_index=63, abilities=[]),
    CharacterNames.SATIPO: CharacterData(id=64, character_index=64, abilities=[]),
    CharacterNames.SHERPA_BRAWLER: CharacterData(id=65, character_index=65, abilities=[]),
    CharacterNames.SHERPA_GUNNER: CharacterData(id=66, character_index=66, abilities=[]),
    CharacterNames.SHORT_ROUND: CharacterData(id=67, character_index=67, abilities=[]),
    CharacterNames.SLAVE_CHILD: CharacterData(id=68, character_index=68, abilities=[]),
    CharacterNames.THUGGEE: CharacterData(id=69, character_index=69, abilities=[]),
    CharacterNames.THUGGEE_ACOLYTE: CharacterData(id=70, character_index=70, abilities=[]),
    CharacterNames.THUGGEE_SLAVE_DRIVER: CharacterData(id=71, character_index=71, abilities=[]),
    CharacterNames.VILLAGE_DIGNITARY: CharacterData(id=72, character_index=72, abilities=[]),
    CharacterNames.VILLAGE_ELDER: CharacterData(id=73, character_index=73, abilities=[]),
    CharacterNames.WILLIE: CharacterData(id=74, character_index=74, abilities=[]),
    CharacterNames.WILLIE_CEREMONY: CharacterData(id=75, character_index=75, abilities=[]),
    CharacterNames.WILLIE_DINNER_SUIT: CharacterData(id=76, character_index=76, abilities=[]),
    CharacterNames.WILLIE_EVENING_DRESS: CharacterData(id=77, character_index=77, abilities=[]),
    CharacterNames.WILLIE_PAJAMAS: CharacterData(id=78, character_index=78, abilities=[]),
    CharacterNames.WU_HAN: CharacterData(id=79, character_index=79, abilities=[]),


