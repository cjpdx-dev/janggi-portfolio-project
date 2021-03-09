#
# Author:       Chris Jacobs
# Date:         2/25/2021
# Assignment:   CS 162 Portfolio Assignment - Janggi
#
# Description:  A CLI version of Janggi, aka Korean Chess. Please view README.md and janggi_notes.txt
#               for further details.
#

# optional import if/when we want to display # the CLI game board
from JanggiDisplay import JanggiDisplay
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

    def make_move(self, current_pos: str, new_pos: str) -> bool:
        """
        Makes a move, first by validating the old position and then the new position. Gets
        the Piece at the old position and checks if it belongs to the current_player. Then checks
        the new position to see if it is either empty or occupied by the opposing player. Finally,
        """
        input_positions = (current_pos.lower(), new_pos.lower())
        print(input_positions)

        if self.validate_position_existence(input_positions) is False:
            return False
        else:
            xy_move = self.convert_algebraic_to_xy((current_pos, new_pos))

        move_is_valid = self._game_board.check_move(xy_move)
        # print(xy_move)
        # # test code
        # old_position: Position = self._game_board.get_position(xy_move[0])
        # new_position: Position = self._game_board.get_position(xy_move[1])
        # print(new_position.get_current_piece().get_label())
        # print(new_position.get_current_piece().get_player().get_player_color())

    @staticmethod
    def validate_position_existence(input_positions: tuple) -> bool:
        """
        Checks that the converted (x,y) notation is valid (i.e. the position exists on the board).
        Does NOT check if the made cannot be made of other reasons.
        """
        if input_positions[0] == input_positions[1]:
            print("ERROR: The given positions were identical.")
            return False

        for position in input_positions:
            if len(position) not in range(2, 4):
                print("ERROR: Invalid position format.")
                return False

            if ord(position[0]) not in range(ord("a"), ord("i")+1):
                print("ERROR: first character in position be a letter in the range of \"a\" through \"i\"")
                return False

            row_string = None
            try:
                if len(position) == 2:
                    row_string = position[1]

                if len(position) == 3:
                    row_string = position[1:3]

                row_num = int(row_string)

                if row_num not in range(1, 11):
                    print("ERROR: Invalid range for row number. Row number must be between 1 and 10.")
                    return False

            except:
                print("ERROR: Row notation was invalid. Row must be a number between 1 and 10.")

        return True

    @staticmethod
    def convert_algebraic_to_xy(algebraic_positions: tuple) -> tuple:
        """
        Converts the user's algebraic notation for representing piece position into (x,y) coordinate
        notation that the Board object can parse.
        """
        positions_list = []
        for position in algebraic_positions:
            column_num = None
            row_num = None
            try:
                column_string = position[0]
                column_ascii_num = ord(column_string)
                column_num = column_ascii_num - 96
                print("column num: ", column_num)

                if len(position) == 2:
                    row_num = int(position[1])
                if len(position) == 3:
                    row_num = int(position[1:3])

            except IndexError:
                "IndexError in JanggiGame.convert_algebraic_to_xy()"
            except ValueError:
                "ValueError in JanggiGame.convert_algebraic_to_xy()"
            except Exception as e:
                print("An unhandled exception occurred: ")
                print(e)

            positions_list.append([column_num, row_num])

        xy_move_notation = (tuple(positions_list[0]), tuple(positions_list[1]))
        return xy_move_notation

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
        """
        if player_color == "BLUE":
            return self._player_1.is_in_check()
        elif player_color == "RED":
            return self._player_2.is_in_check()
        else:
            print("ERROR: Invalid player color was passed to function JanggiGame.is_in_check()")

    def look_for_checkmate(self):
        """
        This function is called by refresh_game_status if next player is found to be in checkmate.
        Checkmate is found by iterating through each piece and seeing
        """

    def set_game_state(self, game_state: str):
        """
        Sets the game state to the string argument passed to the function. Does not need to
        screen for an invalid string, because this function is only called by refresh_game_state()
        which only passes valid strings.
        """
        self._game_state = game_state

    def get_game_state(self) -> str:
        """
        Returns the string representation of the game state.
        :return str: "UNFINISHED", "RED_WON", "BLUE_WON"
        """
        return self._game_state

    def get_current_player(self):
        """
        Returns the Player object currently taking their turn
        """
        return self._current_player

    def get_next_player(self):
        """
        Returns the Player object whose turn is next
        """
        if self._current_player == self._player_1:
            return self._player_2
        elif self._current_player == self._player_2:
            return self._player_1
        else:
            print("ERROR: A current player was not initialized. Returning None.")

    def switch_turns(self):
        """
        Swaps which player is designated as the current player, and alters both Player's
        set_taking_turn field accordingly.
        """
        if self._current_player is self._player_1:
            self._player_1.set_as_current_player(False)
            self._player_2.set_as_current_player(True)
            self._current_player = self._player_2

        elif self._current_player is self._player_2:
            self._player_2.set_as_current_player(False)
            self._player_1.set_as_current_player(True)
            self._current_player = self._player_1

        else:
            print("ERROR: Attempted to switch turns but _current_player is set to None")

    # Display Functions
    def display_board(self):
        """
        Draws a CLI representation of the game board.
        """
        self._display.draw(self.get_drawable_board_data())

    def get_drawable_board_data(self):
        """
        Iterates through each position of the game board and returns a 2d list
        of positions and their pieces. ** indicates the absence of a Piece.
        """
        player_2_label = self._player_2.get_player_color()
        if self._current_player != self._player_2:
            player_2_label = player_2_label.lower()
        drawable_data = [[player_2_label, str(self._player_2.get_points())]]

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

        player_1_label = self._player_1.get_player_color()
        if self._current_player != self._player_1:
            player_1_label = player_1_label.lower()
        drawable_data.append([player_1_label, str(self._player_1.get_points())])
        return drawable_data

    # Test Methods
    def get_board(self):
        """ For testing only. """
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
        """
        Initializes the Player object. Accepts a string that represents the player color, which
        is a unique identifier for the player.
        """

        self._player_color = color
        self._points = 0

        self._player_pieces = []

        self._in_check = False
        self._in_checkmate = False
        self._is_current_player = False

        self.generate_pieces()

    def generate_pieces(self):
        """
        Generates all necessary Piece objects for initial game state. Stores these Piece objects
        in a list that is part of the Player object's data.
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

    def get_player_color(self) -> str:
        """
        Returns the player's color (RED or BLUE)
        """
        return self._player_color

    def is_taking_turn(self) -> bool:
        """
        Returns the bool value that represents if the player is currently taking a turn or not
        """
        return self._is_current_player

    def set_taking_turn(self, turn_status: bool):
        """
        Sets the turn status to either True (player currently taking turn) or False (turn is over)
        """
        self._is_current_player = turn_status

    def is_in_check(self) -> bool:
        """
        Returns the Player's "in check" state
        """
        return self._in_check

    def set_check_status(self, check_state: bool):
        """
        Sets the "in check" state of the Player to True or False
        """
        self._in_check = check_state

    def is_in_checkmate(self) -> bool:
        """
        Returns the Player's "in checkmate" state.
        """
        return self._in_checkmate

    def set_checkmate_status(self, checkmate_status: bool):
        """
        Sets the Player's "in checkmate" state to True or False
        """
        self._in_checkmate = checkmate_status

    def get_points(self) -> int:
        """
        Returns the number of points the player has accumulated through piece capturing.
        This is not a graded feature - it is a future feature I'd like to implement.
        """
        return self._points


