from game import Game

game = Game()
for tile in game.board.tiles:
    print(tile)
    if tile is game.board.robber:
        print("Robber is on this tile.")
game.play()
