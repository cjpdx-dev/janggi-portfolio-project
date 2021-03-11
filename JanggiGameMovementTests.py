import unittest
from JanggiGame import JanggiGame


class MoveGeneralTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class MoveGuardTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class MoveHorseTests(unittest.TestCase):
    def test_horse_cannot_move_over_own_piece(self):
        game = JanggiGame()
        game.display_board()

        game.make_move("c10", "d8")
        game.display_board()

        game.make_move("c1", "d3")
        game.display_board()

        game.make_move("c7", "d7")
        game.display_board()

        game.make_move("c4", "d4")
        game.display_board()

        game.make_move("d8", "c6")
        game.display_board()

        game.make_move("d8", "d8")
        game.display_board()

        game.make_move("d3", "d6")
        game.display_board()

        game.make_move("d3", "d3")
        game.display_board()

        game.make_move("h10", "g8")
        game.display_board()

        game.make_move("h2", "g3")


class MoveChariotTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class MoveElephantTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class MoveCannonTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class MoveSoliderTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class PostPieceMovementTests(unittest.TestCase):
    def test_player_switch(self):
        pass


if __name__ == '__main__':
    unittest.main()
