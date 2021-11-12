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

citys = ["Bremen", "Hamburg", "Kiel", "Lübeck",	"Rostock", "Münster", "Bielefeld", "Hannover", "Magdeburg", "Berlin", "Essen", "Kassel", "Erfurt", "Leipzig", "Dresden", "Bonn", "Frankfurt", "Würzburg", "Nürnberg", "Bayreuth", "Trier", "Stuttgart", "Karlsruhe", "Augsburg", "München"],

trips = []


class City():
    def __init__(self, name):
        self.name = name
        self.row, self.col = -1, -1
        for i, row in enumerate(map):
            if self.name in row:
                self.row = i
                self.col = row.index(self.name)

    def getNeighbours(self, used):
        neighbours = []
        print(f'{self.name} not in {[u.name for u in used]} {self.name not in [u.name for u in used]}')
        for direction in directions:
            neighbourRow = self.row + direction[0]
            neighbourCol = self.col + direction[1]

            if neighbourCol >= 0 and neighbourCol <= 4 and neighbourRow >= 0 and neighbourRow <= 4:
                print(map[neighbourRow][neighbourCol])
                if map[neighbourRow][neighbourCol] not in [u.name for u in used]:
                    neighbours.append(map[neighbourRow][neighbourCol])
        return neighbours
    
    def __str__(self) -> str:
        return self.name


class Trip():
    def __init__(self, next: City, previous=None):
        self.stops = []
        if previous is not None:
            self.stops = previous.stops
        if next is not None:
            self.stops.append(next)


def generateTrip(trip: Trip):
    global trips
    if len(trip.stops[-1].getNeighbours(trip.stops)) == 0:
        if len(trip.stops) == 25:
            trips.append(trip)
            print('found solution')
    else:
        for neighbour in trip.stops[-1].getNeighbours(trip.stops):
            generateTrip(Trip(City(neighbour), trip))

# Aufgabe 1
generateTrip(Trip(City("Erfurt")))
# print(City("Erfurt").getNeighbours([City("Bonn"), City("Stuttgart"), City('Bayreuth'), City('Augsburg'), City('Berlin'), City('Lübeck'), City('Münster'), City('Hamburg')]))

# Aufgabe 2 
# for row in map:
#     for city in row:
#         generateTrip(Trip(City(city)))
#         print(f'Augabe 2: {len(trips)}')

# Aufgabe 3, braucht Aufgabe 2
# for trip in trips:
#     if trip[0] in citys:
#         citys.remove(trip[0])
#     if trip[-1] in citys:
#         citys.remove(trip[-1])
# print(f'Aufgabe 3:\n\t{citys}')
