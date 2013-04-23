import re


class TicTacToeBoard:
    ALPHA_KEYS = {"A": 0, "B": 1, "C": 2}
    NUM_KEYS = {"3": 2, "2": 1, "1": 0}
    PLAYER_X = 'X'
    PLAYER_O = 'O'
    BOARD_SIZE = 3

    def __init__(self):
        self.board = [[" " for i in range(0, self.BOARD_SIZE)]
                      for i in range(0, self.BOARD_SIZE)]
        self.next_player = None
        self.moves_counter = 0
        self._game_status = "Game in progress."

        self.win_combinations = []
        self.win_combinations += [[(i, j) for i in range(0, self.BOARD_SIZE)]
                                  for j in range(0, self.BOARD_SIZE)]
        self.win_combinations += [[(i, j) for j in range(0, self.BOARD_SIZE)]
                                  for i in range(0, self.BOARD_SIZE)]
        self.win_combinations += [[(i, i) for i in range(0, self.BOARD_SIZE)]]
        self.win_combinations += [[(i, self.BOARD_SIZE-i-1)
                                   for i in range(0, self.BOARD_SIZE)]]

    def __str__(self):
        devider = "\n  -------------\n"
        result = "{}".format(devider)
        for i in reversed(range(0, 3)):
            result += "{} ".format(str(i+1))
            for j in range(0, 3):
                result += "| {} ".format(self.board[i][j])

            result += "|{}".format(devider)

        result += "    A   B   C  \n"
        return result

    def __setitem__(self, key, value):
        if not self._check_valid_key(key):
            raise InvalidKey("Invalid key!")

        if not self._check_valid_value(value):
            raise InvalidValue("Invalid value!")

        indexes = self._calculate_indexes(key)
        if self.board[indexes[0]][indexes[1]] != " ":
            raise InvalidMove("Invalid move!")

        if not self._check_your_turn(value):
            raise NotYourTurn

        self.board[indexes[0]][indexes[1]] = value
        self._update_game_status(indexes[0], indexes[1], value)

    def __getitem__(self, key):
        if not self._check_valid_key(key):
            raise InvalidKey("Invalid key!")

        indexes = self._calculate_indexes(key)
        return self.board[indexes[0]][indexes[1]]

    def _calculate_indexes(self, key):
        row = self.ALPHA_KEYS[key[0]]
        col = self.NUM_KEYS[key[1]]
        return (row, col)

    def game_status(self):
        return self._game_status

    def _update_game_status(self, row, col, player):
        self.moves_counter += 1
        for combination in self.win_combinations:
            filtered_combination = [pos for pos in combination 
                                    if self.board[pos[0]][pos[1]] == player]
            if len(filtered_combination) == self.BOARD_SIZE:
                self._game_status = "{} wins!".format(player)
                return

        if self.moves_counter == 9:
            self._game_status = "Draw!"

    def _check_valid_key(self, key):
        return re.match(r'(^([ABC][123])$)', key)

    def _check_valid_value(self, value):
        return re.match(r'(^[XO]$)', value)

    def _check_your_turn(self, player):
        if self.next_player is None or self.next_player == player:
            if player == self.PLAYER_X:
                self.next_player = self.PLAYER_O
            else:
                self.next_player = self.PLAYER_X
            return True

        return False


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass
