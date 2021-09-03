from copy import deepcopy
import array


moves = {
    'e': [1, 0],
    'w': [-1, 0],
    'ne': [1, -1],
    'nw': [0, -1],
    'se': [0, 1],
    'sw': [-1, 1],
}

blackTiles = []


def readFile(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    file.close()

    return lines


def getBlackAdjacentCount(tile):
    count = 0
    for move in moves.values():
        neighbour = [tile[0] + move[0], tile[1] + move[1]]
        if neighbour in blackTiles:
            count += 1
    return count


if __name__ == '__main__':
    fileData = readFile('./aoc24/input.txt')

    size = max([len(line) for line in fileData]) * 2

    for path in fileData:
        tile = array.array('i', [size, size]).tolist()
        while path:
            if path[0] in moves:
                move = moves.get(path[0])
                path = path[1:]
            elif path[0:2] in moves:
                move = moves.get(path[0:2])
                path = path[2:]
            tile[0] += move[0]
            tile[1] += move[1]

        if tile in blackTiles:
            blackTiles.remove(tile)
        else:
            blackTiles.append(tile[0:])

    for day in range(100):
        copy = deepcopy(blackTiles)

        for i in range(0, size * 2):
            for j in range(0, size * 2):
                currentTile = array.array('i', [i, j]).tolist()
                blackNeighboursCount = getBlackAdjacentCount(currentTile)

                if currentTile in blackTiles:
                    if blackNeighboursCount == 0 or blackNeighboursCount > 2:
                        copy.remove(currentTile)
                else:
                    if blackNeighboursCount == 2:
                        copy.append(currentTile[0:])

        blackTiles = copy
        print(f'Day {day+1}: {len(blackTiles)}')

    print(f'-- {len(blackTiles)} tiles flipped --')
