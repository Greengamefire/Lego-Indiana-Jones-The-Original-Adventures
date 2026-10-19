from dataclasses import dataclass
from BaseClasses import Item, ItemClassification
from .data.characters import CHARACTERS
from .data.constants import BASEID

class ItemIds:
    CHARACTERID = BASEID

#holds const references to all item type strings
class ItemTypes:
    CHARACTER = "Character"

class LIJ1Item(Item):
    game = "LEGO Indiana Jones The Original Adventures"

@dataclass
class LIJ1ItemData:
    type:str
    id:int
    classification:ItemClassification

items_dict = {
    **{name: LIJ1ItemData(type = ItemTypes.CHARACTER, id = ItemIds.CHARACTERID + data.id, classification = ItemClassification.progression) for name, data in CHARACTERS.items()},
}

filler_dict = {
    "filler": LIJ1ItemData(type = "Filler", id = 1, classification = ItemClassification.filler),
}

#defines all item names and IDs in the world regardless of settings
def get_item_name_to_id():
    return {
        **{name: data.id for name, data in items_dict.items()},
        **{name: data.id for name, data in filler_dict.items()},
    }

#Creates items for generation
def create_items(world):
    itempool: list[Item] = [] #list that contains all our items. append new items to this
    for name, data in items_dict.items():
        itempool.append(LIJ1Item(name, data.classification,data.id, world.player))

    itempool.extend(create_filler(world, len(itempool)))
    world.multiworld.itempool += itempool

def create_filler(world, filled_locations):
    fillerpool: list[Item] = []
    unfilled_locations = world.multiworld.get_unfilled_locations(world.player)
    needed_items = len(unfilled_locations) - filled_locations
    for i in range (needed_items):
        random_item = world.random.choice(list(filler_dict.keys()))
        data = filler_dict[random_item]
        fillerpool.append(LIJ1Item(random_item, data.classification, data.id, world.player))

    return fillerpool