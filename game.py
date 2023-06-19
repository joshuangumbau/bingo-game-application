class Game:
    def displayBoard(self, player1, player2):
        board1 = player1.board.playBoard
        board2 = player2.board.playBoard
        size = 20
        p1len = len(player1.name)
        print(player1.name+" "*(size-p1len+1)+player2.name)
        for i in range(5):
            for j in board1[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif j>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print("      ",end="")
            for j in board2[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif j>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print()
        print()
