class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacenttiles = []
        self.neighbour = set()
        self.connectedroads = []
        self.owner = None
        self.building = None
