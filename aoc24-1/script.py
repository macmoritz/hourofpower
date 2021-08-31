moves = {
    'e': [1, 0],
    'w': [-1, 0],
    'ne': [1, -1],
    'nw': [0, -1],
    'se': [0, 1],
    'sw': [-1, 1],
}

touchedTiles = []


def readFile(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    file.close()

    return lines


if __name__ == '__main__':
    fileData = readFile('input.txt')

    size = max([len(line) for line in fileData])

    for path in fileData:
        tile = [size * 2, size * 2]
        while path:
            if path[0] in moves:
                move = moves.get(path[0])
                path = path[1:]
            elif path[0:2] in moves:
                move = moves.get(path[0:2])
                path = path[2:]
            tile[0] += move[0]
            tile[1] += move[1]

        if tile in touchedTiles:
            touchedTiles.remove(tile)
        else:
            touchedTiles.append(tile[0:])
    print(touchedTiles)
    print(f'-- {len(touchedTiles)} tiles flipped --')
