from itertools import permutations

directions = [
    [1, -2],
    [2, -1],
    [1, 2], 
    [2, 1], 
    [-1, 2],
    [-2, 1],
    [-1, -2], 
    [-2, -1],
]

map = [
    ["Bremen", "Hamburg", "Kiel", "Lübeck",	"Rostock"],
    ["Münster", "Bielefeld", "Hannover", "Magdeburg", "Berlin"],
    ["Essen", "Kassel", "Erfurt", "Leipzig", "Dresden"],
    ["Bonn", "Frankfurt", "Würzburg", "Nürnberg", "Bayreuth"],
    ["Trier", "Stuttgart", "Karlsruhe", "Augsburg", "München"],
]

cityNames = ["Erfurt", "Bremen", "Münster", "Essen", "Bonn", "Trier", "Hamburg", "Bielefeld", "Kassel", "Frankfurt", "Stuttgart", "Kiel", "Hannover", "Würzburg", "Karlsruhe", "Lübeck", "Magdeburg", "Leipzig", "Nürnberg", "Augsburg", "Rostock", "Berlin", "Dresden", "Bayreuth", "München"]
cityObj = []

start = "Erfurt"


class City():
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.row, self.col = -1, -1
        for i, row in enumerate(map):
            if self.name in row:
                self.row = i
                self.col = row.index(self.name)
        self.findNeighbours()

    def findNeighbours(self):
        for direction in directions:
            neighbourRow = self.row + direction[0]
            neighbourCol = self.col + direction[1]

            if neighbourCol > 0 and neighbourCol <= 4 and neighbourRow > 0 and neighbourRow <= 4:
                self.neighbours.append(map[neighbourRow][neighbourCol])


for cn in cityNames:
    cityObj.append(City(cn))

for tour in permutations(range(1, 25)):
    for stop in tour:
        city = cityObj[stop - 1]
        # if cityNames[stop] in cityObj[stop - 1]:

