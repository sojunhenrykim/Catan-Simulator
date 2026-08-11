class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {"wood":0,"brick":0, "sheep":0,"wheat":0,"ore":0}
        self.roads = []
        self.settlements = []
        self.cities = []
        self.vp = 0
        self.dvcards = {"knight": 0, "victory point": 0, "road building": 0, "year of plenty": 0, "monopoly": 0}
    def buildroad(self,a,b):
        self.roads.append(tuple(sorted((a,b))))
    def buildsettlement(self,v):
        self.settlements.append(v)
        self.vp += 1
    def __str__(self):
        return f'{self.name}: {self.vp} VP'