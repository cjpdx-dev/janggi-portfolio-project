#
# Author:       Chris Jacobs
# Date:         2/25/2021
# Assignment:   CS 162 Portfolio Assignment - Janggi
#
# Description:  A CLI version of Janggi, aka Korean Chess. Please view README.md and janggi_notes.txt
#               for further details.
#


class JanggiGame:
    """
    JanggiGame class is the controller class for the game. All methods the user uses to play the game are methods
    that are part of this class. The class also holds the fields that describe the state of the game and two
    objects that make up the bulk of the game - the game board and the individual players.
    """
    def __init__(self):
        """ Initializes the JanggiGame object """

        self._game_state = None                                     # Initialize the game state

        self._player_1: Player = Player("blue")                             # Initialize the players
        self._player_2: Player = Player("red")
        self._current_player: Player = None

        self._game_board = Board(self._player_1, self._player_2)    # Initialize the game board
        self._display = JanggiDisplay()
        self.start_game()

    def start_game(self):
        """
        Starts the game by setting Player 1 as the current player and setting the game state
        as "UNFINISHED"
        """
        self._game_state = "UNFINISHED"
        self._current_player: Player = self._player_1
        self._player_1.set_as_current_player(True)

    def make_move(self, current_pos: str, new_pos: str) -> bool:
        """
        Makes a move, first by validating the old position and then the new position. Gets
        the Piece at the old position and checks if it belongs to the next_player. Then checks
        the new position to see if it is either empty or occupied by the opposing player. Finally,
        """

        print("Attempting ", current_pos, " to ", new_pos)
        if self.get_game_state() != "UNFINISHED":
            return False

        input_positions = (current_pos.lower(), new_pos.lower())
        if self.validate_position_existence(input_positions) is False:
            return False
        else:
            xy_move = self.convert_algebraic_to_xy((current_pos, new_pos))

        if self._game_board.check_for_pass(xy_move) is True:
            print("Passing turn.")
            self.switch_turns()
            return True

        next_move = self._game_board.validate_move_rules(xy_move)

        if next_move is not None:

            can_complete_move = True

            # # make sure player moved themselves out of check
            # if self._current_player.is_in_check() is True:
            #     if self.detect_out_of_check(self._current_player, next_move) is False:
            #         self._current_player.set_check_status(False)
            #         can_complete_move = True
            #
            # # make sure player didn't put themselves in check
            # if self._current_player.is_in_check() is False:
            #     if self.detect_out_of_check(self._current_player, next_move) is False:
            #         can_complete_move = True

            if can_complete_move is True:
                self._game_board.complete_move(next_move)
                self.refresh_game_state()
                return True
            else:
                return False

        else:
            return False

    @staticmethod
    def validate_position_existence(input_positions: tuple) -> bool:
        """
        Checks that the converted (x,y) notation is valid (i.e. the position exists on the board).
        Does NOT check if the made cannot be made of other reasons.
        """
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

        """
        if self.detect_check(self.get_next_player()) is True:
            self.get_next_player().set_check_status(True)

        self.switch_turns()

    def detect_out_of_check(self, current_player, next_move):
        return True

    def detect_check(self, next_player):

        opposing_player = self.get_current_player()

        position_of_general = self._game_board.find_position_of_general(next_player)
        gen_position_xy = position_of_general.get_position_location()

        opposing_player_positions = self._game_board.find_all_opposing_positions(opposing_player)

        print(opposing_player_positions)
        for opposing_position in opposing_player_positions:
            opposing_location = opposing_position.get_position_location()
            opposing_location_to_player_general = (opposing_location, gen_position_xy)

            if self._game_board.validate_move_rules(opposing_location_to_player_general) is not None:
                print("Check scenario found: ", next_player.get_player_color(), " in check!")
                return True
            else:
                continue

        print("Check scenario not found.")

    def is_in_check(self, player_color: str) -> bool:
        """
        Accesses the current player's data to determine if the player is in check and returns True
        or False accordingly. This method is user-facing so it must handle invalid input from the user.
        """
        print(player_color)
        if player_color == "blue":
            return self._player_1.is_in_check()
        elif player_color == "red":
            return self._player_2.is_in_check()
        else:
            print("ERROR: Invalid player color was passed to function JanggiGame.is_in_check()")

    def detect_checkmate(self, player_to_scan):
        pass

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

    def display_board(self):
        """
        Draws a CLI representation of the game board.
        """
        self._display.draw(self.get_drawable_board_data())

    def get_drawable_board_data(self):
        """
        Iterates through each position of the game board and returns a 2D list
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

    def get_game_board(self):
        """ For testing only. Returns the current game board """
        return self._game_board


