from BaseClasses import Item, ItemClassification
from .data.characters import CHARACTERS

def get_item_name_to_id():
    item_table = {
        #Get items for character unlocks
        **{name: data.id for name, data in CHARACTERS.items()},
    }
    return item_table

#creates a singular item with all needed information
def create_item(name: str, world) -> Item:
    return Item(name, ItemClassification.progression, world.item_name_to_id[name], world.player)

def create_items(world):
    itempool: list[Item] = []
    for item, Itemid in world.item_name_to_id.items():
        itempool.append(create_item(item, world))

    world.multiworld.itempool += itempool

def get_filler_item_name(world):
    return "filler"