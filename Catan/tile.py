class Tile:
    def __init__(self, x: int, y:int, resource: str, number: int, vertices: list[str]):
        pass
        self.coord = (x,y)
        self.resource = resource
        self.number = number
        self.vertices = vertices
    def __str__(self):
        return (f'Coordinates:{self.coord}\nResource: {self.resource}\nNumber: {self.number}')