class Player:
    """
    This class represents the Player. A Player is represented by one of two colors (red or blue).
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
        Returns the player's color (red or blue)
        """
        return self._player_color

    def is_current_player(self) -> bool:
        """
        Returns the bool value that represents if the player is currently taking a turn or not
        """
        return self._is_current_player

    def set_as_current_player(self, turn_status: bool):
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


class Move:
    """
    This class represents a validated Move that will be executed by JanggiGame.make_move()
    It is returned from Board.validate_move_rules()
    """
    def __init__(self, old_position, new_position, is_capture):
        """
        Initializes a Move object.
        :param old_position: (object.Position)
        :param new_position: (object.Position)
        :param is_capture: (bool)
        """
        self._old_position: Position = old_position
        self._piece_moving: Piece = self._old_position.get_current_piece()
        self._player_moving: Player = self._piece_moving.get_player()

        self._new_position: Position = new_position

        self._is_capture: bool = is_capture
        if self._is_capture is True:
            self._piece_being_captured: Piece = self._new_position.get_current_piece()
            self._player_being_captured: Player = self._new_position.get_current_piece().get_player()
        else:
            self._piece_being_captured = None
            self._player_being_captured = None

    def get_player(self) -> Player:
        """ Returns the current player associated with the move """
        return self._player_moving

    def get_old_position(self):
        """ Returns the old position associated with the move """
        return self._old_position

    def get_new_position(self):
        """ Returns the new position associated with the Move"""
        return self._new_position

    def move_is_a_capture(self):
        return self._is_capture


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
        self.initialize_empty_board()
        self.place_player_pieces()

        self._pieces_that_can_move_in_palace = ("ge", "gu", "ch", "ca", "so")

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

    def validate_move_rules(self, xy_coord: tuple):
        """
        Determine if the move is valid based on piece placement and piece movement ability.
        Accepts a tuple that represents (current_position, new_position). These positions have already
        been verified to exist on the board before this method can be called. The move itself is validated
        by this method. Returns a Move object if the move is shown to be possible, otherwise returns None.
        """
        # Check the current position
        current_pos: Position = self.get_position(xy_coord[0])
        piece_at_current_pos: Piece = current_pos.get_current_piece()

        if self.validate_current_position(piece_at_current_pos) is False:
            return None
        else:
            piece_label = piece_at_current_pos.get_label()

        new_pos: Position = self.get_position(xy_coord[1])
        piece_at_new_pos: Piece = new_pos.get_current_piece()

        if self.validate_new_position(piece_at_new_pos) is False:
            return None
        else:
            if piece_at_new_pos is None:
                is_capture = False
            else:
                is_capture = True

        if current_pos.check_if_palace_position() is True:
            if self.check_palace_piece_movement(current_pos, new_pos, is_capture) is False:
                return None
            else:
                return Move(current_pos, new_pos, is_capture)
        else:
            if piece_label == "ch":
                if self.check_chariot_movement_outside_palace(current_pos, new_pos) is True:
                    return Move(current_pos, new_pos, is_capture)
                else:
                    return None
            elif piece_label == "ca":
                if self.check_cannon_movement_outside_palace(current_pos, new_pos, is_capture) is True:
                    return Move(current_pos, new_pos, is_capture)
                else:
                    return None
            else:
                if self.check_non_palace_piece_movement(current_pos, new_pos) is True:
                    return Move(current_pos, new_pos, is_capture)
                else:
                    return None

    @staticmethod
    def validate_current_position(current_piece):

        if current_piece is None:
            print("Move failed: There is no piece at the current position.")
            return False
        elif current_piece.get_player().is_current_player() is False:
            print("Move failed: Attempted to move a piece not controlled by the current player.")
            return False
        else:
            return True

    @staticmethod
    def validate_new_position(piece_at_new_pos):
        if piece_at_new_pos is not None:
            if piece_at_new_pos.get_player().is_current_player() is True:
                print("Move failed: Attempted to move a piece to a position already controlled by the current player.")
                return False
            else:
                return True

    def check_palace_piece_movement(self, current_pos, new_pos, is_capture):
        """
        Checks the movement rules for a piece currently within the palace that is attempting to move within or move
        outside the palace. Returns True if the movement is valid based on Palace movement
        rules.
        """
        piece_at_current_pos = current_pos.get_current_piece()
        piece_label = piece_at_current_pos.get_label()

        current_xy = current_pos.get_position_location()
        new_xy = new_pos.get_position_location()

        delta_x = new_xy[0] - current_xy[0]
        delta_y = new_xy[1] - current_xy[1]
        delta_xy = (delta_x, delta_y)

        move_is_diagonal = self.check_if_move_is_diagonal(delta_x, delta_y)

        if piece_at_current_pos.is_confined_to_palace():
            if new_pos.check_if_palace_position() is False:
                print("Move failed: Palace confined piece attempted to move outside the palace.")
                return False

        current_palace_rules = self.get_palace_rules(current_pos)

        allowed_movements = current_palace_rules[current_xy]
        if allowed_movements is None:
            print("Board.check_palace_piece_movement() was called in error: allowed_movements was None")
            return False

        if piece_at_current_pos.is_confined_to_palace() is True:
            if delta_xy not in allowed_movements:
                print("Move failed: a piece confined to the palace attempted to a move to a position that is")
                print("incompatible with the Palace position's movement rules.")
                return False
            else:
                return True

        print(piece_label)
        if piece_at_current_pos.is_confined_to_palace() is False and current_pos.check_if_palace_position() is True:
            if piece_label == "ch":
                if move_is_diagonal is True:
                    if self.check_chariot_movement_inside_palace(current_pos, new_pos) is True:
                        return True
                    else:
                        return False
                else:
                    if self.check_chariot_movement_outside_palace(current_pos, new_pos) is True:
                        return True
                    else:
                        return False

            elif piece_label == "ca":
                if self.check_cannon_movement_inside_palace(current_pos, new_pos, is_capture) is True:
                    return True
                else:
                    return False

            elif piece_label == "so":
                if self.check_soldier_movement_inside_palace(current_pos, new_pos) is True:
                    return True
                else:
                    return False

            else:
                return self.check_non_palace_piece_movement(current_pos, new_pos)

        print("Reached the end of check_palace_piece_movement() with no return. Returning False")
        return False

    def check_non_palace_piece_movement(self, current_pos, new_pos):
        current_pos: Position = current_pos
        current_xy = current_pos.get_position_location()

        piece_at_current_pos: Piece = current_pos.get_current_piece()
        piece_label: str = piece_at_current_pos.get_label()
        piece_movement_rules = piece_at_current_pos.get_possible_moves()

        new_pos: Position = new_pos
        new_xy = new_pos.get_position_location()

        delta_x = new_xy[0] - current_xy[0]
        delta_y = new_xy[1] - current_xy[1]
        delta_xy = (delta_x, delta_y)

        move_is_diagonal = self.check_if_move_is_diagonal(delta_x, delta_y)
        if move_is_diagonal:
            print("Move failed: No piece outside of the palace can move purely diagonally.")
            return False

        if delta_xy in piece_movement_rules:
            move_sequence = piece_movement_rules[delta_xy]
        else:
            print("Move failed: move was not possible based on ", piece_label.upper(), " movement rules.")
            return False

        temp_current_xy = current_xy
        for move in move_sequence:
            temp_current_xy = (move[0] + temp_current_xy[0], move[1] + temp_current_xy[1])
            temp_position: Position = self.get_position(temp_current_xy)
            if temp_position.get_current_piece() is not None:
                if temp_current_xy != new_xy:
                    print("Move failed: a piece blocked the move from being completed.")
                    return False
                else:
                    return True
        return True

    def check_chariot_movement_inside_palace(self, current_pos, new_pos) -> bool:

        # new_pos and current_pos are reinitialized for the sake of type hinting
        # can't do this in method signature because we're working with a single file
        # and Position is the last class of the file.

        current_pos: Position = current_pos
        current_xy = current_pos.get_position_location()

        new_pos: Position = new_pos
        new_xy = new_pos.get_position_location()

        delta_x = new_xy[0] - current_xy[0]
        delta_y = new_xy[1] - current_xy[1]
        delta_xy = (delta_x, delta_y)

        move_is_diagonal = self.check_if_move_is_diagonal(delta_x, delta_y)
        delta_xy_div_abs = None
        if move_is_diagonal is True:
            delta_xy_div_abs = self.get_delta_xy_div_abs_xy(delta_x, delta_y)
            if delta_xy_div_abs is None:
                print("ERROR: get_delta_xy_div_abs_xy() handled a non-diagonal move")
                return False

        piece_at_current_pos: Piece = current_pos.get_current_piece()
        piece_movement_rules = piece_at_current_pos.get_possible_moves()

        current_palace_rules = self.get_palace_rules(current_pos)
        current_position_rules = current_palace_rules[current_xy]
        print(current_palace_rules)
        print(current_position_rules)

        if move_is_diagonal is True and new_pos.check_if_palace_position() is False:
            print("Move failed: Chariot attempted to move along a diagonal to a position outside of the Palace")
            return False

        if move_is_diagonal is False and new_pos.check_if_palace_position() is False:
            print("Move failed: a purely diagonal move can not occur for any piece outside of the palace")

        if move_is_diagonal is True and new_pos.check_if_palace_position() is True:

            if delta_xy_div_abs in current_position_rules:
                temp_xy = current_xy

                while temp_xy != new_xy:
                    temp_position: Position = self.get_position(temp_xy)
                    temp_movement_rules = current_palace_rules[temp_xy]

                    next_xy = (int(temp_xy[0] + delta_xy_div_abs[0]),
                               int(temp_xy[1] + delta_xy_div_abs[1]))
                    next_position = self.get_position(next_xy)

                    if temp_position is None:
                        print("Move failed: could not track a path to the new position before hitting a ")
                        print("non-existent position.")
                        return False

                    if delta_xy_div_abs not in temp_movement_rules:
                        print("Move failed: could not track a path to the new position - palace movement")
                        print("rules prevented the move.")
                        return False

                    elif temp_position.check_if_palace_position() is False:
                        print("Move failed: Chariot left the palace while attempting a diagonal move.")
                        return False

                    elif next_position.get_current_piece() is not None and next_xy != new_xy:
                        print("Move failed: Encountered a piece that blocks the path of the move.")
                        return False

                    temp_xy = (int(temp_xy[0] + delta_xy_div_abs[0]),
                               int(temp_xy[1] + delta_xy_div_abs[1]))

                return True

            else:
                print("Move failed: the Chariot's movement within the palace violated the Palace rules")
                return False

        if move_is_diagonal is False and new_pos.check_if_palace_position() is True:
            for movement in piece_movement_rules:
                print(movement)
            if delta_xy_div_abs in current_position_rules:
                temp_xy = current_xy
                while temp_xy != new_xy:
                    pass

        if move_is_diagonal is False and new_pos.check_if_palace_position() is False:
            return self.check_chariot_movement_outside_palace()

    @staticmethod
    def check_chariot_movement_outside_palace(current_pos, new_pos):
        current_pos: Position = current_pos
        current_xy = current_pos.get_position_location()

        new_pos: Position = new_pos
        new_xy = new_pos.get_position_location()

        delta_x = new_xy[0] - current_xy[0]
        delta_y = new_xy[1] - current_xy[1]
        delta_xy = (delta_x, delta_y)

        current_piece: Piece = current_pos.get_current_piece()
        piece_movement_rules = current_piece.get_possible_moves()

        move_is_diagonal = Board.check_if_move_is_diagonal(delta_x, delta_y)
        if move_is_diagonal:
            print("Move failed: Chariot cannot move diagonally when outside of the Palace.")
            return False

        valid_delta = False
        for movement_direction in piece_movement_rules:

            if movement_direction[0] == 0:
                for y in movement_direction[1]:
                    if (movement_direction[0], y) == delta_xy:
                        valid_delta = True

            if movement_direction[1] == 0:
                for x in movement_direction[0]:
                    if (x, movement_direction[1]) == delta_xy:
                        valid_delta = True

        if valid_delta is False:
            print("Move failed: move was not possible based on Chariot's movement rules.")
            return False
        else:
            # check for blocking pieces
            return True

    def check_cannon_movement_inside_palace(self, current_pos, new_pos, is_capture):
        # Not implemented.
        pass

    def check_cannon_movement_outside_palace(self, current_pos, new_pos, is_capture):

        current_pos: Position = current_pos
        current_xy = current_pos.get_position_location()

        current_piece: Piece = current_pos.get_current_piece()
        piece_movement_rules = current_piece.get_possible_moves()

        new_pos: Position = new_pos
        new_xy = new_pos.get_position_location()

        if is_capture:
            piece_being_captured = new_pos.get_current_piece()
            if piece_being_captured.get_label() == "ca":
                print("Move failed: Cannons cannot capture other cannons.")
                return False

        delta_x = new_xy[0] - current_xy[0]
        delta_y = new_xy[1] - current_xy[1]
        delta_xy = (delta_x, delta_y)

        move_is_diagonal = Board.check_if_move_is_diagonal(delta_x, delta_y)
        if move_is_diagonal:
            print("Move failed: Cannon cannot move diagonally when outside of the Palace.")
            return False

        valid_delta = False
        for movement_direction in piece_movement_rules:

            if movement_direction[0] == 0:
                for y in movement_direction[1]:
                    if (movement_direction[0], y) == delta_xy:
                        valid_delta = True

            if movement_direction[1] == 0:
                for x in movement_direction[0]:
                    if (x, movement_direction[1]) == delta_xy:
                        valid_delta = True

        if valid_delta is False:
            print("Move failed: move was not possible based on Cannon's movement rules.")
            return False
        else:
            # check for piece orthogonal to cannon in direction of its movement
            print("Current delta xy: ", delta_xy)
            print("Current xy: ", current_xy)

            if delta_x != 0:
                delta_x_div_abs_x = int(delta_x / abs(delta_x))
            else:
                delta_x_div_abs_x = 0

            if delta_y != 0:
                delta_y_div_abs_y = int(delta_y / abs(delta_y))
            else:
                delta_y_div_abs_y = 0

            next_position_xy = (current_xy[0] + delta_x_div_abs_x, current_xy[1] + delta_y_div_abs_y)
            next_position: Position = self.get_position(next_position_xy)
            piece_at_next_position = next_position.get_current_piece()

            if piece_at_next_position is None:
                print("Move failed: Cannon did not have another piece orthogonal to it in the direction of its move.")
                return False
            else:
                return True

    def check_soldier_movement_inside_palace(self, current_pos, new_pos):
        current_pos: Position = current_pos
        current_xy = current_pos.get_position_location()

        new_pos: Position = new_pos
        new_xy = new_pos.get_position_location()

        delta_x = new_xy[0] - current_xy[0]
        delta_y = new_xy[1] - current_xy[1]
        delta_xy = (delta_x, delta_y)

        move_is_diagonal = self.check_if_move_is_diagonal(delta_x, delta_y)

        delta_xy_div_abs = None
        if move_is_diagonal is True:
            delta_xy_div_abs = self.get_delta_xy_div_abs_xy(delta_x, delta_y)
            if delta_xy_div_abs is None:
                print("ERROR: get_delta_xy_div_abs_xy() handled a non-diagonal move")
                return False

        piece_at_current_pos: Piece = current_pos.get_current_piece()
        piece_movement_rules = piece_at_current_pos.get_possible_moves()

        current_palace_rules = self.get_palace_rules(current_pos)
        current_position_rules = current_palace_rules[current_xy]

        if new_pos.check_if_palace_position() is False:
            if delta_xy in piece_movement_rules:
                return True
            else:
                return False

    def find_position_of_general(self, player):

        # TODO: there's a better way to do this - have a field in Player that updates the position
        # of the general each time the player moves the general. Don't have time to implement
        # that right now so we are just brute forcing it here.

        for position_xy in self._board:
            current_position: Position = self.get_position(position_xy)
            current_piece = current_position.get_current_piece()

            if current_piece is None:
                continue

            if current_piece.get_player() is not player:
                continue

            if current_piece.get_player() is player:
                if current_piece.get_label() != "ge":
                    continue
                else:
                    return current_position

            print("ERROR: Player's general could not be found on game board. Returning None")
            return None

    def find_all_opposing_positions(self, opposing_player) -> list:
        """

        :param opposing_player:
        :return:
        """
        opposing_positions = []
        for position in self._board:
            current_position: Position = self.get_position(position)

            if current_position.get_current_piece() is not None:
                current_piece = current_position.get_current_piece()
                if current_piece.get_player() == opposing_player:
                    opposing_positions.append(current_position)
                else:
                    continue
            else:
                continue

        return opposing_positions

    @staticmethod
    def complete_move(next_move: Move):
        old_position = next_move.get_old_position()
        piece_at_old_position = old_position.get_current_piece()

        new_position = next_move.get_new_position()
        is_capture = next_move.move_is_a_capture()

        if is_capture is True:
            new_position.remove_piece_from_position()
            new_position.assign_piece_to_empty_position(piece_at_old_position)
            old_position.remove_piece_from_position()
        else:
            new_position.assign_piece_to_empty_position(piece_at_old_position)
            old_position.remove_piece_from_position()

        print("Move completed.")

    def check_for_pass(self, xy_move):
        current_position: Position = self.get_position(xy_move[0])
        piece_at_current_position = current_position.get_current_piece()

        if piece_at_current_position is not None:
            controlling_player = piece_at_current_position.get_player()

            if controlling_player.is_current_player():
                if xy_move[0] == xy_move[1]:
                    print("Pass detected")
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    @staticmethod
    def get_red_palace_move_rules() -> dict:
        """
        Static method that returns the (x,y) coordinates of the Red palace positions. Data structure returned
        is a dict[tuple]: (tuple(tuple))
        """
        red_palace_positions = {(4, 1): ((0, 1), (1, 1), (1, 0)),
                                (5, 1): ((-1, 0), (0, 1), (1, 0)),
                                (6, 1): ((-1, 0), (-1, 1), (0, 1)),

                                (4, 2): ((0, 1), (1, 0), (0, -1)),
                                (5, 2): ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 1), (-1, 0), (-1, -1)),
                                (6, 2): ((0, 1), (-1, 0), (0, -1)),

                                (4, 3): ((1, 0), (1, -1), (0, -1)),
                                (5, 3): ((-1, 0), (0, -1), (1, 0)),
                                (6, 3): ((-1, 0), (-1, -1), (0, -1))
                                }

        return red_palace_positions

    @staticmethod
    def get_blue_palace_move_rules() -> dict:
        """
        Static method that returns the (x,y) coordinates of the Red palace positions. Data structure returned
        is dict[tuple]: (tuple(tuple))
        """
        blue_palace_positions = {(4, 10): ((1, 0), (1, -1), (0, -1)),
                                 (5, 10): ((-1, 0), (0, -1), (1, 0)),
                                 (6, 10): ((-1, 0), (-1, -1), (0, -1)),

                                 (4, 9): ((0, 1), (1, 0), (0, -1)),
                                 (5, 9): ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 1), (-1, 0), (-1, -1)),
                                 (6, 9): ((0, 1), (-1, 0), (0, -1)),

                                 (4, 8): ((0, 1), (1, 1), (1, 0)),
                                 (5, 8): ((-1, 0), (0, 1), (1, 0)),
                                 (6, 8): ((-1, 0), (-1, 1), (0, 1))
                                 }

        return blue_palace_positions

    @staticmethod
    def get_palace_rules(current_pos):
        if current_pos.check_if_red_palace() is True:
            return Board.get_red_palace_move_rules()
        elif current_pos.check_if_blue_palace() is True:
            return Board.get_blue_palace_move_rules()
        else:
            print("Error in Board.get_palace_rules()")
            return None

    @staticmethod
    def check_if_move_is_diagonal(delta_x, delta_y):
        if (delta_x - delta_y == 0) or (delta_x + delta_y == 0):
            return True
        else:
            return False

    @staticmethod
    def get_delta_xy_div_abs_xy(delta_x, delta_y):
        try:
            delta_x_div_abs_x = delta_x / abs(delta_x)
            delta_y_div_abs_y = delta_y / abs(delta_y)
            delta_xy_div_abs = (delta_x_div_abs_x, delta_y_div_abs_y)
            return delta_xy_div_abs
        except ZeroDivisionError:
            print("ERROR: delta_xy_div_abs_xy handled a non-diagonal move")
            return None

    @staticmethod
    def get_palace_diagonals():

        palace_diagonals = ((1, 1), (-1, -1), (1, -1), (-1, 1), (2, 2), (-2, -2), (2, -2), (-2, 2))
        return palace_diagonals


