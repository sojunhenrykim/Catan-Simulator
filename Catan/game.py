from board import Board
from player import Player
from dice import roll
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]
        self.turnnumber = 0
    def taketurn(self):
        result = roll()
        print(f"Player {self.turnnumber+1} rolled {result}")
        self.collectresource(result)
        self.turnnumber = (self.turnnumber+1)%4
    def collectresource(self, result):
        if result == 7:
            return
        for tile in self.board.tiles:
            if tile.number == result:
                for player in self.players:
                    for vertex in player.settlements:
                        if vertex in tile.vertices:
                            player.resources[tile.resource]  += 1
                    for vertex in player.cities:
                        if vertex in tile.vertices:
                            player.resources[tile.resource] += 2
