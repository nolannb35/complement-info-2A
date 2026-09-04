import secrets
from datetime import datetime
from business_objects.player import Player
from business_objects.game import Game
from business_objects.game_mode import GameMode

class CoinFlipMode(GameMode) :
    def play(self, p1 : Player, p2 : Player):
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2
        return Game(p1, p2, "coinflip", winner, "A game of coin flip", datetime.now())

