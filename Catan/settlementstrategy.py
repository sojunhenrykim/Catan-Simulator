import random
from strategy import Strategy
class SettlementStrategy(Strategy):
    def __init__(self):
        super().__init__("Settlement")
    def choose_setup_settlement(self, game, player):
        legal = game.legal_settlements(player, setup = True)
        return random.choice(legal)
    def choose_setup_road(self,game, player, settlement):
        legal = game.legal_roads(player, setup=True, settlement=settlement)
        return random.choice(legal)
    def choose_action(self, game, player):
        actions = [{"type": "end_turn"}]
        roads = game.legal_roads(player)
        if roads:
            a, b = random.choice(roads)
            actions.append({"type": "build_road","a": a,"b": b})
        settlements = game.legal_settlements(player)
        if settlements:
            for k in range (10):
                actions.append({"type": "build_settlement","vertex": random.choice(settlements)})
        cities = game.legal_cities(player)
        if cities:
            actions.append({"type": "build_city","vertex": random.choice(cities)})
        devcardcost = {"sheep": 1,"wheat": 1,"ore": 1}
        if (game.dvcard_list and game.canafford(player, devcardcost)):
            actions.append({"type": "buy_dev_card"})
        if any(amount >= 4 for amount in player.resources.values()):
            actions.append({"type": "trade"})
        usablecards = [card for card, amount in player.dvcards.items() if amount > 0 and card != "victory point"]
        if usablecards and not player.useddevcardthisturn:
            actions.append({"type": "use_dev_card"})
        return random.choice(actions)
    def choose_discard(self, game, player, amount):
        cards = []
        for resource, quantity in player.resources.items():
            cards.extend([resource]*quantity)
        return random.sample(cards, amount)
    def choose_robber_tile(self, game, player):
        available = [tile for tile in game.board.tiles if tile is not game.board.robber]
        return random.choice(available).coord
    def choose_robber_victim(self,game,player,eligible_players):
        return random.choice(eligible_players).name
    def choose_trade_target(self, game, player):
        return "bank"
    def choose_bank_trade(self,game,player,tradeable_resources):
        give = random.choice(tradeable_resources)
        resources = ["wood","brick", "sheep","wheat","ore"]
        resources.remove(give)
        receive = random.choice(resources)
        return {"give": give,"receive": receive}
    def choose_trade_response(self,game,player,offering_player,proposal):
        return random.choice([True, False])
    def choose_player_trade(self,game,player,target_player):
        return None
    def choose_dev_card(self, game, player):
        available = [card for card, amount in player.dvcards.items()if amount > 0 and card != "victory point"]
        return random.choice(available)
    def choose_free_road(self, game, player, road_number):
        legal = game.legal_roads(player, setup=True)
        if not legal:
            return None
        return random.choice(legal)
    def choose_resource(self, game, player, reason):
        return random.choice(["wood", "wood", "brick", "brick", "sheep", "sheep", "wheat", "wheat", "ore"])