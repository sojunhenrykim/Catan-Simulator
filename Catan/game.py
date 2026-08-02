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
        self.collectresource(result)
        print(f'{player.name} passes')
        self.endturn()
        return result
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
