#
# Author:       Chris Jacobs
# Date:         2/25/2021
# Submitted:    3/11/2021
# Assignment:   CS 162 Portfolio Assignment - Janggi
#               v0.2
#
# Description:  A CLI version of Janggi, aka Korean Chess. Please view README.md and janggi_notes.txt
#               for further details.
#

from Game import Game
from Player import Player


def main():

    p1_name = input("Player 1: ")
    p1 = Player("p1", p1_name)

    p2_name = input("Player 2:")
    p2 = Player("p2", p2_name)

    new_game = Game(p1, p2)
    new_game.start()


main()