class Board:
    """
    This class represents the game board of a Janggi game. It accepts two Player objects
    as arguments. It then creates an empty board, and places pieces on that board.
    """

    def __init__(self, player1: Player, player2: Player):
        """
        Initializes the Board object. Accepts two Player objects as arguments.
        """
        self._player1 = player1
        self._player2 = player2

        self._board = {}

        # helper methods
        self.initialize_empty_board()
        self.place_player_pieces()

    def initialize_empty_board(self):
        """
        Initializes an empty board using a dictionary and populates that dictionary with Position
        objects, such that a generated xy coordinate represents the key and the Position object
        represents that key's value.
        """
        for y in range(1, 11):
            for x in range(1, 10):
                self._board[(x, y)] = Position((x, y))

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
                        self._board[xy_pos].assign_piece_to_empty_position(piece)
                        positions_placed.append(xy_pos)

    def get_position(self, xy_coord: tuple):
        """
        Checks board positions and returns a Position object if a matching xy_coord key value is found.
        Otherwise, returns None.
        """
        if xy_coord in self._board:
            return self._board[xy_coord]
        else:
            return None

    def check_move(self, xy_coord: tuple) -> bool:
        """
        Determine if the move is valid based on piece placement and piece movement ability.
        Accepts a tuple that represents (current_position, new_position). These positions have already
        been verified to exist on the board before this method can be called. The move itself is validated
        by this method. Returns True if the move is shown to be possible, otherwise returns False.
        """
        move_is_a_reposition = False
        movement_rules = None

        move_is_a_capture = False
        capture_rules = None

        # Check the current position
        current_pos: Position = self.get_position(xy_coord[0])
        piece_at_current_pos: Piece = current_pos.get_current_piece()
        if piece_at_current_pos is None:
            print("ERROR: There is no piece at the current position.")
            return False
        if piece_at_current_pos.get_player().is_taking_turn() is False:
            print("ERROR: Attempted to move a piece not controlled by the current player.")
            return False

        # Check the new position
        new_pos: Position = self.get_position(xy_coord[1])
        piece_at_new_pos: Piece = new_pos.get_current_piece()
        if piece_at_new_pos is None:
            move_is_a_reposition = True
        elif piece_at_new_pos.get_player().is_taking_turn() is False:
            move_is_a_capture = True
        elif piece_at_new_pos.get_player().is_taking_turn() is True:
            print("ERROR: Attempted to move a piece to a position already controlled by the current player.")
            return False
        else:
            print("An unknown condition was found while checking the new position in Board.check_move()")

        # Get the piece's movement rules

        # Determine that either the current position or new position are within
        # a Palace.
            # If a move is exiting the palace, then must follow Palace movement rules
            # until it reaches the perimeter of the palace.
            # If a move is entering the palace, there may be different rules too? Unsure

        # Check the piece's movement rules...
            # (1) By seeing if the change in coordinates from the current pos and new pos
            # represent a valid vector in the context of the piece's movement rules
            # (2) By seeing if the sequence moves needed to get to the new pos are possible,
            # by iterating through the positions in that sequence and detecting if another piece
            # is present at any of those positions.

        # If the piece's movement rules are valid, return True

    @staticmethod
    def get_red_palace_coordinates() -> dict:
        """
        Static method that returns the (x,y) coordinates of the Red palace positions. Data structure returned
        is a dict[tuple]: (tuple(tuple))
        """

        # we eventually can change this data struct to a dict so that we can use it
        # to look up valid piece movements within the palace.
        red_palace_positions = {(4, 1): ((1, 0), (1, -1), (0, -1)),
                                (5, 1): ((-1, 0), (0, -1), (1, 0)),
                                (6, 1): ((-1, 0), (-1, -1), (0, -1)),

                                (4, 2): ((0, 1), (1, 0), (0, -1)),
                                (5, 2): ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, -1)),
                                (6, 2): ((0, 1), (-1, 0), (0, -1)),

                                (4, 3): ((0, 1), (1, 1), (1, 0)),
                                (5, 3): ((-1, 0), (0, 1), (1, 0)),
                                (6, 3): ((-1, 0), (-1, 1), (0, 1))
                                }

        return red_palace_positions

    @staticmethod
    def get_blue_palace_coordinates() -> dict:
        """
        Static method that returns the (x,y) coordinates of the Red palace positions. Data structure returned
        is dict[tuple]: (tuple(tuple))
        """
        # we eventually can change this data struct to a dict so that we can use it
        # to look up valid piece movements within the palace.
        red_palace_positions = {(4, 10): ((0, 1), (1, 1), (1, 0)),
                                (5, 10): ((-1, 0), (0, 1), (1, 0)),
                                (6, 10): ((-1, 0), (-1, 1), (0, 1)),

                                (4, 9): ((0, 1), (1, 0), (0, -1)),
                                (5, 9): ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, -1)),
                                (6, 9): ((0, 1), (-1, 0), (0, -1)),

                                (4, 8): ((1, 0), (1, -1), (0, -1)),
                                (5, 8): ((-1, 0), (0, -1), (1, 0)),
                                (6, 8): ((-1, 0), (-1, -1), (0, -1))
                                }

        return red_palace_positions


