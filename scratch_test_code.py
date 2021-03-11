from JanggiGame import JanggiGame
from JanggiGame import Board
from JanggiGame import Piece
from JanggiGame import Player
from JanggiGame import Chariot

game: JanggiGame = JanggiGame()

game.display_board()
game.make_move("a10", "a9")
game.display_board()
game.make_move("a4", "a5")
game.display_board()
game.make_move("a9", "c9")
game.display_board()
# game_board = game.get_game_board()

# player = game.get_current_player()
#
# chariot: Chariot = Chariot(player, "ch")
# print(chariot.get_possible_moves())
