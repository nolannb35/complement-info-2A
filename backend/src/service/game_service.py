from fastapi import HTTPException

from dao.player_dao import PlayerDao
from utils.log_utils import log

from ..business_object.game_mode.GameModeFactory import GameModeFactory


class GameService:
    """Service that manages games."""

    @log
    def play(self, id_player: int, id_opponent: int, game_mode: str, **kwargs):
        """Executes a single round of a coin-flip game between two players.
        Args:
            id_player (int): The unique identifier of the first player.
            id_opponent (int): The unique identifier of the opponent.
            choice (str, optional): The player's choice ('heads' or 'tails'). Defaults to "heads".
        Returns:
            dict: A dictionary containing the match details and new elo
        Raises:
            HTTPException: 400 if the two players are the same.
            HTTPException: 404 if one or both players are not found in the database.
        """
        if id_player == id_opponent:
            raise HTTPException(status_code=400, detail="Two different players required")

        player1 = PlayerDao().find_by_id(id_player)
        player2 = PlayerDao().find_by_id(id_opponent)

        if not player1 or not player2:
            raise HTTPException(status_code=404, detail="Player not found")

        GameModeFactory.get_mode(game_mode).play(player1, player2)

        winner = player1 if result == choice else player2

        self.update_player_ratings(player1, player2, winner)

        PlayerDao().update(player1)
        PlayerDao().update(player2)

        return {
            "player1": player1.username,
            "player2": player2.username,
            "description": result,
            "winner": winner.username,
            "new_elo1": player1.elo,
            "new_elo2": player2.elo,
        }
