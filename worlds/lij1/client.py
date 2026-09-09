import asyncio
from asyncio import Task

import colorama
from CommonClient import CommonContext, ClientCommandProcessor, ClientStatus, get_base_parser, gui_enabled, server_loop, \
    logger
from pymem import pymem
from pymem.exception import ProcessNotFound
from NetUtils import JSONMessagePart, JSONTypes, NetworkItem
from .data.characters import CHARACTERS, CharacterNames

PROCESS_NAME = "LEGOIndy.exe"
module_name = "LEGOIndy.exe"
level1Minikits = 0x5ACEC9
locationID = 1
character_array = 0x5AD4AC

class LIJ1Context(CommonContext):
    game = "LEGO Indiana Jones The Original Adventures"
    items_handling = 7
    command_processor = ClientCommandProcessor
    item_queue: list[NetworkItem]
    game_connect_task: Task
    module_address: int

    game_process: pymem.Pymem | None = None

    def __init__(self, server_address, password):
        super().__init__(server_address, password)

        self.game_connect_task = None
        self.item_consume_task = None

        # Item handling
        self.slot_data = {}
        self.force_resync_on_connect = True
        self.item_queue = []

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()


    def on_items_received(self, items):
        logger.info("Got item")
        for item in items:
            self.item_queue.append(item)

    def on_package(self, cmd: str, args: dict):
        """Handle incoming packets from the server."""
        if cmd == "Connected":
            print("connected")
        if cmd == "ReceivedItems":
          self.on_items_received(args["items"])

    async def open_game_process(self):
        connected = False
        while not connected:
            logger.info("attemting to connect to exe")
            try:
                process = pymem.Pymem(PROCESS_NAME)
                self.game_process = process
                connected = True
            except ProcessNotFound:
                connected = False
            if not connected:
                logger.info("Connection failed")
                await asyncio.sleep(5)
        logger.info("Connection Successful")
        modules = self.game_process.list_modules()
        for m in modules:
            if m.name == module_name:
                self.module_address = m.lpBaseOfDll
        logger.info(hex(self.module_address))
        self.item_consume_task = asyncio.create_task(item_consumer(self), name="Item Consumer")



    def run_gui(self):
        from kvui import GameManager

        class LIJ1Manager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Lego Indiana Jones The Original Adventures Client"

            def build(self):
                ret = super().build()
                return ret

        self.ui = LIJ1Manager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

async def minikit_watcher(ctx: LIJ1Context):
    await ctx.game_connect_task
    done = False
    true_address = level1Minikits + ctx.module_address
    logger.info("Watcher started")
    while not done:
        value = ctx.game_process.read_bytes(true_address, 1)
        if value == b"\x01":
            done = True
            await ctx.send_msgs([{
                "cmd": "LocationChecks",
                "locations": [locationID]
            }])
        await asyncio.sleep(0.2)

async def item_consumer(ctx: LIJ1Context):
    while not ctx.exit_event.is_set():
        if ctx.item_queue:
            item = ctx.item_queue.pop(0)
            itemid = item.item
            if itemid == CHARACTERS[CharacterNames.HAN_SOLO].id:
                character_address = ctx.module_address+ character_array + CHARACTERS[CharacterNames.HAN_SOLO].character_index
                logger.info(f"CharAdd:{hex(character_address)}")
                ctx.game_process.write_uchar(character_address, 3)

        await asyncio.sleep(0.2)


async def async_main(parsed_args):
    ctx = LIJ1Context(parsed_args.connect, parsed_args.password)

    ctx.run_gui()
    await asyncio.sleep(2)

    ctx.game_connect_task = asyncio.create_task(ctx.open_game_process(), name = "Game Connect")
    ctx.minikit_task = asyncio.create_task(minikit_watcher(ctx), name="Minikit Watcher")

    await ctx.exit_event.wait()
    await ctx.shutdown()


def main(args=None):
    colorama.init()
    parser = get_base_parser()
    parsed_args = parser.parse_args(args)
    asyncio.run(async_main(parsed_args))


def launch(args=None):
    main(args)