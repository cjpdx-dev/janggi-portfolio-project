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

    def __init__(self):
        # init game state
        self._game_state = "UNFINISHED"

        # init players
        self._player_1 = Player("RED")
        self._player_2 = Player("BLUE")

        # init game board
        self._game_board = Board(self._player_1, self._player_2)

        # init current player
        self._player_1.set_taking_turn(True)
        self._current_player = self._player_1

    def set_game_state(self, game_state):
        self._game_state = game_state

    def get_game_state(self):
        return self._game_state

    def refresh_game_state(self):
        pass

    def make_move(self, old_pos, new_pos):
        pass
        # check game board for old position data

    def switch_turns(self):

        if self._current_player is self._player_1:
            self._current_player = self._player_2
            self._player_1.set_taking_turn(False)
            self._player_2.set_taking_turn(True)

        elif self._current_player is self._player_2:
            self._current_player = self._player_1
            self._player_2.set_taking_turn(False)
            self._player_1.set_taking_turn(True)
        else:
            print("No current player is set.")



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
        self._initial_red_positions = []


        # rows 10-7 belong to blue

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

        self._blue_start_positions = ["e9"]
        self._red_start_positions = ["e2"]

        self._in_palace = True
        self._confined_to_palace = True


class Guard(Piece):

    def __init__(self):
        super().__init__()

        self._blue_start_positions = ["d10", "f10"]
        self._red_start_positions = ["d1", "f1"]

        self._in_palace = True
        self._confined_to_palace = True


class Chariot(Piece):

    def __init__(self):
        super().__init__()


class Elephant(Piece):

    def __init__(self):
        super().__init__()


class Horse(Piece):

    def __init__(self):
        super().__init__()


class Cannon(Piece):

    def __init__(self):
        super().__init__()


class Soldier(Piece):

    def __init__(self):
        super().__init__()




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









