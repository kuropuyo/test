# mapsquare.py

class MapSquare(object):
    def __init__(self, height, ground, coordinate):
        self.height = height
        self.ground = ground
        self.coordinate = coordinate
        self.unit = None

# neighborSquare : MapSquare, direction = {'n', 'e', 'w', 's'}
    def getNeighborSquare(self, direction):
        return self.neighbor_square[direction]

    def setNeighborSquare(self, direction, n_square):
        self.neighbor_square[direction] = n_square

# height : int
    def getHeight(self):
        return self.height

    def setHeight(self. height):
        self.height = height

# ground : string
    def getGround(self):
        return self.ground

    def setGround(self, ground):
        self.ground = ground

# coordinate : tuple
    def getCoordinate(self):
        return self.coordinate

    def setCoordinate(self, coordinate):
        self.coordinate = coordinate

    def getX(self):
        return self.coordinate[0]

    def getY(self):
        return self.coordinate[1]

# unit : Unit class
    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit

