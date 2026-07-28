from tile import Tile
import random
class Board:
    def __init__(self):
        self.tiles = []
        self.generateboard()

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
                    k.vertices = ['v1', 'v6', 'v7', 'v22', 'v23', 'v24']
                elif k.coord == (0,2):
                    k.vertices = ['v23', 'v24', 'v51', 'v52', 'v53', 'v54']
                elif k.coord == (0,-1):
                    k.vertices = ['v3', 'v4', 'v13', 'v14', 'v15', 'v16']
                elif k.coord == (0,-2):
                    k.vertices = ['v14', 'v15', 'v36', 'v37', 'v38', 'v39']
                elif k.coord == (1,0):
                    k.vertices = ['v1', 'v2', 'v7', 'v8', 'v9', 'v10']
                elif k.coord == (1,1):
                    k.vertices = ['v7', 'v8', 'v24', 'v25', 'v26', 'v54']
                elif k.coord == (1,-1):
                    k.vertices = ['v2', 'v3', 'v10', 'v11', 'v12', 'v13']
                elif k.coord == (1,-2):
                    k.vertices = ['v12', 'v13', 'v14', 'v34', 'v35', 'v36']
                elif k.coord == (2,0):
                    k.vertices = ['v8', 'v9', 'v36', 'v37', 'v38', 'v39']
                elif k.coord == (2,-1):
                    k.vertices = ['v9', 'v10', 'v11', 'v29', 'v30', 'v31']
                elif k.coord == (2,-2):
                    k.vertices = ['v11', 'v12', 'v31', 'v32', 'v33', 'v34']
                elif k.coord == (-1,0):
                    k.vertices = ['v4', 'v5', 'v16', 'v17', 'v18', 'v19']
                elif k.coord == (-1,1):
                    k.vertices = ['v5', 'v6', 'v19', 'v20', 'v21', 'v22']
                elif k.coord == (-1,2):
                    k.vertices = ['v21', 'v22', 'v23', 'v49', 'v50', 'v51']
                elif k.coord == (-1,-1):
                    k.vertices = ['v15', 'v16', 'v17', 'v39', 'v40', 'v41']
                elif k.coord == (-2,0):
                    k.vertices = ['v17', 'v18', 'v41', 'v42', 'v43', 'v44']
                elif k.coord == (-2,1):
                    k.vertices = ['v18', 'v19', 'v20', 'v44', 'v45', 'v46']
                elif k.coord == (-2,2):
                    k.vertices = ['v20', 'v21', 'v46', 'v47', 'v48', 'v49']
                              
             
             



