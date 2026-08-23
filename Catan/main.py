from game import Game
from strategy import HumanStrategy
from randomstrategy import RandomStrategy
from settlementstrategy import SettlementStrategy
from longestroadstrategy import LongestroadStrategy
from citystrategy import CityStrategy
from devcardstrategy import DevcardStrategy


total_turn = 0
Player1_total_vp = 0
Player2_total_vp = 0
Player3_total_vp = 0
Player4_total_vp = 0
Player1_wins = 0
Player2_wins = 0
Player3_wins = 0
Player4_wins = 0
gamecount = 10000
for k in range (gamecount):
    game = Game()
    game.players[0].strategy = SettlementStrategy()
    game.players[1].strategy = LongestroadStrategy()
    game.players[2].strategy = DevcardStrategy()
    game.players[3].strategy = CityStrategy()
    winner = game.play()
    for tile in game.board.tiles:
        print(tile)
        if tile is game.board.robber:
            print("Robber is on this tile.")
    total_turn += game.turnnumber - 1
    if winner.name == "Player 1":
        Player1_wins += 1
    if winner.name == "Player 2":
            Player2_wins += 1
    if winner.name == "Player 3":
            Player3_wins += 1
    if winner.name == "Player 4":
            Player4_wins += 1
    for k in game.players:
        if k.name == "Player 1":
            Player1_total_vp += k.vp
        if k.name == "Player 2":
            Player2_total_vp += k.vp
        if k.name == "Player 3":
            Player3_total_vp += k.vp
        if k.name == "Player 4":
            Player4_total_vp += k.vp
print(f'Settlement Strategy: {Player1_wins} wins\n          average vp: {(Player1_total_vp)/(gamecount)}\n          win rate: {100*(Player1_wins)/(gamecount)}%')
print(f'Longest Road Strategy: {Player2_wins} wins\n          average vp: {(Player2_total_vp)/(gamecount)}\n          win rate: {100*(Player2_wins)/(gamecount)}%')
print(f'Development Card Strategy: {Player3_wins} wins\n          average vp: {(Player3_total_vp)/(gamecount)}\n          win rate: {100*(Player3_wins)/(gamecount)}%')
print(f'City Strategy: {Player4_wins} wins\n          average vp: {(Player4_total_vp)/(gamecount)}\n          win rate: {100*(Player4_wins)/(gamecount)}%')

    

    
