moves = {
    'ne': (1, -1),
    'nw': (0, -1),
    'se': (0, 1),
    'sw': (-1, 1),
    'e': (1, 0),
    'w': (-1, 0),
}

blackTiles = set()


def readFile(filename):
    paths = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            x, y = 0, 0
            for move in moves:
                counter = line.count(move)
                x += (moves[move][0] * counter)
                y += (moves[move][1] * counter)
                line = line.replace(move, '')
            paths.append((x, y))
    file.close()
    return paths


def getBlackAdjacentCount(tile):
    count = 0
    for move in moves.values():
        neighbour = (tile[0] + move[0], tile[1] + move[1])
        if neighbour in blackTiles:
            count += 1
    return count


if __name__ == '__main__':
    fileData = readFile('./input.txt')

    middle = max([len(line) for line in fileData]) + 25
    size = int(middle * 2)

    for path in fileData:
        tile = (middle + path[0], middle + path[1])

        if tile in blackTiles:
            blackTiles.remove(tile)
        else:
            blackTiles.add(tile[0:])

    for day in range(100):
        copy = blackTiles.copy()

        for i in range(0, size):
            for j in range(0, size):
                currentTile = (i, j)
                blackNeighboursCount = getBlackAdjacentCount(currentTile)

                if currentTile in blackTiles:
                    if blackNeighboursCount == 0 or blackNeighboursCount > 2:
                        copy.remove(currentTile)
                else:
                    if blackNeighboursCount == 2:
                        copy.add(currentTile[0:])

        blackTiles = copy
        print(f'Day {day+1}: {len(blackTiles)}')

    print(f'-- {len(blackTiles)} tiles flipped --')
