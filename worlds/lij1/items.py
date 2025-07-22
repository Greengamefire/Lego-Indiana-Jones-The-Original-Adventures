from BaseClasses import Item

item_table = [
    "Whip",
    "Shovel",
    "Wrench",
    "Bazooka",
    "Torch",
    "Book",
    "Sword",
    "Key",
    "Grail",
    "Crystal Skull"
]

def create_item(name: str, player: int) -> Item:
    return Item(name, True, None, player)
