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

from JanggiExceptions import *


class JanggiGame:
    """
    JanggiGame class is the controller class for the game. All methods the user uses to play the game are methods
    that are part of this class. The class also holds the fields that describe the state of the game and two
    objects that make up the bulk of the game - the game board and the individual players.
    """
    def __init__(self):
        """ Initializes the JanggiGame object """

        self._game_state = None                                     # Initialize the game state

        self._player_1 = Player("BLUE")                             # Initialize the players
        self._player_2 = Player("RED")
        self._current_player = None

        self._game_board = Board(self._player_1, self._player_2)    # Initialize the game board
        self._display = JanggiDisplay()
        self.start_game()

    def start_game(self):
        """
        Starts the game by setting Player 1 as the current player and setting the game state
        as "UNFINISHED"
        """
        self._game_state = "UNFINISHED"
        self._current_player = self._player_1

        # Not sure if we need to have a player object knowing that it is the current player
        # but it may be helpful later when we are doing movement validation
        self._player_1.set_taking_turn(True)
        # self.display_board()

    def make_move(self, old_pos: str, new_pos: str) -> bool:
        """
        Makes a move, first by validating the old position and then the new position. Gets
        the Piece at the old position and checks if it belongs to the current_player. Then checks
        the new position to see if it is either empty or occupied by the opposing player. Finally,
        """
        pass

    def convert_algebraic_to_xy(self) -> tuple:
        """
        Converts the user's algebraic notation for representing piece position into (x,y) coordinate
        notation that the Board object can parse.
        """
        pass

    def check_for_valid_coordinates(self) -> bool:
        """
        Checks that the converted (x,y) notation is valid (i.e. the position exists on the board).
        """
        pass

    def refresh_game_state(self):
        """
        This method determines if the game state has changed by calling _is_in_check. If is_in_check
        returns true, then we call look_for_checkmate
        """
        pass

    def is_in_check(self, player_color: str) -> bool:
        """
        Accesses the current player's data to determine if the player is in check and returns True
        or False accordingly. This method is user-facing so it must handle invalid input from the user.
        :param player_color: (str) "BLUE" or "RED"
        :return: bool
        """
        if player_color == "BLUE":
            return self._player_1.is_in_check()
        elif player_color == "RED":
            return self._player_2.is_in_check()
        else:
            print("ERROR: Invalid player color was passed to function JanggiGame.is_in_check()")

    def look_for_checkmate(self):
        """
        his function is called by refresh_game_status if next player is found to be in checkmate.
        Checkmate is found by iterating through each piece and seeing
        """

    def set_game_state(self, game_state: str):
        """
        Sets the game state to the string argument passed to the function. Does not need to
        screen for an invalid string, because this function is only called by refresh_game_state()
        which only passes valid strings.
        :param game_state:
        :return:
        """
        self._game_state = game_state

    def get_game_state(self) -> str:
        """
        Returns the string representation of the game state.
        :return: str - "UNFINISHED", "RED_WON", or "BLUE_WON"
        """
        return self._game_state

    def get_current_player(self):
        """ Returns the Player object currently taking their turn """
        return self._current_player

    def get_next_player(self):
        """ Returns the Player object whose turn is next"""
        if self._current_player == self._player_1:
            return self._player_2
        elif self._current_player == self._player_2:
            return self._player_1
        else:
            print("ERROR: current player is not initialized. Returning None.")

    def switch_turns(self):
        """
        Swaps which player is designated as the current player, and alters both Player's
        set_taking_turn field accordingly.
        """
        if self._current_player is self._player_1:
            self._player_1.set_taking_turn(False)
            self._player_2.set_taking_turn(True)
            self._current_player = self._player_2

        elif self._current_player is self._player_2:
            self._player_2.set_taking_turn(False)
            self._player_1.set_taking_turn(True)
            self._current_player = self._player_1

        else:
            print("ERROR: Attempted to switch turns but _current_player is set to None")

    # Display Functions

    def display_board(self):
        self._display.draw(self.get_drawable_board_data())

    def get_drawable_board_data(self):
        drawable_data = [[str(self._player_2.get_points())]]

        for y in range(1, 11):
            drawable_row = []

            for x in range(1, 10):
                position = self._game_board.get_position((x, y))

                if position.get_current_piece() is not None:
                    piece_label = position.get_current_piece().get_label()
                    controlling_player = position.get_current_piece().get_player()

                    if controlling_player is self._current_player:
                        piece_label = piece_label.upper()

                    drawable_row.append(piece_label)

                else:
                    drawable_row.append("**")

            drawable_data.append(drawable_row)

        drawable_data.append([str(self._player_1.get_points())])
        return drawable_data

    # Methods for Tests
    def get_board(self):
        """ For testing only """
        return self._game_board


