import datetime
import secrets

from GameMode import GameMode

from ..game import Game
from ..player import Player


class CoinFlipMode(GameMode):
    """Jeu de la pièce"""
    def play(self, p2: Player, p1: Player, choice="heads"):
        """Executes a single round of a coin-flip game between two players.
        Args:
            id_player (int): The unique identifier of the first player.
            id_opponent (int): The unique identifier of the opponent.
            choice (str, optional): The player's choice ('heads' or 'tails'). Defaults to "heads".
        Returns:
            dict: A dictionary containing the match details and new elo
        """

        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        return Game(p1, p2, "coinflip", winner, "Rien à dire", datetime.now())
