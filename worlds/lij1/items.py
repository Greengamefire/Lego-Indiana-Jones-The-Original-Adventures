from BaseClasses import Item, ItemClassification
from .data.characters import CHARACTERS

#holds const references to all item type strings
class ItemTypes:
    CHARACTER = "Character"

#defines all item names and IDs in the world regardless of settings
def get_item_name_to_id():
    item_table = {
        #Get items for character unlocks
        **{name: data.id for name, data in CHARACTERS.items()},
    }
    return item_table

#creates a singular item with all needed information
def create_item(name: str, type:str, world) -> Item:
    if type == ItemTypes.CHARACTER: #for all items of the character type
        return Item(name, ItemClassification.progression, CHARACTERS[name].id, world.player)

#Creates items for generation
def create_items(world):
    itempool: list[Item] = [] #list that contains all our items. append new items to this
    for character, data in CHARACTERS.items(): #loop through all characters in the characters dict
        item = create_item(character, ItemTypes.CHARACTER, world) #pass the character into the create_item with type set to character. returns our new item object
        itempool.append(item) #add the new item to the itempool list


    world.multiworld.itempool += itempool #add the new items to the multiworlds itempool. += means add or equals. if the multiworld itempool is empty theen it will set it equal to our itempool but if items are in it our items get added to the list

def get_filler_item_name(world):
    return "filler"