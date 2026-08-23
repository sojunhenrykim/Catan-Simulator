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
        self.dvcard_list = (["knight"]*14 + ["victory point"]*5 + ["road building"]*2 + ["year of plenty"]*2 + ["monopoly"]*2)
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
        self.longest_road(player)
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
        player = self.currentplayer()
        for a, b in player.newdvcards.items():
            player.dvcards[a] += b
            player.newdvcards[a] = 0
        player.useddevcardthisturn = False
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
                v = k.strategy.choose_setup_settlement(self,k)
                if not self.settlementcheck(k, v, setup=True):
                    print("Invalid placement. Try again.")
                else:
                    self.buildsettlement(k, v, setup=True)
                    print(f'{k.name} placed a settlement at {v}.')
                    settlementbuilt = True
            roadbuilt = False
            while not roadbuilt:
                roadchoice = k.strategy.choose_setup_road(self,k,v)
                if roadchoice is None:
                    print("Please enter exactly two vertices")
                    continue
                a, b = roadchoice
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
                        v = k.strategy.choose_setup_settlement(self, k)
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
                        roadchoice = k.strategy.choose_setup_road(self,k,v)
                        if roadchoice is None:
                            print("Please enter exactly two vertices")
                            continue
                        a, b = roadchoice
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
            action = player.strategy.choose_action(self, player)
            actiontype = action.get("type")
            if actiontype == "build_road":
                a = action.get("a")
                b = action.get("b")
                if not self.roadcheck(player, a, b):
                    print("Invalid placement or insufficient resources.")
                    continue
                self.buildroad(player, a, b)
                print(f"{player.name} built a road between {a} and {b}.")
            elif actiontype == "build_settlement":
                vertex = action.get("vertex")

                if not self.settlementcheck(player, vertex):
                    print("Invalid placement or insufficient resources.")
                    continue
                self.buildsettlement(player, vertex)
                print(f"{player.name} built a settlement at {vertex}.")
            elif actiontype == "build_city":
                vertex = action.get("vertex")
                if not self.citycheck(player, vertex):
                    print("Invalid placement or insufficient resources.")
                    continue
                self.buildcity(player, vertex)
                print(f"{player.name} upgraded {vertex} to a city.")
            elif actiontype == "buy_dev_card":
                self.buy_devcard(player)
            elif actiontype == "trade":
                self.trade(player)
            elif actiontype == "use_dev_card":
                self.use_devcard(player)
            elif actiontype == "end_turn":
                print(f"{player.name} ended their turn.")
                break
            else:
                print("Invalid action. Try again.")
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
                amount = total_resources // 2
                while True:
                    choices = player.strategy.choose_discard(self, player, amount)
                    if len(choices) != amount:
                        print(f"You must select exactly {amount} resources.")
                        continue

                    resourcesremaining = player.resources.copy()
                    valid = True

                    for resource in choices:
                        if (resource not in resourcesremaining or resourcesremaining[resource] <= 0):
                            valid = False
                            break
                        resourcesremaining[resource] -= 1
                    if not valid:
                        print("Invalid discard selection. Try again.")
                        continue
                    player.resources = resourcesremaining
                    print(f"{player.name} discarded {amount} resources.")
                    break
    def move_robber(self, player):
        print(f'Current robber location: {self.board.robber.coord}')
        while True:
            coordinates = player.strategy.choose_robber_tile(self, player)
            if coordinates is None:
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
            while True:
                steal_choice = player.strategy.choose_robber_victim(
                    self,
                    player,
                    eligible_players
                )
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
        trade_player = player.strategy.choose_trade_target(self, player)
        if trade_player is None:
            print("Invalid choice. Please select a valid option.")
            return

        if trade_player == "bank":
            tradeable_resources = []
            for resource in player.resources:
                if player.resources[resource] >= 4:
                    tradeable_resources.append(resource)
            if len(tradeable_resources) == 0:
                print("You do not have enough resources to trade with the bank.")
                return

            proposal = player.strategy.choose_bank_trade(
                self,
                player,
                tradeable_resources
            )
            trade_choice = proposal.get("give")
            receive_choice = proposal.get("receive")
            resources = ["wood", "brick", "sheep", "wheat", "ore"]

            if (
                trade_choice not in tradeable_resources
                or receive_choice not in resources
                or trade_choice == receive_choice
            ):
                print("Invalid choice or insufficient resources. Try again.")
                return

            player.resources[trade_choice] -= 4
            player.resources[receive_choice] += 1
            print(
                f'{player.name} traded 4 {trade_choice} to the bank '
                f'for 1 {receive_choice}.'
            )
            return

        if trade_player not in self.players or trade_player is player:
            print("You cannot trade with that player.")
            return

        proposal = player.strategy.choose_player_trade(
            self,
            player,
            trade_player
        )
        offer_resource = proposal.get("give")
        request_resource = proposal.get("receive")

        if offer_resource not in player.resources or player.resources.get(offer_resource, 0) <= 0:
            print("Invalid choice or insufficient resources. Try again.")
            return
        if request_resource not in trade_player.resources or trade_player.resources.get(request_resource, 0) <= 0:
            print(f"{trade_player.name} does not have enough {request_resource}.")
            return
        if offer_resource == request_resource:
            print("You cannot offer and request the same resource.")
            return

        accepted = trade_player.strategy.choose_trade_response(
            self,
            trade_player,
            player,
            proposal
        )
        if not accepted:
            print(f'{trade_player.name} declined the trade.')
            return

        player.resources[offer_resource] -= 1
        player.resources[request_resource] += 1
        trade_player.resources[offer_resource] += 1
        trade_player.resources[request_resource] -= 1
        print(
            f'Trade completed: {player.name} gave 1 {offer_resource} '
            f'to {trade_player.name} and received 1 {request_resource}.'
        )
    def buy_devcard(self, player):
        dvcard_list = self.dvcard_list
        if len(dvcard_list) == 0:
            print("No development cards left to buy.")
            return False
        if not self.canafford(player, dvcard_cost):
            print("Insufficient resources to buy a development card.")
            return False
        self.pay(player, dvcard_cost)
        print(f'{player.name} bought a development card.')
        pick = random.choice(dvcard_list)
        dvcard_list.remove(pick)
        if pick == "knight":
            player.newdvcards["knight"] += 1
            print(f'{player.name} received a Knight card.')
        if pick == "victory point":
            player.vp += 1
            print(f'{player.name} received a Victory Point.')
        if pick == "road building":
            player.newdvcards["road building"] += 1
            print(f'{player.name} received a Road Building card.')
        if pick == "year of plenty":
            player.newdvcards["year of plenty"] += 1
            print(f'{player.name} received a Year of Plenty card.')
        if pick == "monopoly":
            player.newdvcards["monopoly"] += 1
            print(f'{player.name} received a Monopoly card.')
        return True
    def use_devcard(self, player):
        if player.useddevcardthisturn:
            print("You have already used a development card this turn.")
            return
        if sum(player.dvcards.values()) == 0:
            print("You have no development cards to use.")
            return
        card_choice_actual = player.strategy.choose_dev_card(self, player)
        if card_choice_actual not in player.dvcards:
            print("Invalid choice. Please select a valid option.")
            return
        if  player.dvcards[card_choice_actual] <= 0:
            print("Invalid choice or you do not have that card. Try again.")
            return
        player.useddevcardthisturn = True
        if card_choice_actual == "knight":
            player.dvcards["knight"] -= 1
            print(f'{player.name} used a Knight card.')
            self.move_robber(player)
            player.armysize += 1
            if player.armysize >= 3 and not player.largest_army:
                if player.armysize > max(p.armysize for p in self.players if p is not player):
                    print(f'{player.name} has the Largest Army with {player.armysize} knights!')
                    player.vp += 2
                    player.largest_army = True
                    for p in self.players:
                        if p is player:
                            continue
                        else:
                            if p.largest_army == True:
                                p.vp -= 2
                                p.largest_army = False
        elif card_choice_actual == "road building":         
            print(f'{player.name} used a Road Building card. You can build two roads for free.')
            k = 0
            while k <2:
                legalroads = self.legal_roads(player, setup=True)
                if not legalroads:
                    print(f'{player.name} has no legal roads remaining.')
                    break
                vertices = player.strategy.choose_free_road(self, player, k + 1)
                if vertices is None:
                    print("Please enter exactly two vertices.")
                    continue
                a, b = vertices
                if not self.roadcheck(player, a, b, setup=True):
                    print("Invalid placement. Try again.")
                    continue
                else:
                    for resource, amount in road_cost.items():
                        player.resources[resource] += amount
                    self.buildroad(player, a, b)
                    print(f'{player.name} built a road between {a} and {b}.')
                    k += 1
            player.dvcards["road building"] -= 1
        elif card_choice_actual == "year of plenty": 
            print(f'{player.name} used a Year of Plenty card. You can take any two resources from the bank.')
            resources_taken = 0
            while resources_taken < 2:
                resource_choice = player.strategy.choose_resource(
                    self,
                    player,
                    "Year of Plenty"
                )
                if resource_choice not in ['wood', 'brick', 'sheep', 'wheat', 'ore']:
                    print("Invalid resource choice. Try again.")
                else:
                    player.resources[resource_choice] += 1
                    print(f'{player.name} took 1 {resource_choice} from the bank.')
                    resources_taken += 1
            player.dvcards["year of plenty"] -= 1
        elif card_choice_actual == "monopoly":
            print(f'{player.name} used a Monopoly card. You can choose a resource type and take all of that resource from other players.')
            while True:
                resource_choice = player.strategy.choose_resource(
                    self,
                    player,
                    "Monopoly"
                )
                if resource_choice in ['wood', 'brick', 'sheep', 'wheat', 'ore']:
                    break
                print("Invalid resource choice. Try again.")
            total_taken = 0
            for other_player in self.players:
                if other_player is not player:
                    amount = other_player.resources[resource_choice]
                    total_taken += amount
                    other_player.resources[resource_choice] = 0
            player.resources[resource_choice] += total_taken
            print(f'{player.name} took {total_taken} {resource_choice} from other players.')
            player.dvcards["monopoly"] -= 1
    def longest_road_check(self,player):
        owned_roads = set(player.roads)
        if len(owned_roads) == 0:
            return 0
        def search(vertexname, usedroads, started=False):
            vertex = self.board.vertices[vertexname]
            if (started and vertex.owner is not None and vertex.owner is not player):
                return 0
            longest = 0
            for road in owned_roads:
                if road in usedroads:
                    continue
                a, b = road
                if vertexname == a:
                    nextvertex = b
                elif vertexname == b:
                    nextvertex = a
                else:
                    continue
                newusedroads = usedroads | {road}
                length = 1+search(nextvertex, newusedroads, started = True)
                longest = max(longest, length)
            return longest
        vertices = set()
        for a, b in owned_roads:
            vertices.add(a)
            vertices.add(b)
        return max(search(vertexname, set()) for vertexname in vertices)
    def longest_road(self, player):
        for p in self.players:
            p.roadsize = self.longest_road_check(p)
        roadsize = player.roadsize
        if roadsize < 5 and player.longest_road:
            player.longest_road = False
            player.vp -=2
        if roadsize >= 5 and not player.longest_road:
            if roadsize > max(p.roadsize for p in self.players if p is not player):
                            print(f'{player.name} has the longest road with {roadsize} connected roads!')
                            player.vp += 2
                            player.longest_road = True
                            for p in self.players:
                                if p is player:
                                    continue
                                else:
                                    if p.longest_road == True:
                                        p.vp -= 2
                                        p.longest_road = False
    def legal_settlements(self, player, setup = False):
        legal = []
        for vertexname in self.board.vertices:
            if self.settlementcheck(player, vertexname, setup):
                legal.append(vertexname)
        return legal
    def legal_roads(self, player, setup=False, settlement = None):
        legal = []
        for road in self.board.roads:
            if settlement is not None:
                if settlement not in (road.v1, road.v2):
                    continue
            if self.roadcheck(player, road.v1, road.v2, setup):
                legal.append((road.v1,road.v2))
        return legal
    def legal_cities(self, player):
        legal = []
        for vertexname in player.settlements:
            if self.citycheck(player, vertexname):
                legal.append(vertexname)
        return legal
