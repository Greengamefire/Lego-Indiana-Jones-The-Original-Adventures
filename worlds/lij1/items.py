from BaseClasses import Item, ItemClassification

def get_item_name_to_id():
    item_table = {
        "Han Solo": 1
    }


def create_item(name: str, world) -> Item:
    return Item(name, ItemClassification.progression, 1, world.player)

def create_items(world):
    itempool: list[Item] = []
    for item, Itemid in world.item_name_to_id():
        itempool.append(create_item(item, world))

    world.multiworld.itempool += itempool