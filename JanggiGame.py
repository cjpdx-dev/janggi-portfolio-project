#
# Author:       Chris Jacobs
# Date:         2/25/2021
# Assignment:   CS 162 Portfolio Assignment - Janggi
#
# Description:  A CLI version of Janggi, aka Korean Chess. Please view README.md and janggi_notes.txt
#               for further details.
#

class JanggiGame:

    def __init__(self):
        pass


class Player:

    def __init__(self):
        pass


class Board:

    def __init__(self):
        pass


class Position:

    def __init__(self):
        pass


class Piece:

    def __init__(self):
        pass


class General(Piece):

    def __init__(self):
        super().__init__()


class Guard(Piece):

    def __init__(self):
        super().__init__()


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


class DisplayDriver:

    def __init__(self):

        self.line1 = "                                                            "
        self.line2 = "             aa  bb  cc  dd  ee  ff  gg  hh  ii   BLUE: %s  "
        self.line3 = "          ========================================          "
        self.line4 = "       10 |--%s--%s--%s-|%s\-%s-/%s|-%s--%s--%s--| 10       "
        self.line5 = "          |             |   \  /   |             |          "
        self.line6 = "        9 |--%s--%s--%s-|%s--%s--%s|-%s--%s--%s--| 9        "
        self.line7 = "          |             |   /  \   |             |          "
        self.line8 = "        8 |--%s--%s--%s-|%s/-%s-\%s|-%s--%s--%s--| 8        "
        self.line9 = "          |             |----------|             |          "
        self.line10 = "        7 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 7        "
        self.line11 = "          |                                      |          "
        self.line12 = "        6 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 6        "
        self.line13 = "          |                                      |          "
        self.line14 = "        5 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 5        "
        self.line15 = "          |                                      |          "
        self.line16 = "        4 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 4        "
        self.line17 = "          |             |----------|             |          "
        self.line18 = "        3 |--%s--%s--%s-|%s\-%s-/%s|-%s--%s--%s--| 3        "
        self.line19 = "          |             |   \  /   |             |          "
        self.line20 = "        2 |--%s--%s--%s-|%s--%s--%s|-%s--%s--%s--| 2        "
        self.line21 = "          |             |   /  \   |             |          "
        self.line22 = "        1 |--%s--%s--%s-|%s/-%s-\%s|-%s--%s--%s--| 1        "
        self.line23 = "          ========================================          "
        self.line24 = "             aa  bb  cc  dd  ee  ff  gg  hh  ii   RED: %s   "
        self.line25 = "                                                            "

        self.board_rows = [self.line1, self.line2, self.line3, self.line4, self.line5, self.line6,
                           self.line7, self.line8, self.line9, self.line10, self.line11, self.line12,
                           self.line13, self.line14, self.line15, self.line16, self.line17, self.line18,
                           self.line19, self.line20, self.line21, self.line22, self.line23, self.line24,
                           self.line25]

    def display_board(self, pieces):

        i = 0
        for row in self.board_rows:
            if "%" in row:
                print(row % tuple(pieces[i]))
                i += 1
            else:
                print(row)


display = DisplayDriver()
all_placements = ["100"], \
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

display.display_board(all_placements)









