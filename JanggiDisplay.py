#
# Author: Chris Jacobs
# Date: 3/1/2021
# Description: A class for creating the CLI display for a Janggi game board.
# This class and the code that utilizes it in JanggiGame.py will be disabled in the final submission of the project.
#

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
        self.line18 = "          |             |   \  /   |             |          "
        self.line19 = "        9 |--%s--%s--%s-|%s--%s--%s|-%s--%s--%s--| 9        "
        self.line20 = "          |             |   /  \   |             |          "
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

    def display_test_board(self):

        test_placements = ["0"], \
                          ["ch", "el", "hr", "gu", "**", "gu", "el", "hr", "ch"], \
                          ["**", "**", "**", "**", "ge", "**", "**", "**", "**"], \
                          ["**", "ca", "**", "**", "**", "**", "**", "ca", "**"], \
                          ["so", "**", "so", "**", "so", "**", "so", "**", "so"], \
                          ["**", "**", "**", "**", "**", "**", "**", "**", "**"], \
                          ["**", "**", "**", "**", "**", "**", "**", "**", "**"], \
                          ["SO", "**", "SO", "**", "SO", "**", "SO", "**", "SO"], \
                          ["**", "CA", "**", "**", "**", "**", "**", "CA", "**"], \
                          ["**", "**", "**", "**", "GE", "**", "**", "**", "**"], \
                          ["CH", "EL", "HR", "GU", "**", "GU", "EL", "HR", "CH"], \
                          ["0"]

        self.draw(test_placements)


if __name__ == "__main__":
    print("JanggiDisplay.py is being run directly: displaying a sample test board.")
    display = JanggiDisplay()
    display.display_test_board()
else:
    print("JanggiDisplay.py is being imported into another module")
