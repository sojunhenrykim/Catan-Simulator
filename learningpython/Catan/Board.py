class Tile:
    def __init__(self, x: int, y:int, resource: str, number: int, Verticies: list):
        pass
        self.x = x
        self.y = y
        self.resource = resource
        self.number = number
        self.verticies = Verticies
    def __str__(self):
        pass
        return (f'This tile is at ({self.x},{self.y})\nResource: {self.resource}')
class Verticies:
    def __init__(self, vertex_number: int, player: str, build: str):
        self.vertex_number = vertex_number
        self.player = player
        self.build = build


def create_coordinates():