from game import Game
from strategy import HumanStrategy
game = Game()
for player in game.players:
    player.strategy = HumanStrategy()
for tile in game.board.tiles:
    print(tile)
    if tile is game.board.robber:
        print("Robber is on this tile.")
game.play()
