from Board import Board


class Game:

    def __init__(self, player_1, player_2):

        self._state = "UNFINISHED"

        self.player_1 = player_1
        self.player_2 = player_2

        self._current_player = player_1
        self._next_player = player_2

        self._p1_pieces = player_1.get_pieces()
        self._p2_pieces = player_2.get_pieces()

        all_pieces = []
        for piece in self._p1_pieces:
            all_pieces.append(piece)
        for piece in self._p2_pieces:
            all_pieces.append(piece)

        self.game_board = Board(all_pieces)

    def start(self):

        print("Starting game...")

        while self.check_game_state() == "UNFINISHED":

            valid_input = False

            player_name = self._current_player
            print("Current player: ", player_name)

            while valid_input is False:
                print()
                print("Initial position: ", end="")
                current_position = self.get_player_input()
                if current_position is None:
                    print("Invalid Current Position")
                else:
                    print("New position: ", end="")
                    new_position = self.get_player_input()
                    if new_position is None:
                        print("Invalid New Position")
                    else:
                        if self.validate_turn(current_position, new_position) is True:
                            valid_input = True
                        else:
                            print("Invalid movement.")

    def get_player_input(self):

        player_position = input()
        if self.game_board.check_position_exists(player_position.lower()) is False:
            return None
        else:
            return player_position

    def validate_turn(self, current_position, new_position):
        return True

    def swap_turns(self):
        if self.player_1 == self._current_player:
            self._current_player = self.player_2
            self._next_player = self.player_1
        else:
            self._current_player = self.player_1
            self._next_player = self.player_2

    def update_game_state(self):
        pass

    def check_game_state(self):
        return self._state