class Piece:
    """
    The Piece class represents a piece object - in practice all Piece objects will exist as
    one of the child classes associated with this parent Piece class. Each piece
    will have be associated with a controlling player, possess a label, and have fields
    determining its possible start positions, move rules, whether it is in or confined to
    the palace, as well as additional fields like _in_danger or _captured.
    """

    def __init__(self, player: Player, label: str):
        """
        Initializes the Piece object
        """
        self._controlling_player = player
        self._label = label

        self._red_start_coordinates = ()
        self._blue_start_coordinates = ()

        self._in_palace = None
        self._confined_to_palace = None
        self._possible_moves = {(): (())}

        # # unsure as to whether these fields will be useful later
        # self._in_danger = None
        # self._captured = None

    def get_player(self) -> Player:
        """
        Returns the Player object that the piece is controlled by.
        """
        return self._controlling_player

    def get_label(self) -> str:
        """
        Returns the string label that identifies the piece type.
        """
        return self._label

    def get_starting_coordinates(self) -> tuple:
        """
        Returns the starting positions for the piece, based on the piece's color ("BLUE" or "RED")
        :return: A tuple of tuples. If the piece is a General, the second tuple will be None.
        """
        if self._controlling_player.get_player_color() == "BLUE":
            return self._blue_start_coordinates
        elif self._controlling_player.get_player_color() == "RED":
            return self._red_start_coordinates
        else:
            print("ERROR: A player other than BLUE or RED was detected.")

    def get_possible_moves(self) -> dict:
        """
        Returns the possible movements for the Piece.
        """
        return self._possible_moves


