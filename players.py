from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Player:
    """Create Player Dataclass
    """

    name: str
    count_player: ClassVar[int] = 0
    player_number: int = field(init=False)

    def __post_init__(self):
        self.player_number = Player.update_counter()

    @classmethod
    def update_counter(cls):
        cls.count_player += 1
        return cls.count_player

    def check_who_plays(self):
        if (self.player_number == 1) and (self.name == "Alice"):
            raise ValueError("The first player cannot be Alice")
        elif (self.player_number == 2) and (self.name != "Alice"):
            raise ValueError("The second player has to be Alice")
        else:
            print("Players are in lexicographic order!...Let's start to play!")