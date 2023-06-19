from board import Board
class Player(Board):
    def __init__(self, name):
        self.name = name
        self.board = Board()

    def updatePlayerBoard(self, val):
        self.board.updateBoard(val)

    def checkBingo(self):
        return self.board.checkBingo()