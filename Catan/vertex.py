class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacenttiles = []
        self.neighbour = set()
        self.connectedroads = []
