from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log
from utils.singleton import Singleton

from .business_object.game.py import Game

logger = get_logger(__name__)


class GameDao(metaclass=Singleton):
    def create(self, game) -> bool:
        """Create a game in the database.
        Args:
            Game to create
        Returns:
            True if creation is successful, False otherwise
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO game(id_player1, id_player2, game_mode, id_winner, detail) VALUES "
                        "(%(id_player1)s, %(id_player2)s, %(game_mode)s, %(id_winner)s,  %(detail)s) "
                        "RETURNING id_game;",
                        {
                            "player1": game.id_player1,
                            "player2": game.id_player2,
                            "game_mode": game.game_mode,
                            "winner": game.winner,
                            "detail": game.detail
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        created = False
        if res:
            game.id_game = res["id_game"]
            created = True

        return created

    def find_by_id(self, id_player: int) -> Game:
        """Find a game by their id.
        Args:
            id_game (int): The ID of the game to find
        Returns:
            Game matching the given id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                            "
                        "  FROM game                       "
                        " WHERE id_game = %(id_game)s;   ",
                        {"id_game": id_game},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        game = None

        if res:
            game = Game(
                player1=res["id_player1"],
                player2=res["id_player2"],
                winner=res["id_winner"],
                game_mode=res["game_mode"],
                description=res["detail"],
                game_id=res["game_id"],
                timestamp=res["timestamp"],
            )

        return game
