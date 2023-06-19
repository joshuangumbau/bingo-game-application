from player import Player
from game import Game
game = Game()
player1 = Player(name="player1")
player2 = Player(name="player2")

game.displayBoard(player1, player2)
while True:
    val = int(input(f"{player1.name}'s turn : "))
    player1.updatePlayerBoard(val)
    player2.updatePlayerBoard(val)
    game.displayBoard(player1, player2)
    if player1.checkBingo() and player2.checkBingo():
        print("DRAW")
        break
    if player1.checkBingo():
        print(f"{player1.name} WON")
        break
    if player2.checkBingo():
        print(f"{player2.name} WON")
        break
