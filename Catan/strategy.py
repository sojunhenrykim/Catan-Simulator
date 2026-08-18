class Strategy:
    def __init__(self, name):
        self.name = name
    def choose_action(self, game, player):
        pass
    def choose_setup_settlement(self, game, player):
        pass

    def choose_setup_road(self, game, player, settlement):
        pass

    def choose_discard(self, game, player, amount):
        pass

    def choose_robber_tile(self, game, player):
        pass

    def choose_robber_victim(self, game, player, eligible_players):
        pass

    def choose_trade_target(self, game, player):
        pass

    def choose_bank_trade(self, game, player, tradeable_resources):
        pass

    def choose_player_trade(self, game, player, target_player):
        pass

    def choose_trade_response(self, game, player, offering_player, proposal):
        pass

    def choose_dev_card(self, game, player):
        pass

    def choose_free_road(self, game, player, road_number):
        pass

    def choose_resource(self, game, player, reason):
        pass
class HumanStrategy(Strategy):
    def __init__(self):
        super().__init__("Human")
    def choose_action(self, game, player):
        print(f"{player.name}'s resources:")
        print(player.resources)

        print(f"What would you like to do, {player.name}?")
        print("1. Build Road")
        print("2. Build Settlement")
        print("3. Build City")
        print("4. Buy Development Card")
        print("5. Trade")
        print("6. Use Development Card")
        print("7. End Turn")

        choice = input().strip()

        if choice == "1":
            vertices = input(
                "Enter two road vertices separated by a space: "
            ).split()

            if len(vertices) != 2:
                return {"type": "invalid"}

            return {
                "type": "build_road",
                "a": vertices[0],
                "b": vertices[1]
            }

        if choice == "2":
            vertex = input(
                "Where do you want to build your settlement? "
            ).strip()

            return {
                "type": "build_settlement",
                "vertex": vertex
            }

        if choice == "3":
            vertex = input(
                "Which settlement do you want to upgrade? "
            ).strip()

            return {
                "type": "build_city",
                "vertex": vertex
            }

        if choice == "4":
            return {"type": "buy_dev_card"}

        if choice == "5":
            return {"type": "trade"}

        if choice == "6":
            return {"type": "use_dev_card"}

        if choice == "7":
            return {"type": "end_turn"}

        return {"type": "invalid"}
    def choose_setup_settlement(self, game, player):
        return input(f"{player.name}, where do you want to place your settlement? ").strip()
    def choose_setup_road(self, game, player, settlement):
        vertices = input(f"{player.name}, enter two vertices for your road: ").split()
        if len(vertices) != 2:
            return None
        return (vertices[0], vertices[1])
    def choose_discard(self, game, player, amount):
        print(f"{player.name}'s resources:")
        print(player.resources)
        choices = input(f"Choose {amount} resources to discard,\nseparated by spaces: ").strip().lower().split()
        return choices
    def choose_robber_tile(self, game, player):
        choice = input(
            f'{player.name}, enter the new robber coordinates as "x,y": '
        ).strip()

        try:
            x, y = choice.split(",")
            return (int(x), int(y))
        except ValueError:
            return None
    def choose_robber_victim(self, game, player, eligible_players):
        print("Players you can steal from:")
        for eligible_player in eligible_players:
            print(f" - {eligible_player.name}")

        return input(
            f"{player.name}, enter the name of the player to steal from: "
        ).strip()
    def choose_trade_target(self, game, player):
        print(f"{player.name}, choose a trade partner:")
        for number, other_player in enumerate(game.players, start=1):
            print(f"{number}) {other_player.name}")
        print("5) Bank")

        choice = input().strip()
        if choice == "5":
            return "bank"

        try:
            return game.players[int(choice) - 1]
        except (ValueError, IndexError):
            return None
    def choose_bank_trade(self, game, player, tradeable_resources):
        print(f"Resources available for a 4:1 trade: {tradeable_resources}")
        give = input("Resource to give: ").strip().lower()
        receive = input("Resource to receive: ").strip().lower()
        return {"give": give, "receive": receive}
    def choose_player_trade(self, game, player, target_player):
        print(f"{player.name}, you are trading with {target_player.name}.")
        give = input("Resource to offer: ").strip().lower()
        receive = input("Resource to request: ").strip().lower()
        return {"give": give, "receive": receive}
    def choose_trade_response(self, game, player, offering_player, proposal):
        give = proposal.get("give")
        receive = proposal.get("receive")
        answer = input(
            f"{player.name}, accept 1 {give} from {offering_player.name} "
            f"for 1 {receive}? (yes/no): "
        ).strip().lower()
        return answer == "yes"
    def choose_dev_card(self, game, player):
        print(f"{player.name}, your development cards: {player.dvcards}")
        print("1) Knight\n2) Road Building\n3) Year of Plenty\n4) Monopoly")
        choices = {
            "1": "knight",
            "2": "road building",
            "3": "year of plenty",
            "4": "monopoly"
        }
        return choices.get(input("Choose a development card: ").strip())
    def choose_free_road(self, game, player, road_number):
        vertices = input(
            f"Choose free road {road_number}/2 (two vertices): "
        ).split()
        if len(vertices) != 2:
            return None
        return (vertices[0], vertices[1])
    def choose_resource(self, game, player, reason):
        return input(
            f"Choose a resource for {reason} "
            "(wood, brick, sheep, wheat, ore): "
        ).strip().lower()
