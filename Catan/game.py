from board import Board
from player import Player
from dice import roll
import random
road_cost = {"wood":1,"brick":1}
settlement_cost = {"wood":1,"brick":1, "sheep" :1, "wheat":1}
city_cost = {"wheat" :2, "ore":3}
dvcard_cost = {"sheep":1, "wheat":1, "ore":1}

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]
        self.currentplayernumber = 0
        self.turnnumber = 1
    def taketurn(self):
        player = self.currentplayer()
        result = roll()
        print(f'{player.name} rolled {result}')
        if result == 7:
            self.discard()
            self.move_robber(player)
        else:
            self.collectresource(result)
        self.action(player)
        self.endturn()
        return result
    def collectresource(self, result):
        for tile in self.board.tiles:
            if tile is not self.board.robber and tile.number == result:
                for player in self.players:
                    for vertex in player.settlements:
                        if vertex in tile.vertices:
                            player.resources[tile.resource]  += 1
                    for vertex in player.cities:
                        if vertex in tile.vertices:
                            player.resources[tile.resource] += 2
    def canafford(self, player, cost):
        for resource, amount in cost.items():
            if player.resources[resource] < amount:
                return False
        return True
    def pay(self, player, cost):
        for resource, amount in cost.items():
            player.resources[resource] -= amount
    def settlementcheck(self, player,vertex, setup=False):
        if vertex not in self.board.vertices:
            return False
        vertex = self.board.vertices[vertex]
        if len(player.settlements) >= 5:
            return False
        if vertex.building is not None:
            return False
        for k in vertex.neighbour:
            neighbour = self.board.vertices[k]
            if neighbour.building is not None:
                return False
        if not setup:
            connected = False
            for road in vertex.connectedroads:
                if road.owner is player:
                    connected = True
            if not connected:
                return False
            if not self.canafford(player, settlement_cost):
                return False
        return True
    def buildsettlement(self, player, vertexname, setup = False):
        if not self.settlementcheck(player, vertexname, setup):
            return False
        vertex = self.board.vertices[vertexname]
        vertex.owner = player
        vertex.building = "settlement"
        player.settlements.append(vertexname)
        player.vp +=1
        if not setup:
            self.pay(player, settlement_cost)
        return True
    def findroad(self, a, b):
        for road in self.board.roads:
            if {road.v1, road.v2} == {a,b}:
                return road
        return None
    def roadcheck(self, player, a, b, setup=False):
        road = self.findroad(a,b)
        if road is None:
            return False
        if road.owner is not None:
            return False
        if len(player.roads)>= 15:
            return False
        connected = False
        for k in (a,b):
            vertex = self.board.vertices[k]
            if vertex.owner is player:
                connected = True
                break
            if vertex.owner is not None:
                continue
            for connectedroad in vertex.connectedroads:
                if connectedroad.owner is player:
                    connected = True
                    break
            if connected:
                break
        if not connected:
            return False
        if not setup:
                if not self.canafford(player, road_cost):
                    return False
        return True
    def buildroad(self, player, a, b, setup = False):
        if not self.roadcheck(player, a, b, setup):
            return False
        road = self.findroad(a,b)
        road.owner = player
        player.roads.append(tuple(sorted((a,b))))
        if not setup:
            self.pay(player, road_cost)
        return True
    def citycheck(self, player, vertexname, setup=False):
        if vertexname not in self.board.vertices:
            return False
        if vertexname not in player.settlements:
            return False
        vertex = self.board.vertices[vertexname]
        if vertex.owner is not player:
            return False
        if vertex.building != "settlement":
            return False

        if len(player.cities)>=4:
            return False
        if setup:
            return False
        if not self.canafford(player, city_cost):
            return False
        return True
    def buildcity(self, player, vertexname, setup=False):
        if not self.citycheck(player, vertexname, setup):
            return False
        vertex = self.board.vertices[vertexname]
        vertex.building = "city"
        player.settlements.remove(vertexname)
        player.cities.append(vertexname)
        player.vp +=1
        self.pay(player, city_cost)
        return True
    def currentplayer(self):
        return self.players[self.currentplayernumber]
    def endturn(self):
        self.currentplayernumber = (self.currentplayernumber + 1) % 4
        self.turnnumber += 1
    def setuporder(self):
        random.shuffle(self.players)
        return self.players.copy()
    def setup(self):
        playerorder = self.setuporder()
        for k in playerorder:
            settlementbuilt = False
            while not settlementbuilt:
                v = input(f'{k.name}, where do you want to place your first settlement?')
                if not self.settlementcheck(k, v, setup=True):
                    print("Invalid placement. Try again.")
                else:
                    self.buildsettlement(k, v, setup=True)
                    print(f'{k.name} placed a settlement at {v}.')
                    settlementbuilt = True
            roadbuilt = False
            while not roadbuilt:
                a = input(f'{k.name}, where do you want to place your first road? Please enter two vertices separated by a space.')
                a,b = a.split()
                if v not in (a,b):
                    print("Road must be connected to your settlement. Try again.")
                elif not self.roadcheck(k, a, b, setup=True):
                    print("Invalid placement. Try again.")
                else:
                    self.buildroad(k, a, b, setup=True)
                    print(f'{k.name} placed a road between {a} and {b}.')
                    roadbuilt = True
        playerorder.reverse()
        for k in playerorder:
                    settlementbuilt = False
                    while not settlementbuilt:
                        v = input(f'{k.name}, where do you want to place your second settlement?')
                        if not self.settlementcheck(k, v, setup=True):
                            print("Invalid placement. Try again.")
                        else:
                            self.buildsettlement(k, v, setup=True)
                            print(f'{k.name} placed a settlement at {v}.')
                            for tile in self.board.tiles:
                                if v in tile.vertices and tile.resource != "desert":
                                    k.resources[tile.resource] += 1
                            settlementbuilt = True
                    roadbuilt = False
                    while not roadbuilt:
                        a = input(f'{k.name}, where do you want to place your second road? Please enter two vertices separated by a space.')
                        a,b = a.split()
                        if v not in (a,b):
                            print("Road must be connected to your settlement. Try again.")
                        elif not self.roadcheck(k, a, b, setup=True):
                            print("Invalid placement. Try again.")
                        else:
                            self.buildroad(k, a, b, setup=True)
                            print(f'{k.name} placed a road between {a} and {b}.')
                            roadbuilt = True
    def action(self, player):
        while True:
            print(f"{player.name}'s resources\n{player.resources}\nWhat would you like to do, {player.name}?\n")
            print('1. Build Road\n2. Build Settlement\n3. Build City\n4. Buy Development Card\n5. Trade\n6. End Turn')
            choice = input().strip()
            if choice == "1":
                vertices = input(f'Where do you want to place your road? Please enter two vertices separated by a space.').split()
                if len(vertices) != 2:
                    print("Please enter exactly two vertices.")
                    continue
                a, b = vertices
                if not self.roadcheck(player, a, b):
                    print("Invalid placement or insufficient resources. Try again.")
                else:
                    self.buildroad(player, a, b)
                    print(f'{player.name} built a road between {a} and {b}.')
            elif choice == "2":
                v = input(f'Where do you want to place your settlement?')
                if not self.settlementcheck(player, v):
                    print("Invalid placement or insufficient resources. Try again.")
                else:
                    self.buildsettlement(player, v)
                    print(f'{player.name} built a settlement at {v}.')
            elif choice == "3":
                v = input(f'Which settlement do you want to upgrade to a city?')
                if not self.citycheck(player, v):
                    print("Invalid placement or insufficient resources. Try again.")
                else:
                    self.buildcity(player, v)
                    print(f'{player.name} upgraded settlement at {v} to a city.')
            elif choice == "4":
                print("Buying development card is not implemented yet.")
            elif choice == "5":
                self.trade(player)
            elif choice == "6":
                print(f'{player.name} ended their turn.')
                break
            else:
                print("Invalid choice. Please select a valid option.")
    def winner(self):
        for player in self.players:
            if player.vp >= 10:
                return player
        return None
    def play(self):
        print("Welcome to Catan!")
        self.setup()
        while self.winner() is None:
            self.taketurn()
        winner = self.winner()
        print(f'Congratulations {winner.name}, you have won the game with {winner.vp} victory points!')
        return winner
    def discard(self):
        for player in self.players:
            total_resources = sum(player.resources.values())
            if total_resources <= 7:
                continue
            else:
                remaining = total_resources // 2
                print(f'{player.name}, you have {total_resources} resources. You must discard {remaining} resources.')
                print(f'Your resources: {player.resources}')
                while remaining>0:
                    discard_choice = input(f'Enter the resource you want to discard (remaining to discard: {remaining}): ').strip().lower()
                    if discard_choice not in player.resources or player.resources[discard_choice] <= 0:
                        print("Invalid choice or insufficient resources. Try again.")
                    else:
                        player.resources[discard_choice] -= 1
                        remaining -= 1
                print(f'{player.name} has discarded the required resources. Remaining resources: {player.resources}')
    def move_robber(self, player):
        print(f'Current robber location: {self.board.robber.coord}')
        while True:
            choice = input(f'{player.name}, please enter the new coordinates for the robber in the format "x,y": ').strip()
            try:
                x,y = choice.split(",")
                coordinates = (int(x), int(y))
            except ValueError:
                print("Invalid format. Please enter coordinates in the format 'x,y'.")
                continue
            newtile = next((tile for tile in self.board.tiles if tile.coord == coordinates), None)
            if newtile is None:
                print("Invalid tile coordinates. Please try again.")
                continue
            if newtile is self.board.robber:
                print("The robber is already on this tile. Please choose a different tile.")
                continue
            self.board.robber = newtile
            print(f'Robber moved to {coordinates}.')
            break
        eligible_players = []
        for other_player in self.players:
            if other_player is not player and sum(other_player.resources.values())>0:
                for k in other_player.settlements + other_player.cities:
                    if k in self.board.robber.vertices:
                        eligible_players.append(other_player)
                        break
        if len(eligible_players) == 0:
            print("No players to steal from.")
            return
        else:
            print("Players you can steal from:")
            for p in eligible_players:
                print(f" - {p.name}")
            while True:
                steal_choice = input(f'{player.name}, enter the name of the player you want to steal from: ').strip()
                target_player = next((p for p in eligible_players if p.name == steal_choice), None)
                if target_player is None:
                    print("Invalid player name. Please choose from the eligible players.")
                    continue
                else:
                    cards = []
                    for resource, count in target_player.resources.items():
                        cards.extend([resource]*count)
                    stolen_resource = random.choice(cards)
                    target_player.resources[stolen_resource] -= 1
                    player.resources[stolen_resource] += 1
                    print(f'{player.name} stole 1 {stolen_resource} from {target_player.name}.')
                    break
    def trade(self, player):
        print(f'{player.name}, please enter the number of the player you want to trade with: ')
        print("1) Player 1")
        print("2) Player 2")
        print("3) Player 3")
        print("4) Player 4")
        trade_player = input('5) Bank').strip()
        if trade_player not in ['1','2','3','4','5']:
            print("Invalid choice. Please select a valid option.")
            return
        if trade_player == '5':
            tradeable_resources = []
            for k in player.resources:
                if player.resources[k] >= 4:
                    tradeable_resources.append(k)
            if len(tradeable_resources) == 0:
                print("You do not have enough resources to trade with the bank.")
                return
            print(f'{player.name}, you can trade with the bank with the following resources: {player.resources}')
            trade_choice = input(f'{player.name}, please enter the resource you want to trade to the bank: ').strip().lower()
            if trade_choice not in tradeable_resources:
                print("Invalid choice or insufficient resources. Try again.")
                return
            else:
                player.resources[trade_choice] -= 4
                print(f'{player.name}, you traded 4 {trade_choice} to the bank.')
                receive_choice = input(f'{player.name}, please enter the resource you want to receive from the bank: ').strip().lower()
                if receive_choice not in ['wood','brick','sheep','wheat','ore'] or trade_choice == receive_choice:
                    print("Invalid choice. Please select a valid resource.")
                    player.resources[trade_choice] += 4
                    return
                else:
                    player.resources[receive_choice] += 1
                    print(f'{player.name}, you have received 1 {receive_choice} from the bank.')
        if trade_player in ['1','2','3','4']:
            target_player = self.players[int(trade_player) - 1]
            if target_player is player:
                print("You cannot trade with yourself.")
                return
            trade_player = target_player
            print(f'{player.name}, you are trading with {trade_player.name}.')
            offer_resource = input(f'{player.name}, please enter the resource you want to offer: ').strip().lower()
            if offer_resource not in player.resources or player.resources[offer_resource] <= 0:
                print("Invalid choice or insufficient resources. Try again.")
                return
            request_resource = input(f'{player.name}, please enter the resource you want to request: ').strip().lower()
            if request_resource not in trade_player.resources or trade_player.resources[request_resource] <= 0:
                print(f"{trade_player.name} does not have enough {request_resource}. Trade cannot proceed.")
                return
            elif offer_resource == request_resource:
                print("You cannot offer and request the same resource. Trade cannot proceed.")
                return
            accept_trade = input(f'{trade_player.name}, do you accept the trade? (yes/no): ').strip().lower()
            if accept_trade == 'yes':
                player.resources[offer_resource] -= 1
                player.resources[request_resource] += 1
                trade_player.resources[offer_resource] += 1
                trade_player.resources[request_resource] -= 1
                print(f'Trade completed: {player.name} gave 1 {offer_resource} to {trade_player.name} and received 1 {request_resource}.')
            else:
                print(f'{trade_player.name} declined the trade.')
