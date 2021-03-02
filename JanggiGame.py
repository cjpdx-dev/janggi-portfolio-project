#
# Author:       Chris Jacobs
# Date:         2/25/2021
# Assignment:   CS 162 Portfolio Assignment - Janggi
#
# Description:  A CLI version of Janggi, aka Korean Chess. Please view README.md and janggi_notes.txt
#               for further details.
#

from JanggiDisplay import JanggiDisplay


class JanggiGame:
    """
    JanggiGame class is the controller class for the game. All methods the user uses to play the game are methods
    that are part of this class. The class also holds the fields that describe the state of the game and two
    objects that make up the bulk of the game - the game board and the individual players.
    """

    def __init__(self):

        self._game_state = "UNFINISHED"                             # Initialize the game state

        self._player_1 = Player("BLUE")                              # Initialize the players
        self._player_2 = Player("RED")

        self._player_1.set_taking_turn(True)                        # Assign _player_1 to be the current player
        self._current_player = self._player_1

        self._game_board = Board(self._player_1, self._player_2)    # Initialize the game board

    def make_move(self, old_pos: str, new_pos: str) -> bool:
        """
        The process for this method is as follows:
            1. Confirm that the old_pos is an actual valid space on the board.
            2. Confirm that the move is acting on a position (old_pos) that the current player controls.
            3. Confirm that the move is valid. This requires the following sub-steps:
                a. Is the new_pos possible based on the "move rules" of the piece?
                b. Are there any pieces
        """
        pass

    def refresh_game_state(self):
        pass

    def is_in_check(self, player_color: str) -> bool:
        pass

    def switch_turns(self):
        pass

    def set_game_state(self, game_state):
        self._game_state = game_state

    def get_game_state(self):
        return self._game_state


class Player:

    def __init__(self, color):
        self._player_color = color

        self._in_check = False
        self._in_checkmate = False
        self._taking_turn = False

        self._player_pieces = []

    # Player Name Methods
    def get_player_color(self):
        return self._player_color

    # Turn Position Methods
    def is_taking_turn(self):
        return self._taking_turn

    def set_taking_turn(self, turn_status):
        self._taking_turn = turn_status

    # In Check/Out of Check Methods
    def is_in_check(self):
        return self._in_check

    def set_in_check(self):
        self._in_check = True

    def set_out_of_check(self):
        self._in_check = False


class Board:

    def __init__(self, player1: Player, player2: Player):

        # rows 1-4 belong to red
        self._initial_red_positions = (0, 0, )


        # rows 10-7 belong to blue

        pass

    def populate_positions(self):
        pass


class Position:

    def __init__(self, position_label):
        self._pos_label = position_label


class Piece:

    def __init__(self, player):
        self._player = player


class General(Piece):

    def __init__(self, player):

        super().__init__(player)

        self._long_label = "General"
        self._short_label = "GE"

        self._red_start_positions = ["e2"]
        self._blue_start_positions = ["e9"]

        self._in_palace = True
        self._confined_to_palace = True


class Guard(Piece):

    def __init__(self, player):
        super().__init__(player)

        self._long_label = "Guard"
        self._short_label = "GU"

        self._red_start_positions = ((3, 0), (5, 0))
        self._blue_start_positions = ("d10", "f10")

        self._in_palace = True
        self._confined_to_palace = True


class Chariot(Piece):

    def __init__(self, player):
        super().__init__(player)

        self._long_label = ""
        self._short_label = ""

        self._red_start_positions = []
        self._blue_start_positions = []

        self._in_palace = False
        self._confined_to_palace = False


class Horse(Piece):

    def __init__(self, player):
        super().__init__(player)

        self._long_label = ""
        self._short_label = ""

        self._red_start_positions = []
        self._blue_start_positions = []

        self._in_palace = False
        self._confined_to_palace = False

        # self._possible_moves
        #
        # Represented as a dict (tuple: tuple of tuples)
        # The key is equal to cur_pos [col, row] - new_pos [col, row]
        # Example for a horse moving from c3 to d5: c3 -> [2, 2], d5 -> [3,4], [2,2] - [3,4] = [-1, -2]
        #
        # The value is the "move sequence" that is valid from the new_pos to the old_os for that corresponding
        # key. the rules for a horse are that it can move 1 space orthogonally and 1 diagonally. So to do that
        # with the above key (-1, -2), the move sequence would be ((-1, -1), (0, -1)). This represents the following
        # sequence of steps: x - 1 then y - 1 (arrived at a position, so check for piece here), then x - 0 and y - 1
        # (we arrive at the cur_pos).
        #
        # Important to remember that these values are tracing a path from the new_pos back to the cur_pos.
        # Also important to remember that we are operating in (X,Y) coordinate system - the first value in
        # any point notation, whether we are representing a fixed point or the delta of that point, is always
        # in (X, Y) notation.
        #

        self._possible_moves = {
            (-1, -2): ((-1, -1), (0, -1)),

            (1, -2): ((1, -1), (0, -1)),

            (2, -1): ((1, -1), (1, 0)),

            (2, 1): ((1, 1), (1, 0)),

            (1, 2): ((1, 1), (0, 1)),

            (-1, 2): ((-1, 1), (0, 1)),

            (-2, 1): ((-1, 1), (-1, 0)),

            (-2, -1): ((-1, -1), (-1, 0))
        }


class Elephant(Piece):

    def __init__(self, player):
        super().__init__(player)

        self._long_label = ""
        self._short_label = ""

        self._red_start_positions = []
        self._blue_start_positions = []

        self._in_palace = False
        self._confined_to_palace = False



class Cannon(Piece):

    def __init__(self):
        super().__init__()

        self._long_label = ""
        self._short_label = ""

        self._red_start_positions = []
        self._blue_start_positions = []

        self._in_palace = False
        self._confined_to_palace = False


class Soldier(Piece):

    def __init__(self):
        super().__init__()

        self._long_label = ""
        self._short_label = ""

        self._red_start_positions = []
        self._blue_start_positions = []

        self._in_palace = False
        self._confined_to_palace = False


display = JanggiDisplay()

test_placements = ["100"], \
                 ["CH", "EL", "HR", "GU", "**", "GU", "EL", "HR", "CH"],\
                 ["**", "**", "**", "**", "GE", "**", "**", "**", "**"],\
                 ["**", "CA", "**", "**", "**", "**", "**", "CA", "**"],\
                 ["SO", "**", "SO", "**", "SO", "**", "SO", "**", "SO"],\
                 ["**", "**", "**", "**", "**", "**", "**", "**", "**"],\
                 ["**", "**", "**", "**", "**", "**", "**", "**", "**"],\
                 ["SO", "**", "SO", "**", "SO", "**", "SO", "**", "SO"],\
                 ["**", "CA", "**", "**", "**", "**", "**", "CA", "**"],\
                 ["**", "**", "**", "**", "GE", "**", "**", "**", "**"],\
                 ["CH", "EL", "HR", "GU", "**", "GU", "EL", "HR", "CH"],\
                 ["100"]

display.display_board(test_placements)









