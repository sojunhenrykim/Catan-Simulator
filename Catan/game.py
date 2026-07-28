from board import Board
from player import Player
from dice import dice
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]
        self.turn = 0
    def turn(self):
        result = dice

