#
# Author: Chris Jacobs
# Date: 3/1/2021
# Description: A class for creating the CLI display for a Janggi game board
#

class JanggiDisplay:

    def __init__(self):

        self.line1 = "                                                            "
        self.line2 = "             aa  bb  cc  dd  ee  ff  gg  hh  ii   BLUE: %s  "
        self.line3 = "          ========================================          "
        self.line4 = "       10 |--%s--%s--%s-|%s\-%s-/%s|-%s--%s--%s--| 10       "
        self.line5 = "          |             |   \  /   |             |          "
        self.line6 = "        9 |--%s--%s--%s-|%s--%s--%s|-%s--%s--%s--| 9        "
        self.line7 = "          |             |   /  \   |             |          "
        self.line8 = "        8 |--%s--%s--%s-|%s/-%s-\%s|-%s--%s--%s--| 8        "
        self.line9 = "          |                                      |          "
        self.line10 = "        7 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 7        "
        self.line11 = "          |                                      |          "
        self.line12 = "        6 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 6        "
        self.line13 = "          |                                      |          "
        self.line14 = "        5 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 5        "
        self.line15 = "          |                                      |          "
        self.line16 = "        4 |--%s--%s--%s--%s--%s--%s--%s--%s--%s--| 4        "
        self.line17 = "          |                                      |          "
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

    def display_board(self, current_board):

        i = 0
        for row in self.board_rows:
            if "%" in row:
                print(row % tuple(current_board[i]))
                i += 1
            else:
                print(row)


if __name__ == "__main__":
    print("JanggiDisplay.py is being run directly")
    display = JanggiDisplay()
    display.display_board()
else:
    print("JanggiDisplay.py is being imported into another module")
