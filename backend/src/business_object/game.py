from .player import Player
from datetime import datetime

class Game :                #sould be named GameResult
    def __init__(
        self,
        player1 : Player,
        player2 : Player,
        game_mode : str,
        winner : Player,
        description : str,
        timestamp : datetime
    ):
        self.id = None
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp
    
    def __str__(self):
        return f"{self.game_mode} between {self.player1} and {self.player2}. Winner: {self.winner}"
    


