from JanggiGame import JanggiGame
from JanggiGame import Board
from JanggiGame import Piece
from JanggiGame import Player
from JanggiGame import Chariot

game: JanggiGame = JanggiGame()
game.display_board()
# gameboard = game.get_game_board()
# player1 = game.get_current_player()
# player2 = game.get_next_player()
#
# gen_position = gameboard.find_position_of_general(player1)
# print(gen_position.get_position_location())
#
# opposing_positions = gameboard.find_all_opposing_positions(player2)
# for position in opposing_positions:
#     print(position.get_position_location())
#
# game.refresh_game_state()

game.make_move("c7", "c6")
game.display_board()

game.make_move("c1", "d3")
game.display_board()

game.make_move("b10", "d7")
game.display_board()

game.make_move("b3", "e3")
game.display_board()

game.make_move("c10", "d8")
game.display_board()

game.make_move("h1", "g3")
game.display_board()

game.make_move("e7", "e6")
game.display_board()

game.make_move("e3", "e6")
game.display_board()

game.make_move("h8", "c8")
game.display_board()

game.make_move("d3", "e5")
game.display_board()

game.make_move("c8", "c4")
game.display_board()

game.make_move("e5", "c4")
game.display_board()

game.make_move("i10", "i8")
game.display_board()

game.make_move("g4", "f4")
game.display_board()

game.make_move("i8", "f8")
game.display_board()

game.make_move("g3", "h5")
game.display_board()

game.make_move("h10", "g8")
game.display_board()

game.make_move("e6", "e3")
game.display_board()





# # game.make_move("c10", "d8")
# # game.display_board()
# # game.make_move("a4", "a5")
# # game.display_board()
# # game.make_move("d8", "e6")
# # game.display_board()
#
#
# game.make_move("a10", "a9")
# game.display_board()
# game.make_move("a4", "a5")
# game.display_board()
# game.make_move("a9", "c9")
# game.display_board()
# game.make_move("a5", "a6")
# game.display_board()
# game.make_move("d10", "e10")
# game.display_board()
# game.make_move("a6", "a7")
# game.display_board()
# game.make_move("c9", "d9")
# game.display_board()
# game.make_move("a7", "a8")
# game.display_board()
# game.make_move("d9", "d10")
# game.display_board()
# game.make_move("a8", "a9")
# game.display_board()
# game.make_move("d10", "f8")
# game.display_board()
# game.make_move("e9", "e8")
# game.display_board()
# game.make_move("a9", "a10")
# game.display_board()
# game.make_move("d10", "f8")
# game.display_board()
# game.make_move("a10", "b10")
# game.display_board()
# game.make_move("f8", "f9")
# game.display_board()
# game.make_move("b10", "c10")
# game.display_board()
# game.make_move("e8", "f8")
# game.display_board()
# game.make_move("c10", "d10")
# game.display_board()
# game.make_move("f9", "e8")
# game.display_board()
# game.make_move("f9", "e9")
# game.display_board()
# game.make_move("d10", "c10")
# game.display_board()
# game.make_move("h10", "f9")
# game.display_board()
#
# game.make_move("c7", "c6")
# game.display_board()
# game.make_move("a4", "a5")
# game.display_board()
# game.make_move("a7", "b7")
# game.display_board()
# game.make_move("a5", "a6")
# game.display_board()
# game.make_move("b8", "b6")
# game.display_board()
# game.make_move("a6", "a7")
# game.display_board()
# game.make_move("b6", "b6")
# game.display_board()
# game.make_move("c4", "b4")
# game.display_board()
# game.make_move("c6", "c5")
# game.display_board()
# game.make_move("b4", "b4")
# game.display_board()
# game.make_move("c5", "b5")
# game.display_board()
# game.make_move("b4", "b4")
# game.display_board()
# game.make_move("b6", "b4")
# game.display_board()




