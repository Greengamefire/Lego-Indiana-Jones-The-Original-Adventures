from dataclasses import dataclass
from Options import Toggle

class Test(Toggle):
    display_name = "Test"
    default = False

@dataclass
class LIJ1Options:
    test: Test