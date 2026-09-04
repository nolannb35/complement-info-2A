from abc import ABC

from .game import Game
from .player import Player

class Game_mode(ABC) :
    @abstractmethod
    def play(self, p1: Player, p2: Player) -> Game :
        pass

