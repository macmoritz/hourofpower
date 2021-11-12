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

citys = ["Bremen", "Hamburg", "Kiel", "Lübeck",	"Rostock", "Münster", "Bielefeld", "Hannover", "Magdeburg", "Berlin", "Essen", "Kassel", "Erfurt", "Leipzig", "Dresden", "Bonn", "Frankfurt", "Würzburg", "Nürnberg", "Bayreuth", "Trier", "Stuttgart", "Karlsruhe", "Augsburg", "München"]

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
        for direction in directions:
            neighbourRow = self.row + direction[0]
            neighbourCol = self.col + direction[1]

            if neighbourCol >= 0 and neighbourCol <= 4 and neighbourRow >= 0 and neighbourRow <= 4:
                if map[neighbourRow][neighbourCol] not in [u.name for u in used]:
                    neighbours.append(map[neighbourRow][neighbourCol])
        return neighbours
    
    def __str__(self) -> str:
        return self.name


class Trip():
    def __init__(self, next: City, previous=None):
        self.stops = []
        if previous is not None:
            self.stops = previous.copy()
        if next is not None:
            self.stops.append(next)


def generateTrip(trip: Trip):
    global trips
    if len(trip.stops[-1].getNeighbours(trip.stops)) == 0:
        if len(trip.stops) == 25:
            trips.append(trip)
            # print('found solution')
    else:
        for neighbour in trip.stops[-1].getNeighbours(trip.stops):
            generateTrip(Trip(City(neighbour), trip.stops))

# Aufgabe 1
generateTrip(Trip(City("Erfurt")))
print(f'Aufgabe 1: {len(trips)}')

# Aufgabe 2
trips = []
for city in citys:
    print(f'calculating {city}')
    generateTrip(Trip(City(city)))
print(f'Aufgabe 2: {len(trips)}')

# Aufgabe 3
for trip in trips:
    if trip.stops[0].name in citys:
        citys.remove(str(trip.stops[0].name))
    if trip.stops[-1].name in citys:
        citys.remove(str(trip.stops[-1].name))
print(f'Aufgabe 3:\n\t{citys}')
