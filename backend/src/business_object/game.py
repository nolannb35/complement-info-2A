import datetime

from .player import Player


class Game:
    """Class reprensenting a game played
    Attributes:
        id_game (int): id of the game
        player_1 (Player): Player 1 of the game
        player_2 (Player): Player 2 of the game
        game_mode (str): Game mode of the game played
        winner (Player): Winner of the game
        description (str): Description of the game
        timestamp (datetime): Time of the game played
    """

    def __init__(
        self,
        player_1: Player,
        player_2: Player,
        game_mode: str,
        winner: Player or None,
        description: str,
        timestamp: datetime,
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        if game_mode in ["coinflip", "dice"]:
            self.game_mode = game_mode
        else:
            raise ValueError("Le jeux doit être coinflip ou game")
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

        self.id = None

    def __str__(self):
        return f"{self.game_mode} between {self.player_1} and {self.player_2}. The winner is {self.winner}."
