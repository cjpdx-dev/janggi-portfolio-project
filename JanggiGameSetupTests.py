import unittest
from JanggiGame import JanggiGame


class BoardInitializationTests(unittest.TestCase):

    def test_game_creation_and_initial_game_state(self):
        game = JanggiGame()
        game.start_game()

        self.assertEqual(game.get_game_state(), "UNFINISHED")

        self.assertEqual(game.get_current_player().get_player_color(), "BLUE")
        self.assertEqual(game.get_current_player().is_current_player(), True)

        self.assertEqual(game.get_next_player().get_player_color(), "RED")
        self.assertEqual(game.get_next_player().is_current_player(), False)

        self.assertEqual(game.is_in_check("BLUE"), False)
        self.assertEqual(game.is_in_check("RED"), False)

    def test_position_initialization_and_piece_placement(self):

        game = JanggiGame()
        game.start_game()

        test_placements = [["0"],
                           ["ch", "el", "hr", "gu", "**", "gu", "el", "hr", "ch"],
                           ["**", "**", "**", "**", "ge", "**", "**", "**", "**"],
                           ["**", "ca", "**", "**", "**", "**", "**", "ca", "**"],
                           ["so", "**", "so", "**", "so", "**", "so", "**", "so"],
                           ["**", "**", "**", "**", "**", "**", "**", "**", "**"],
                           ["**", "**", "**", "**", "**", "**", "**", "**", "**"],
                           ["SO", "**", "SO", "**", "SO", "**", "SO", "**", "SO"],
                           ["**", "CA", "**", "**", "**", "**", "**", "CA", "**"],
                           ["**", "**", "**", "**", "GE", "**", "**", "**", "**"],
                           ["CH", "EL", "HR", "GU", "**", "GU", "EL", "HR", "CH"],
                           ["0"]]

        initial_board_state = game.get_drawable_board_data()

        self.assertEqual(test_placements, initial_board_state)


class PieceInitializationTests(unittest.TestCase):
    starting_piece_positions = ()


if __name__ == '__main__':
    unittest.main()
