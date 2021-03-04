#
# Author:       Chris Jacobs
# Date:         2/25/2021
# Assignment:   CS 162 Portfolio Assignment - Janggi
#
# Description:  A CLI version of Janggi, aka Korean Chess. Please view README.md and janggi_notes.txt
#               for further details.
#

from JanggiDisplay import JanggiDisplay         # optional import if/when we want to display
                                                # the CLI game board


class JanggiGame:
    """
    JanggiGame class is the controller class for the game. All methods the user uses to play the game are methods
    that are part of this class. The class also holds the fields that describe the state of the game and two
    objects that make up the bulk of the game - the game board and the individual players.
    """

    def __init__(self):

        self._game_state = "UNFINISHED"                             # Initialize the game state

        self._player_1 = Player("BLUE")                             # Initialize the players
        self._player_2 = Player("RED")
        self._current_player = None

        self._game_board = Board(self._player_1, self._player_2)    # Initialize the game board

        self.start_game()

    def start_game(self):
        """
        Starts the game by setting _player_1
        """
        self._current_player = self._player_1
        self._player_1.set_taking_turn(True)


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

    def is_in_check(self, player_color: str) -> bool:
        if player_color == "BLUE":
            return self._player_1.is_in_check()
        elif player_color == "RED":
            return self._player_2.is_in_check()
        else:
            print("ERROR: Invalid player color was passed to function JanggiGame.is_in_check()")

    def switch_turns(self):
        pass

    def refresh_game_state(self):
        pass

    def set_game_state(self, game_state: str):
        self._game_state = game_state

    def get_game_state(self) -> str:
        return self._game_state


class Player:

    def __init__(self, color: str):
        self._player_color = color

        self._in_check = False
        self._in_checkmate = False
        self._taking_turn = False

        self._player_pieces = []
        self.generate_pieces()

    def generate_pieces(self):
        """
        Generates the all necessary Piece objects to start the game and stores each Piece object
        in the list self._player_pieces
        """
        pass

    # Player Info Methods
    def get_player_color(self) -> str:
        """ Gets the player color """
        return self._player_color

    # Turn Functions
    def is_taking_turn(self) -> bool:
        """ Returns the bool value that represents if the player is currently taking a turn or not"""
        return self._taking_turn

    def set_taking_turn(self, turn_status: bool):
        """ Sets the turn status to either True (player currently taking turn) or False (turn is over)"""
        self._taking_turn = turn_status

    # Check Functions
    def is_in_check(self) -> bool:
        """ Returns whether the player is currently in check """
        return self._in_check

    def set_check_status(self, check_state: bool):
        self._in_check = check_state

    # Checkmate Functions
    def is_in_checkmate(self) -> bool:
        return self._in_checkmate

    def set_checkmate_status(self, checkmate_status: bool):
        self._in_checkmate = checkmate_status


class Board:
    """

    """

    def __init__(self, player1: Player, player2: Player):

        self._initial_red_positions = ()
        self._initial_blue_positions = ()

        self._red_palace_positions = ((4, 1), (5, 1), (6, 1),
                                      (4, 2), (5, 2), (6, 2),
                                      (4, 3), (5, 3), (6, 3))

        self._blue_palace_positions = ((4, 10), (5, 10), (6, 10),
                                       (4, 9), (5, 9), (6, 9),
                                       (4, 8), (5, 8), (6, 8))

        pass

    def populate_positions(self):
        pass

    def get_red_palace_positions(self):
        return self._red_palace_positions

    def get_blue_palace_positions(self):
        return self._blue_palace_positions

    def display_board(self):
        display = JanggiDisplay()
        display.draw(self.get_board_display_data())

    @staticmethod
    def get_board_display_data(self):
        return []

    @staticmethod
    def display_test_board(self):
        display = JanggiDisplay()
        display.test_board()


class Position(Board):
    """

    """

    def __init__(self, xy_position: tuple):
        super().__init__(xy_position)

        self._xy_pos = xy_position

        self._is_palace_position = self.check_if_palace_position()

    def check_if_palace_position(self):
        if self._xy_pos in self.get_blue_palace_positions():
            return True

        elif self._xy_pos in self.get_red_palace_positions():
            return True

        else:
            return False


class Piece:

    def __init__(self, player: Player, label: str):
        self._controlling_player = player
        self._label = label

        self._red_start_positions = ((), ())
        self._blue_start_positions = ((), ())

        self._in_palace = None
        self._confined_to_palace = None
        self._possible_moves = ()

        # unsure as to whether we will need these fields or not
        self._in_danger = None
        self._captured = None

    def get_player(self) -> Player:
        """ Returns the Player object that the piece is controlled by. """
        return self._controlling_player

    def get_label(self) -> str:
        """ Returns the string label that identifies the piece type. """
        return self._label

    def get_starting_positions(self) -> tuple:
        """
        Returns the starting positions for the piece, based on the piece's color ("BLUE" or "RED")
        :return: A tuple of tuples. If the piece is a General, the second tuple will be empty.
        """
        if self._controlling_player.get_player_color() == "BLUE":
            return self._blue_start_positions

        elif self._controlling_player.get_player_color() == "RED":
            return self._blue_start_positions
        else:
            raise Exception

    def


class General(Piece):

    def __init__(self, player, label):

        super().__init__(player, label)

        self._label = label

        # start positions in (x,y) notation
        self._red_start_positions = ((5, 2), ())
        self._blue_start_positions = ((5, 9), ())

        self._in_palace = True
        self._confined_to_palace = True
        self._possible_moves = ()


class Guard(Piece):

    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 3

        self._red_start_positions = ((4, 1), (6, 1))
        self._blue_start_positions = ((4, 10), (6, 10))

        self._in_palace = True
        self._confined_to_palace = True
        self._possible_moves = ()


class Chariot(Piece):

    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 13

        self._red_start_positions = []
        self._blue_start_positions = []

        # _in_palace will be important for other pieces as they move to and from the palace, because being in the
        # palace determines which moves are possible (i.e. for pieces where diagonal moves are not possible, being
        # in the palace allows for diagonal movement).

        self._in_palace = False

        # _confined_to_palace will be important for the General and for Guards - when checking an attempted move from
        # a Guard or General, we can check if the piece is confined to the palace, determine if the new_pos is a
        # Palace position, and invalidate the move right then and there
        self._confined_to_palace = False
        self._possible_moves = ()


class Horse(Piece):

    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 5

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

    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 3

        self._red_start_positions = []
        self._blue_start_positions = []

        self._in_palace = False
        self._confined_to_palace = False
        self._possible_moves = ()


class Cannon(Piece):

    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 7

        self._red_start_positions = []
        self._blue_start_positions = []

        self._in_palace = False
        self._confined_to_palace = False
        self._possible_moves = ()


class Soldier(Piece):

    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 2

        self._red_start_positions = []
        self._blue_start_positions = []

        self._in_palace = False
        self._confined_to_palace = False
        self._possible_moves = ()