class Piece:
    """
    The Piece class represents a piece object - in practice all Piece objects will exist as
    one of the child classes associated with this parent Piece class.

    Each piece will have be associated with a controlling player, possess a label, and have fields
    determining its possible start positions, move rules, whether it is in or confined to
    the palace.
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

    def is_in_palace(self) -> bool:
        """
        Returns True if Piece is currently in Palace. Otherwise returns False.
        """
        return self._in_palace

    def is_confined_to_palace(self) -> bool:
        """
        Returns a bool representing whether the piece is confined to the palace or not.
        """
        return self._confined_to_palace

    def get_starting_coordinates(self) -> tuple:
        """
        Returns the starting positions for the piece, based on the piece's color ("blue" or "red")
        :return: A tuple of tuples. If the piece is a General, the second tuple will be None.
        """
        if self._controlling_player.get_player_color() == "blue":
            return self._blue_start_coordinates
        elif self._controlling_player.get_player_color() == "red":
            return self._red_start_coordinates
        else:
            print("ERROR: A player other than blue or red was detected.")

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

        self._red_start_coordinates = ((5, 2), )
        self._blue_start_coordinates = ((5, 9), )

        self._in_palace = True
        self._confined_to_palace = True
        self._possible_moves = {(1, 0): ((1, 0), ),
                                (0, 1): ((0, 1), ),
                                (-1, 0): ((-1, 0), ),
                                (0, -1): ((0, -1), )
                                }

        self._in_check = False
        self._in_checkmate = False


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
        self._possible_moves = {(1, 0): ((1, 0), ),
                                (0, 1): ((0, 1), ),
                                (-1, 0): ((-1, 0), ),
                                (0, -1): ((0, -1), )
                                }


class Chariot(Piece):
    """
    A child class of Piece that represents a Chariot. Chariot's have a different data structure
    for possible moves - instead of a dict with a key as a vector and a value of move sequences,
    Chariots have a tuple that holds a range of tuples.
    """
    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 13

        self._red_start_coordinates = ((1, 1), (9, 1))
        self._blue_start_coordinates = ((1, 10), (9, 10))

        self._in_palace = False

        self._confined_to_palace = False

        self._possible_moves = ((0, tuple(range(1, 10))),
                                (tuple((range(1, 9))), 0),
                                (0, tuple(range(-9, 0))),
                                (tuple((range(-8, -0))), 0)
                                )

    def get_possible_moves(self) -> tuple:
        return self._possible_moves


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

        self._possible_moves = {(2, 3): ((0, 1), (1, 1), (1, 1)),
                                (-2, 3): ((0, 1), (-1, 1), (-1, 1)),
                                (2, -3): ((0, -1), (1, -1), (1, -1)),
                                (-2, -3): ((0, -1), (-1, -1), (-1, -1))
                                }


class Cannon(Piece):
    """
    A child class of Piece that represents a Cannon. Cannon's have a different data structure
    for possible moves - instead of a dict with a key as a vector and a value of move sequences,
    Chariots have a tuple that holds a range of tuples.
    """
    def __init__(self, player, label):
        super().__init__(player, label)

        self._label = label
        self._points = 7

        self._red_start_coordinates = ((2, 3), (8, 3))
        self._blue_start_coordinates = ((2, 8), (8, 8))

        self._in_palace = False
        self._confined_to_palace = False
        self._possible_moves = ((0, tuple(range(1, 10))),
                                (tuple((range(1, 9))), 0),
                                (0, tuple(range(-9, 0))),
                                (tuple((range(-8, -0))), 0)
                                )

    def get_possible_moves(self) -> tuple:
        return self._possible_moves


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

        # needs to have red moves and blue moves
        if player.get_player_color() == "red":
            self._possible_moves = {(1, 0): ((1, 0), ),
                                    (0, 1): ((0, 1), ),
                                    (-1, 0): ((-1, 0), )
                                    }

        elif player.get_player_color() == "blue":
            self._possible_moves = {(1, 0): ((1, 0), ),
                                    (0, -1): ((0, -1), ),
                                    (-1, 0): ((-1, 0), )
                                    }


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

        self._current_piece = None

        self._is_red_palace_position = False
        self._is_blue_palace_position = False

        if self._xy_pos in Board.get_red_palace_move_rules():
            self._is_red_palace_position = True

        if self._xy_pos in Board.get_blue_palace_move_rules():
            self._is_blue_palace_position = True

    def check_if_palace_position(self) -> bool:
        """
        Checks to see if this Position represents a Palace position.

        Accomplishes this by calling the static methods Board.get_[color]_palace_coordinates(),
        where [color] is either "red" or "blue".

        If the (x,y) coordinate associated with the Position is found in the data structure in either of the two static
        methods, this method returns True. Otherwise, returns False.
        """
        if self._is_red_palace_position is True or self._is_blue_palace_position is True:
            return True
        else:
            return False

    def check_if_red_palace(self) -> bool:
        """ Returns True if Position is a red palace position """
        if self._is_red_palace_position is True:
            return True
        else:
            return False

    def check_if_blue_palace(self) -> bool:
        """ Returns True if Position is a blue palace position """
        if self._is_blue_palace_position is True:
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
        Assigns a Piece object to an empty position. Assumes that the removal of hte piece Object is valid, based
        on the validation performed in the validate_ methods of Object.Board
        """
        self._current_piece = piece

    def remove_piece_from_position(self):
        """
        Removes a Piece object from the Position. Assumes that the removal of the Piece object is valid, based on
        the validation performed in the validate_ methods in Object.Board
        """
        self._current_piece = None


