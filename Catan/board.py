from tile import Tile
from road import Road
import random
class Board:
    def __init__(self):
        self.tiles = []
        self.generateboard()
        self.roads = []
        self.generateroads()

    def generateboard(self):
        coordinates =[]
        numbers = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
        resources = ['wood','wood','wood','wood','sheep','sheep','sheep','sheep','wheat','wheat','wheat','wheat','brick','brick','brick','ore','ore','ore','desert']
        for k in range (-2,3):
            for l in range (-2,3):
                if abs(k+l) <=2:
                    coordinates.append((k,l))
        for (k,l) in coordinates:
            m = random.choice(resources)
            if m == "desert":
                    n = 7
                    self.tiles.append(Tile(k,l,m,n,[]))
                    resources.remove(m)
            else:   
                    n = random.choice(numbers)
                    self.tiles.append(Tile(k,l,m,n,[]))
                    numbers.remove(n)
                    resources.remove(m)
        for k in self.tiles:
                if k.coord == (0,0):
                    k.vertices = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']
                elif k.coord == (0,1):
                    k.vertices = ['v24', 'v7', 'v1', 'v6', 'v22', 'v23']
                elif k.coord == (0,2):
                    k.vertices = ['v53', 'v54', 'v24', 'v23', 'v51', 'v52']
                elif k.coord == (0,-1):
                    k.vertices = ['v3', 'v13', 'v14', 'v15', 'v16', 'v4']
                elif k.coord == (0,-2):
                    k.vertices = ['v14', 'v36', 'v37', 'v38', 'v39', 'v15']
                elif k.coord == (1,0):
                    k.vertices = ['v8', 'v9', 'v10', 'v2', 'v1', 'v7']
                elif k.coord == (1,1):
                    k.vertices = ['v25', 'v26', 'v8', 'v7', 'v24', 'v54']
                elif k.coord == (1,-1):
                    k.vertices = ['v10', 'v11', 'v12', 'v13', 'v3', 'v2']
                elif k.coord == (1,-2):
                    k.vertices = ['v12', 'v34', 'v35', 'v36', 'v14', 'v13']
                elif k.coord == (2,0):
                    k.vertices = ['v27', 'v28', 'v29', 'v9', 'v8', 'v26']
                elif k.coord == (2,-1):
                    k.vertices = ['v29', 'v30', 'v31', 'v11', 'v10', 'v9']
                elif k.coord == (2,-2):
                    k.vertices = ['v31', 'v32', 'v33', 'v34', 'v12', 'v11']
                elif k.coord == (-1,0):
                    k.vertices = ['v5', 'v4', 'v16', 'v17', 'v18', 'v19']
                elif k.coord == (-1,1):
                    k.vertices = ['v22', 'v6', 'v5', 'v19', 'v20', 'v21']
                elif k.coord == (-1,2):
                    k.vertices = ['v51', 'v23', 'v22', 'v21', 'v49', 'v50']
                elif k.coord == (-1,-1):
                    k.vertices = ['v16', 'v15', 'v39', 'v40', 'v41', 'v17']
                elif k.coord == (-2,0):
                    k.vertices = ['v18', 'v17', 'v41', 'v42', 'v43', 'v44']
                elif k.coord == (-2,1):
                    k.vertices = ['v20', 'v19', 'v18', 'v44', 'v45', 'v46']
                elif k.coord == (-2,2):
                    k.vertices = ['v49', 'v21', 'v20', 'v46', 'v47', 'v48']
                else:
                    continue
             
    def generateroads(self):
        roads = set()
        for tile in self.tiles:
            roads.add(tuple(sorted((tile.vertices[0],tile.vertices[1]))))
            roads.add(tuple(sorted((tile.vertices[1],tile.vertices[2]))))
            roads.add(tuple(sorted((tile.vertices[2],tile.vertices[3]))))
            roads.add(tuple(sorted((tile.vertices[3],tile.vertices[4]))))
            roads.add(tuple(sorted((tile.vertices[4],tile.vertices[5]))))
            roads.add(tuple(sorted((tile.vertices[5],tile.vertices[0]))))
        for a,b in roads:
            self.roads.append(Road(a,b))


             



