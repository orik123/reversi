class Reversi:
    H_LINE = "  +---+---+---+---+---+---+---+---+"
    E_LINE = "  |   |   |   |   |   |   |   |   |"
    DIGITS1TO8 = "12345678"

    def __init__(self):
        self.board = None

    def start(self):
        self.init()
        self.print_board()
        while True:
            move = self.get_player_move()
            self.play_move(move)
            self.print_board()

    def init(self):
        self.board = []
        for i in range(8):
            self.board.append([" "] * 8)

        self.board[3][3] = "X"
        self.board[4][4] = "X"
        self.board[3][4] = "O"
        self.board[4][3] = "O"

    def print_board(self):
        print("    1   2   3   4   5   6   7   8")
        print(self.H_LINE)
        for i in range(8):
            print(self.E_LINE)
            print(f"{i + 1}", end=' ')
            for j in range(8):
                print(f"| {self.board[i][j]}", end=' ')
            print("|")
            print(self.E_LINE)
            print(self.H_LINE)

    def get_player_move(self):
        print("Please enter your move...")
        move = input()
        if self.is_valid_move(move):
            print(f"Your move is: {move}")
            return move
        else:
            return self.get_player_move()

    def is_valid_move(self, move: str) -> bool:
        if len(move) != 2:
            print("ERROR: Your move has to be exactly 2 digits!")
            return False

        if move[0] not in self.DIGITS1TO8 or move[1] not in self.DIGITS1TO8:
            print("ERROR: Your move has to include only digits between 1 and 8!")
            return False

        row = int(move[0]) - 1
        col = int(move[1]) - 1
        if self.board[row][col] != " ":
            print("ERROR: The cell is already occupied!")
            return False

        return True

    def play_move(self, move: str):
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        self.board[row][col] = "X"


if __name__ == '__main__':
    reversi = Reversi()
    reversi.start()
