from game import Game

game = Game()
for tile in game.board.tiles:
    print(tile)
    print()
game.play()
