import os

import requests
from src.business_object.game import Game

base_url = os.environ("BACKEND_URL")


class GameClient:
    def get_games(self) -> list[Game]:
        list_game = []
        url = base_url + "/player"
        r = requests.get(url)
        r.raise_for_status()
        json: list[dict] = r.json()
        for i in range(len(json)):
            id = json[i]["id"]
            player_list = json[i]["player_list"]
            location_name = json[i]["location_name"]
            duration_seconds = json[i]["duration_seconds"]
            mode_type = json[i]["mode_type"]
            list_game.append(Game(id, player_list, location_name, duration_seconds, mode_type))
        return list_game