class Player:
    """
    This class represents the Player. A Player is represented by one of two colors (RED or BLUE).
    A player can be in or out of check, in or out of checkmate, and is either taking its turn or
    not taking its turn. The primary data structure within a Player is stored in the list
    called _player_pieces. Upon initialization of a player, all the Piece objects needed to start
    the game are generated and stored in this data structure.
    """

    def __init__(self, color: str):
        """ Initializes the Player object """

        self._player_color = color

        self._in_check = False
        self._in_checkmate = False
        self._taking_turn = False

        self._points = 0

        self._player_pieces = []
        self.generate_pieces()

    # Piece methods
    def generate_pieces(self):
        """
        Generates the all necessary Piece objects to start the game and stores each Piece object
        in the list self._player_pieces.
        """
        pieces = [General(self, "ge"), Guard(self, "gu"), Guard(self, "gu"), Chariot(self, "ch"),
                  Chariot(self, "ch"), Horse(self, "hr"), Horse(self, "hr"), Elephant(self, "el"),
                  Elephant(self, "el"), Cannon(self, "ca"), Cannon(self, "ca")]

        for i in range(0, 5):
            pieces.append(Soldier(self, "so"))

        for piece in pieces:
            self._player_pieces.append(piece)

    def get_all_pieces(self) -> list:
        """
        Returns a list of all the player's pieces - this list does not represent which pieces
        are still in play, just a list of all of a player's pieces that the player starts with.
        """
        return self._player_pieces

    # Player Info Methods
    def get_player_color(self) -> str:
        """
        Returns the player's color (RED or BLUE)
        """
        return self._player_color

    def get_points(self) -> int:
        """
        Returns the number of points the player has accumulated through piece capturing.
        This is not a graded feature - it is a future feature I'd like to implement.
        """
        return self._points

    # Turn Methods
    def is_taking_turn(self) -> bool:
        """ Returns the bool value that represents if the player is currently taking a turn or not"""
        return self._taking_turn

    def set_taking_turn(self, turn_status: bool):
        """ Sets the turn status to either True (player currently taking turn) or False (turn is over)"""
        self._taking_turn = turn_status

    # "In Check" Methods
    def is_in_check(self) -> bool:
        """ Returns whether the player is currently in check """
        return self._in_check

    def set_check_status(self, check_state: bool):
        """ Sets the _in_check state to True or False"""
        self._in_check = check_state

    # Checkmate Functions
    def is_in_checkmate(self) -> bool:
        """ Returns the current state of self._in_checkmate """
        return self._in_checkmate

    def set_checkmate_status(self, checkmate_status: bool):
        """ Sets the current state of self._in_checkmate """
        self._in_checkmate = checkmate_status


