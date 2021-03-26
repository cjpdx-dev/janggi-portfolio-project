from JanggiExceptions import PieceException


class Piece:

    def __init__(self, player, label: str, start_pos: tuple):
        """
        """
        self._controlling_player = player
        self._label = label
        self._start_pos = start_pos

        self._confined_to_palace = None
        self._possible_moves = None

    def get_player(self):
        return self._controlling_player

    def get_label(self) -> str:
        return self._label

    def get_start_pos(self):
        return self._start_pos

    def is_confined_to_palace(self) -> bool:
        return self._confined_to_palace

    def get_possible_moves(self) -> dict:
        return self._possible_moves


class General(Piece):
    """
    """
    def __init__(self, player, label, start_pos):

        super().__init__(player, label, start_pos)

        self._label = label
        self._points = 100
        self._confined_to_palace = True

        self._possible_moves = {(1, 0): ((1, 0), ),
                                (0, 1): ((0, 1), ),
                                (-1, 0): ((-1, 0), ),
                                (0, -1): ((0, -1), )
                                }


class Guard(Piece):
    """
    """
    def __init__(self, player, label, start_pos):
        super().__init__(player, label, start_pos)

        self._label = label
        self._points = 3
        self._confined_to_palace = True

        self._possible_moves = {(1, 0): ((1, 0), ),
                                (0, 1): ((0, 1), ),
                                (-1, 0): ((-1, 0), ),
                                (0, -1): ((0, -1), )
                                }


class Chariot(Piece):
    """
    """
    def __init__(self, player, label, start_pos):
        super().__init__(player, label, start_pos)

        self._label = label
        self._points = 13
        self._confined_to_palace = False

        self._possible_moves = ((0, tuple(range(1, 10))),
                                (tuple((range(1, 9))), 0),
                                (0, tuple(range(-9, 0))),
                                (tuple((range(-8, -0))), 0)
                                )


class Horse(Piece):
    """
    """
    def __init__(self, player, label, start_pos):
        super().__init__(player, label, start_pos)

        self._label = label
        self._points = 5
        self._confined_to_palace = False

        self._possible_moves = {
            (-1, -2): ((0, -1), (-1, -1)),

            (1, -2): ((0, -1), (1, -1)),

            (2, -1): ((1, 0), (1, -1)),

            (2, 1): ((1, 0), (1, 1)),

            (1, 2): ((0, 1), (1, 1)),

            (-1, 2): ((0, 1), (-1, 1)),

            (-2, 1): ((-1, 0), (-1, 1)),

            (-2, -1): ((-1, 0), (-1, -1))
        }


class Elephant(Piece):
    """
    """
    def __init__(self, player, label, start_pos):
        super().__init__(player, label, start_pos)

        self._label = label
        self._points = 3
        self._confined_to_palace = False

        self._possible_moves = {(2, 3): ((0, 1), (1, 1), (1, 1)),
                                (-2, 3): ((0, 1), (-1, 1), (-1, 1)),
                                (2, -3): ((0, -1), (1, -1), (1, -1)),
                                (-2, -3): ((0, -1), (-1, -1), (-1, -1))
                                }


class Cannon(Piece):
    """
    """
    def __init__(self, player, label, start_pos):
        super().__init__(player, label, start_pos)

        self._label = label
        self._points = 7
        self._confined_to_palace = False

        self._possible_moves = ((0, tuple(range(1, 10))),
                                (tuple((range(1, 9))), 0),
                                (0, tuple(range(-9, 0))),
                                (tuple((range(-8, -0))), 0)
                                )


class Soldier(Piece):
    """
    """
    def __init__(self, player, label, start_pos):
        super().__init__(player, label, start_pos)

        self._label = label
        self._points = 2
        self._confined_to_palace = False

        if player.get_player_id() == "p1":
            self._possible_moves = {(1, 0): ((1, 0), ),
                                    (0, 1): ((0, 1), ),
                                    (-1, 0): ((-1, 0), )
                                    }

        elif player.get_player_id() == "p2":
            self._possible_moves = {(1, 0): ((1, 0), ),
                                    (0, -1): ((0, -1), ),
                                    (-1, 0): ((-1, 0), )
                                    }

        else:
            raise PieceException
