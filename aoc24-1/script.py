moves = {
    'e': (1, 0),
    'w': (-1, 0),
    'ne': (1, -1),
    'nw': (0, -1),
    'se': (0, 1),
    'sw': (-1, 1),
}

touchedTiles = set()


def readFile(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    file.close()

    return lines


if __name__ == '__main__':
    fileData = readFile('input.txt')

    size = max([len(line) for line in fileData]) * 2
    for path in fileData:
        x, y, tile = 0, 0, ()
        while path:
            if path[0] in moves:
                move = moves.get(path[0])
                path = path[1:]
            elif path[0:2] in moves:
                move = moves.get(path[0:2])
                path = path[2:]

            x += move[0]
            y += move[1]

        tile = (size + x, size + y)

        if tile in touchedTiles:
            touchedTiles.remove(tile)
        else:
            touchedTiles.add(tile)

    print(f'-- {len(touchedTiles)} tiles flipped --')