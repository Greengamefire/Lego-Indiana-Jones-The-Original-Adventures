import asyncio
import colorama
from CommonClient import CommonContext, ClientCommandProcessor, ClientStatus, get_base_parser, gui_enabled, server_loop

class LIJ1Context(CommonContext):
    game = "LEGO Indiana Jones The Original Adventures"
    items_handling = 7
    command_processor = ClientCommandProcessor

    def __init__(self, server_address, password):
        super().__init__(server_address, password)

        # Item handling
        self.slot_data = {}
        self.force_resync_on_connect = True

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()


    async def on_items_received(self, items):
        print("on_items_received", len(items))

    def on_package(self, cmd: str, args: dict):
        """Handle incoming packets from the server."""
        if cmd == "Connected":
            print("connected")

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

async def async_main(parsed_args):
    ctx = LIJ1Context(parsed_args.connect, parsed_args.password)

    ctx.run_gui()

    await ctx.exit_event.wait()
    await ctx.shutdown()



def main(args=None):
    colorama.init()
    parser = get_base_parser()
    parsed_args = parser.parse_args(args)
    asyncio.run(async_main(parsed_args))


def launch(args=None):
    main(args)