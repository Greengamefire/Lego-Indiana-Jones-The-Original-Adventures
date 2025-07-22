from BaseClasses import CollectionState, Item, Region, Location, Tutorial, MultiWorld
from .items import item_table, create_item
from .locations import location_table
from .regions import create_regions
from .game import LEGOIndianaJonesOptions

class LEGOIndianaJonesWorld:
    game = "LEGO Indiana Jones"

    option_definitions = LEGOIndianaJonesOptions

    def __init__(self, multiworld: MultiWorld, player: int):
        self.multiworld = multiworld
        self.player = player
        self.options = multiworld.player_options[player]

    def create_items(self):
        itempool = []
        for item_name in item_table:
            item = create_item(item_name, self.player)
            itempool.append(item)
        self.multiworld.itempool += itempool

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        pass

    def generate_basic(self):
        pass

    def fill_slot_data(self):
        return {}
