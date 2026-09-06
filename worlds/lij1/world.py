from BaseClasses import CollectionState, Item, Region, Location, Tutorial, MultiWorld
from .items import get_item_name_to_id, create_items
from .locations import get_location_name_to_id, create_locations
from .regions import create_regions

class LEGOIndianaJonesWorld:
    game = "LEGO Indiana Jones The Original Adventure"

    item_name_to_id = get_item_name_to_id()
    location_name_to_id = get_location_name_to_id()

    def create_items(self):
        create_items(self)

    def create_regions(self):
        create_regions(self)
        create_locations(self)

    def set_rules(self):
        pass

    def fill_slot_data(self):
        return {}