class Board:
    """
    This class represents the game board of a Janggi game. It accepts two Player objects
    as arguments. It then creates an empty board, and places pieces on that board.
    """

    def __init__(self, player1: Player, player2: Player):
        """ Initializes the Board object """
        self._player1 = player1
        self._player2 = player2

        self._board = {}
        self.initialize_empty_board()
        self.place_player_pieces()

    def initialize_empty_board(self):
        """ Initializes an empty board using a dictionary and populates that dictionary with Position
        objects, such that a generated xy coordinate represents the key and the Position object represents
        that key's value.
        """
        for y in range(1, 11):
            for x in range(1, 10):
                self._board[(x, y)] = Position((x, y))

        # print(self._board)

    def place_player_pieces(self):
        """
        For each player, gets all pieces assigned to that player by calling Player.get_all_pieces().
        Then assigns them to the correct Position object on the Board, based on that Piece's data and
        the color of the controlling player.
        """
        players = [self._player1, self._player2]

        for player in players:
            positions_placed = []
            player_pieces = player.get_all_pieces()
            for piece in player_pieces:
                start_coordinates = piece.get_starting_coordinates()
                for xy_pos in start_coordinates:
                    if xy_pos is not None and xy_pos not in positions_placed:
                        self._board[xy_pos].assign_piece_to_position(piece)
                        positions_placed.append(xy_pos)

    @staticmethod
    def get_blue_palace_coordinates() -> tuple:
        """
        Static method that returns the (x,y) coordinates of the Blue palace positions. Data structure returned
        is a tuple of tuples.
        """

        # we eventually can change this data struct to a dict so that we can use it
        # to look up valid piece movements within the palace.
        blue_palace_positions = ((4, 1), (5, 1), (6, 1),
                                 (4, 2), (5, 2), (6, 2),
                                 (4, 3), (5, 3), (6, 3))

        return blue_palace_positions

    @staticmethod
    def get_red_palace_coordinates() -> tuple:
        """
        Static method that returns the (x,y) coordinates of the Red palace positions. Data structure returned
        is a tuple of tuples.
        """
        # we eventually can change this data struct to a dict so that we can use it
        # to look up valid piece movements within the palace.
        red_palace_positions = ((4, 10), (5, 10), (6, 10),
                                (4, 9), (5, 9), (6, 9),
                                (4, 8), (5, 8), (6, 8))

        return red_palace_positions

    def get_position(self, xy_coord: tuple):
        """
        Checks board positions and returns a Position object if a matching
        xy_coord key value is found. Otherwise, returns None.
        """
        if xy_coord in self._board:
            return self._board[xy_coord]
        else:
            return None


class Piece:
    """
    A Piece class represents a piece object - in practice all Piece objects will exist as
    one of the child classes associated with this parent Piece class. Each piece
    will have be associated with a controlling player, possess a label, and have fields
    determining its possible start positions, move rules, whether it is in or confined to
    the palace, as well as additional fields like _in_danger or _captured.
    """

    def __init__(self, player: Player, label: str):
        """ Initializes the Piece object """
        self._controlling_player = player
        self._label = label

        self._red_start_coordinates = ()
        self._blue_start_coordinates = ()

        self._in_palace = None
        self._confined_to_palace = None
        self._possible_moves = ()

        # unsure as to whether these fields will be useful later
        self._in_danger = None
        self._captured = None
        #

    def get_player(self) -> Player:
        """ Returns the Player object that the piece is controlled by. """
        return self._controlling_player

    def get_label(self) -> str:
        """ Returns the string label that identifies the piece type. """
        return self._label

    def get_starting_coordinates(self) -> tuple:
        """
        Returns the starting positions for the piece, based on the piece's color ("BLUE" or "RED")
        :return: A tuple of tuples. If the piece is a General, the second tuple will be empty.
        """
        if self._controlling_player.get_player_color() == "BLUE":
            return self._blue_start_coordinates
        elif self._controlling_player.get_player_color() == "RED":
            return self._red_start_coordinates
        else:
            print("No Player")

    def get_possible_moves(self):
        """ Returns the possible movements for the Piece """
        return self._possible_moves
        pass


class General(Piece):
    """ A child class of Piece that represents the General """

    def __init__(self, player, label):

        super().__init__(player, label)

        self._label = label

        # start positions in (x,y) notation
        # tuple(tuple(list('abc')))

        self._red_start_coordinates = ((5, 2), None)
        self._blue_start_coordinates = ((5, 9), None)

        self._in_palace = True
        self._confined_to_palace = True
        self._possible_moves = ()


