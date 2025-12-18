class board():
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def checkWin(self):
        if self.hasWon('x'):
            return 'x'
        if self.hasWon('o'):
            return 'o'
        return 'n'

    def hasWon(self, player):

        # Checking every row
        if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
            return True
        if self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
            return True
        if self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
            return True

        # Checking every column
        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        if self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        if self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True

        # Checking every diag
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True

        # if player didn't win - return false
        return False

    def checkTie(self):
        for i in range(3):
            for ii in range(3):
                if self.board[i][ii] == "-":
                    return False

        return self.checkWin() == "n"

    def makeMove(self, player, row, col):

        if not self.checkEmpty(row, col):
            print("please make a move on empty space")
            return -1

        if not self.checkValidMove(player, row, col):
            print("please make a move on the board")
            return -1

        self.board[row][col] = player
        print(f"placed {player} in location [{row},{col}]")
        return player

    def checkEmpty(self, row, col):
        if row not in [0,1,2] or col not in [0,1,2]:
            return False

        if self.board[row][col] == "-":
            return True
        return False

    def checkValidMove(self, player, row, col):
        if player not in ['x', 'o']:
            return False
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            return False
        if not self.checkEmpty(row, col):
            return False
        return True

    def emptyBoard(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def displayBoard(self):
        print("-" * 13)
        for i in range(3):
            print("|", self.board[i][0], "|", self.board[i][1], "|", self.board[i][2], "|")
            print("-" * 13)

