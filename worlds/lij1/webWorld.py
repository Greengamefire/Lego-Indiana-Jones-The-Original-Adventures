from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class LIJ1Web(WebWorld):
    theme = 'stone'
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "LIJ1 Setup",
        "English",
        "lij1_en.md",
        "lij1/en",
        ["Greengamefire"]
    )]