class Guard(Piece):
    """ A child class of Piece that represents a Guard """
    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 3

        self._red_start_coordinates = ((4, 1), (6, 1))
        self._blue_start_coordinates = ((4, 10), (6, 10))

        self._in_palace = True
        self._confined_to_palace = True
        self._possible_moves = ()


class Chariot(Piece):
    """ A child class of Piece that represents a Chariot """
    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 13

        self._red_start_coordinates = ((1, 1), (9, 1))
        self._blue_start_coordinates = ((1, 10), (9, 10))

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
    """ A child class of Piece that represents a Horse """
    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 5

        self._red_start_coordinates = ((3, 1), (8, 1))
        self._blue_start_coordinates = ((3, 10), (8, 10))

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
    """ A child class of piece that represents an Elephant """
    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 3

        self._red_start_coordinates = ((2, 1), (7, 1))
        self._blue_start_coordinates = ((2, 10), (7, 10))

        self._in_palace = False
        self._confined_to_palace = False
        self._possible_moves = ()


class Cannon(Piece):
    """ A child class of Piece that represents a Cannon """
    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 7

        self._red_start_coordinates = ((2, 3), (8, 3))
        self._blue_start_coordinates = ((2, 8), (8, 8))

        self._in_palace = False
        self._confined_to_palace = False
        self._possible_moves = ()


class Soldier(Piece):
    """ A child class of Piece that represents a Soldier """
    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 2

        self._red_start_coordinates = ((1, 4), (3, 4), (5, 4), (7, 4), (9, 4))
        self._blue_start_coordinates = ((1, 7), (3, 7), (5, 7), (7, 7), (9, 7))

        self._in_palace = False
        self._confined_to_palace = False
        self._possible_moves = ()


class Position:
    """
    This class represents a position within the board. The Position accepts an (x,y) as its argument
    and this field is the main identifying field for the Position. The Position also has a field to store
    a Player object as its controlling player. If the Position is empty, that field is None. If a field currently
    has a Piece, that Piece object is stored in the _current_piece field.
    """

    def __init__(self, xy_position: tuple):
        """ Initializes the Position object """

        self._xy_pos = xy_position
        self._is_palace_position = self.check_if_palace_position()

        self._current_piece = None

    def check_if_palace_position(self):
        """
        Calls the static method Board.get_color_palace_coordinates() to determine if the Position's
        xy_pos can be found in that data structure. Returns True or False and sets the Position's
        self._is_palace_position accordingly.
        """
        if self._xy_pos in Board.get_blue_palace_coordinates():
            return True
        elif self._xy_pos in Board.get_red_palace_coordinates():
            return True
        else:
            return False

    def get_current_piece(self) -> Piece:
        """
        Returns the current Piece object assigned to the position. If the position does not have
        a piece, returns None
        """
        return self._current_piece

    def get_position_location(self) -> tuple:
        """ Returns the x,y location of the position """
        return self._xy_pos

    def assign_piece_to_position(self, piece: Piece):
        """
        Assigns a piece to an empty position. If the position is already filled, raise Exception.
        If the player removing the Piece is not its controlling player, return raise Exception.
        """
        self._current_piece = piece

    def remove_piece_from_position(self, controlling_player: Player):
        """
        Removes a piece from a position occupied by a piece by setting _controlling_player to None and
        _current_piece to None. If the position does not have a piece present, return False. If the player removing
        the Piece is not its controlling player, return False. Otherwise, return True.
        """


game = JanggiGame()
gameboard = game.get_board()
game.display_board()

# print("testing board:")
# for y in range(1, 11):
#     for x in range(1, 10):
#         position = gameboard.get_position((x, y))
#         print(position)
#         print(position.get_position_location())
#         print(position.get_current_piece())
#         if position.get_current_piece() is not None:
#             print(position.get_current_piece().get_player().get_player_color())
#         print()
