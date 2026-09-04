from datetime import datetime
from business_objects.player import Player
from business_objects.game import Game
from random import randint

class DiceMode(GameMode):
    def play(self, player1 : Player, player2 : Player) :
        player1_roll = randint(1, 6)
        player2_roll = randint(1, 6)
        if player1_roll > player2_roll:
            winner = player1
        elif player1_roll < player2_roll:
            winner = player2
        else:
            winner = None
        return Game(player1, player2, "dice", winner, "A game of dice", datetime.now())
