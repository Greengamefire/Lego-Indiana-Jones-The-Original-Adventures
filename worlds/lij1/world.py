from worlds.AutoWorld import World
from BaseClasses import CollectionState, Item, Region, Location, Tutorial, MultiWorld
from worlds.LauncherComponents import Type, components, launch_subprocess, Component
from .webWorld import LIJ1Web
from .items import get_item_name_to_id, create_items, get_filler_item_name
from .locations import get_location_name_to_id, create_locations
from .regions import create_regions
from .lij1_options import LIJ1Options

class LEGOIndianaJonesWorld(World):
    game = "LEGO Indiana Jones The Original Adventures"
    web = LIJ1Web()
    options: LIJ1Options

    item_name_to_id = get_item_name_to_id()
    location_name_to_id = get_location_name_to_id()

    def run_client(*args):
        from .client import launch
        launch_subprocess(launch, name="LIJ1Client", args=args)

    components.append(
        Component("Lego Indiana Jones The Original Adventures Client", func=run_client, component_type=Type.CLIENT)
    )

    def create_items(self):
        create_items(self)

    def create_regions(self):
        create_regions(self)
        create_locations(self)

    def set_rules(self):
        pass

    def get_filler_item_name(self):
        get_filler_item_name(self)

    def fill_slot_data(self):
        return {}
