import mapsquare

class Map(object):
    def __init__(self, x, y):
        self.array = []
        for i in range(x):
            self.array.append([])
            for j in range(y):
                ms = MapSquare(0, 'soil', (x, y))
                if i == 0:
                    ms.setNeighborSquare('w', None)
                else:
                    ms.setNeighborSquare('w', arr[i-1][j])
                if j == 0:
                    ms.setNeighborSquare('n', None)
                else:
                    ms.setNeighborSquare('n', arr[i][j-1])
                if i == x-1:
                    ms.setNeighborSquare('e', None)
                else:
                    ms.setNeighborSquare('e', arr[i+1][j])
                if j == y-1:
                    ms.setNeighborSquare('s', None)
                else:
                    ms.setNeighborSquare('s', arr[i][j+1])

                self.array[i].append(ms)