class JanggiDisplay:

    def __init__(self):

        self.line1 = "             aa  bb  cc  dd  ee  ff  gg  hh  ii   %s : %s  "
        self.line2 = "          ========================================          "
        self.line3 = "        1 |--%s--%s--%s-|%s\-%s-/%s|-%s--%s--%s--| 1        Current player pieces in uppercase."
        self.line4 = "          |             |   \  /   |             |          Opposing player pieces in lowercase."
        self.line5 = "        2 |--%s--%s--%s-|%s--%s--%s|-%s--%s--%s--| 2        "
        self.line6 = "          |             |   /  \   |             |          "
        self.line7 = "        3 |--%s--%s--%s-|%s/-%s-\%s|-%s--%s--%s--| 3        "
        self.line8 = "          |                                      |          "
        self.line9 = "        4 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 4        "
        self.line10 = "          |                                      |         "
        self.line11 = "        5 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 5        "
        self.line12 = "          |                                      |          "
        self.line13 = "        6 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 6        "
        self.line14 = "          |                                      |          "
        self.line15 = "        7 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 7        "
        self.line16 = "          |                                      |          "
        self.line17 = "        8 |--%s--%s--%s-|%s\-%s-/%s|-%s--%s--%s--| 8        "
        self.line18 = "          |             |   \||/   |             |          "
        self.line19 = "        9 |--%s--%s--%s-|%s--%s--%s|-%s--%s--%s--| 9        "
        self.line20 = "          |             |   /||\   |             |          "
        self.line21 = "       10 |--%s--%s--%s-|%s/-%s-\%s|-%s--%s--%s--| 10       "
        self.line22 = "          ========================================          "
        self.line23 = "             aa  bb  cc  dd  ee  ff  gg  hh  ii   %s : %s  "

        self.board_rows = [self.line1, self.line2, self.line3, self.line4, self.line5, self.line6,
                           self.line7, self.line8, self.line9, self.line10, self.line11, self.line12,
                           self.line13, self.line14, self.line15, self.line16, self.line17, self.line18,
                           self.line19, self.line20, self.line21, self.line22, self.line23]

    def draw(self, current_board):
        print()
        i = 0
        for row in self.board_rows:
            if "%" in row:
                print(row % tuple(current_board[i]))
                i += 1
            else:
                print(row)
        print()


