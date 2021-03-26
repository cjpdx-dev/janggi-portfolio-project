
from Piece import General, Guard, Chariot, Horse, Elephant, Cannon, Soldier
from JanggiExceptions import PlayerException


class Player:

    def __init__(self, player_id, name):

        self._player_id = player_id
        self._player_name = name

        self._in_check = False

        self._pieces = self.init_pieces()
        if self._pieces is None:
            raise PlayerException

    def init_pieces(self):

        pieces = None

        if self._player_id == "p1":
            pieces = [General(self, "ge", (5, 2)),
                      Guard(self, "gu", (4, 1)), Guard(self, "gu", (6, 1)),
                      Chariot(self, "ch", (1, 1)), Chariot(self, "ch", (9, 1)),
                      Horse(self, "hr", (3, 1)), Horse(self, "hr", (8, 1)),
                      Elephant(self, "el", (2, 1)), Elephant(self, "el", (7, 1)),
                      Cannon(self, "ca", (2, 3)), Cannon(self, "ca", (8, 3))]

            solider_start_positions = ((1, 4), (3, 4), (5, 4), (7, 4), (9, 4))
            for pos in solider_start_positions:
                pieces.append(Soldier(self, "so", pos))

        if self._player_id == "p2":
            pieces = [General(self, "ge", (5, 9)),
                      Guard(self, "gu", (4, 10)), Guard(self, "gu", (6, 10)),
                      Chariot(self, "ch", (1, 10)), Chariot(self, "ch", (9, 10)),
                      Horse(self, "hr", (3, 10)), Horse(self, "hr", (8, 10)),
                      Elephant(self, "el", (2, 10)), Elephant(self, "el", (7, 10)),
                      Cannon(self, "ca", (2, 8)), Cannon(self, "ca", (8, 8))]

            solider_start_positions = ((1, 7), (3, 7), (5, 7), (7, 7), (9, 7))
            for pos in solider_start_positions:
                pieces.append(Soldier(self, "so", pos))

        return pieces

    def get_pieces(self):
        return self._pieces

    def get_player_name(self):
        return self._player_name

    def get_player_id(self):
        return self._player_id
