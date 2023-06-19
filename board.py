import random

class Board:
    def __init__(self):
        self.position = {}
        self.playBoard = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        self.bingo = {
            "row" : [0,0,0,0,0],
            "col" : [0,0,0,0,0],
            "diagonal" : [0,0]
        }
        self.createBoard()

    def createBoard(self):
        choices = [i for i in range(1,26)]
        for i in range(5):
            for j in range(5):
                choice = random.choice(choices)
                self.playBoard[i][j] = choice
                choices.pop(choices.index(choice))
                self.position[choice] = (i,j)

    def updateBoard(self, val):
        x,y = self.position[val]
        self.playBoard[x][y] = 'X'
        self.updateBingo(x,y)

    def updateBingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1
        if x==y==2:
            self.bingo["diagonal"][0] += 1
            self.bingo["diagonal"][1] += 1
        elif x==y:
            self.bingo["diagonal"][0] += 1
        elif x+y == 4:
            self.bingo["diagonal"][1] += 1

    def checkBingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"] or 5 in self.bingo["diagonal"]