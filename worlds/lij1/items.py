from BaseClasses import Item, ItemClassification
from .data.characters import CHARACTERS

def get_item_name_to_id():
    item_table = {
        #Get items for character unlocks
        **{name: data.id for name, data in CHARACTERS.items()},
    }
    return item_table

#creates a singular item with all needed information
def create_item(name: str, type:str, world) -> Item:
    if type == "Character":
        return Item(name, ItemClassification.progression, CHARACTERS[name].id, world.player)

def create_items(world):
    itempool: list[Item] = []
    for character, data in CHARACTERS.items():
        item = create_item(character, "Character", world)
        itempool.append(item)


    world.multiworld.itempool += itempool

def get_filler_item_name(world):
    return "filler"