class General(Piece):
    """
    A child class of Piece that represents the General.
    """

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
    """
    A child class of Piece that represents a Guard.
    """
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
    """
    A child class of Piece that represents a Chariot.
    """
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
    """
    A child class of Piece that represents a Horse.
    """
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
    """
    A child class of piece that represents an Elephant.
    """
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
    """
    A child class of Piece that represents a Cannon.
    """
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
    """
    A child class of Piece that represents a Soldier.
    """
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
    which represents its location on the board and is therefore the position's unique identifier.\n

    If a Piece object resides at the Position, that piece can be accessed using the method
    Position.get_current_piece(). If a Position is a palace position, then the method
    Position.check_if_palace_position() returns True.
    """

    def __init__(self, xy_position: tuple):
        """
        Initializes the Position object. Accepts a tuple (x,y) as an argument.
        """

        self._xy_pos = xy_position
        self._is_palace_position = self.check_if_palace_position()

        self._current_piece = None

    def check_if_palace_position(self) -> bool:
        """
        Checks to see if this Position represents a Palace position.

        Accomplishes this by calling the static methods Board.get_[color]_palace_coordinates(),
        where [color] is either "red" or "blue".

        If the (x,y) coordinate associated with the Position is found in the data structure in either of the two static
        methods, this method returns True. Otherwise, returns False.
        """
        if self._xy_pos in Board.get_blue_palace_coordinates():
            return True
        elif self._xy_pos in Board.get_red_palace_coordinates():
            return True
        else:
            return False

    def get_current_piece(self) -> Piece:
        """
        Returns the current Piece object assigned to the position. If the position does not have a piece, this method
        returns None.
        """
        return self._current_piece

    def get_position_location(self) -> tuple:
        """
        Returns the (x,y) location of the position.
        """
        return self._xy_pos

    def assign_piece_to_empty_position(self, piece: Piece):
        """
        Assigns a piece to an empty position. If the position is already filled, then an Exception is raised.
        """
        # TODO: Filter out attempts to assign a piece to a filled position (such that self_current_piece != None)
        self._current_piece = piece

    def remove_piece_from_position(self, controlling_player: Player):
        """
        Removes a Piece object from the Position. Accepts a Player object as an argument. If the Player argument is not
        equal to the piece's controlling player, then an Exception is raised. Otherwise the Piece is removed by setting
        self._current_piece to None.
        """
        # TODO: Filter out attempts to remove Piece if controlling_player != self._current_piece.get_player()
        self._current_piece = None


game = JanggiGame()
gameboard = game.get_board()
game.display_board()

game.make_move("a9", "i10")
game.switch_turns()
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
