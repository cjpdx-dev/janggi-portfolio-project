import unittest
from JanggiGame import JanggiGame


class BoardInitializationTests(unittest.TestCase):
    def test_game_creation_and_initial_game_state(self):
        game = JanggiGame()
        game.start_game()

        self.assertEqual(game.get_game_state(), "UNFINISHED")

        self.assertEqual(game.get_current_player().get_player_color(), "BLUE")
        self.assertEqual(game.get_current_player().is_taking_turn(), True)

        self.assertEqual(game.get_next_player().get_player_color(), "RED")
        self.assertEqual(game.get_next_player().is_taking_turn(), False)

        self.assertEqual(game.is_in_check("BLUE"), False)
        self.assertEqual(game.is_in_check("RED"), False)


class BoardPositionInitializationTests(unittest.TestCase):
    pass


class PieceInitializationTests(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
