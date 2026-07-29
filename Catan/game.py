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
        self.turnnumber = (self.turnnumber+1)%4

