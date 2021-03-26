

class Position:

    def __init__(self):
        self._is_palace = False
        self._current_piece = None

    def check_if_palace(self):
        return self._is_palace

    def get_current_piece(self):
        return self._current_piece

    def set_current_piece(self, new_piece):
        self._current_piece = new_piece
