from requests import request
from src.business_object.game import Game


def get_games(self) -> list[Game]:
    url = "http://0.0.0.0.5000/player"
    r = request("GET", url)
    r.raise_for_status()

    json = r.json()

    game_list = []
    for game_dict in json:
        game = Game(
            player1=game_dict(["player_list"][0]),
            player2=game_dict(["player_list"][1]),
            game_mode=game_dict["mode_type"],
            
        )
        game_list.append(game)
    return json
