class TicTacToeBoard:
    PLAYERS = ("X", "O")
    KEYS = ("A3", "B3", "C3",
            "A2", "B2", "C2",
            "A1", "B1", "C1")
    WIN_COMBINATIONS = (("A1", "A2", "A3"),
                        ("B1", "B2", "B3"),
                        ("C1", "C2", "C3"),
                        ("A1", "B1", "C1"),
                        ("A2", "B2", "C2"),
                        ("A3", "B3", "C3"),
                        ("A3", "B2", "C1"),
                        ("A1", "B2", "C3"))
    GAME_IN_PROGRESS = "Game in progress."
    X_WINS = "X wins!"
    O_WINS = "O wins!"
    DRAW = "Draw!"
    BOARD_SIZE = 3

    def __init__(self):
        self.__board = {}
        self.__last_player = None
        self.__moves_counter = 0
        self.__game_status = self.GAME_IN_PROGRESS

    def __str__(self):
        return ("\n" +
                "  -------------\n" +
                "3 | {} | {} | {} |\n" +
                "  -------------\n" +
                "2 | {} | {} | {} |\n" +
                "  -------------\n" +
                "1 | {} | {} | {} |\n" +
                "  -------------\n" +
                "    A   B   C  \n").format(
                    *[self.__board.get(key, " ")
                      for key in self.KEYS])

    def __setitem__(self, key, value):
        if key not in self.KEYS:
            raise InvalidKey("Invalid key!")

        if value not in self.PLAYERS:
            raise InvalidValue("Invalid value!")

        elif key in self.__board:
            raise InvalidMove("Invalid move!")

        if self.__last_player == value:
            raise NotYourTurn

        self.__board[key] = value
        self.__last_player = value
        self.__update_game_status(key, value)

    def __getitem__(self, key):
        if key not in self.KEYS:
            raise InvalidKey("Invalid key!")

        return self.__board[key]

    def game_status(self):
        return self.__game_status

    def __update_game_status(self, key, player):
        if self.__game_status != self.GAME_IN_PROGRESS:
            return
        self.__moves_counter += 1
        player_win = len([comb for comb in self.WIN_COMBINATIONS
                          if self.__check_line(comb, player)])
        if player_win:
            self.__game_status = "{} wins!".format(player)
        elif self.__moves_counter == 9:
            self.__game_status = self.DRAW

    def __check_line(self, line, player):
        return all([self.__board.get(key, " ") == player
                    for key in line])


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass
