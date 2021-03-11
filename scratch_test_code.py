from JanggiGame import JanggiGame
from JanggiGame import Board
from JanggiGame import Piece
from JanggiGame import Player
from JanggiGame import Chariot

game: JanggiGame = JanggiGame()

game_board = game.get_game_board()
player = game.get_current_player()

chariot: Chariot = Chariot(player, "ch")
print(chariot.get_possible_moves())
