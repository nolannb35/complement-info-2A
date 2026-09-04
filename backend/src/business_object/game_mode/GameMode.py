from abc import abstractmethod

from ..game import Game


class GameMode:
    """Represents an abstract game with a single function called play."""

    @abstractmethod
    def play(p1, p2) -> Game:
        pass
