import datetime
import random

from ..game import Game
from .GameMode import GameMode


class DiceMode(GameMode):
    """Inherits of the GameMode class, defines the diceroll game."""

    def play(self, p1, p2) -> Game:
        p1_roll = random.randint(1, 6)
        p2_roll = random.randint(1, 6)
        if p1_roll < p2_roll:
            winner = p2_roll
        elif p1_roll > p2_roll:
            winner = p1_roll
        else:
            winner = None
        return Game(p1, p2, "dice", winner, "Rien à dire", datetime.now())
