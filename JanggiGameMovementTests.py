import unittest
from JanggiGame import JanggiGame


class BasicMovementTests(unittest.TestCase):
    # Test that the conversion from algebraic notation to (x,y) coordinate
    # notation is successful or causes make_move() to return False
    pass


class FirstPassMoveValidityTests(unittest.TestCase):

    # Test that an attempted move from a position that holds no piece returns False

    # Test that an attempted from a position that holds a piece belonging to the
    # next player returns False

    # Test that an attempted move to a non-existent board position returns False

    # Test that an attempted move to a position which already holds a piece
    # belonging to the current player return False
    pass


# "Piece-specific" move tests

class MoveGeneralTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class MoveGuardTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class MoveHorseTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


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
