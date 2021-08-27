moves = {
    'e': [1, 0],
    'w': [-1, 0],
    'nw': [-1, -1],
    'ne': [1, -1],
    'sw': [1, 1],
    'se': [-1, 1],
}

touchedTiles = []


def readFile(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    file.close()

    return lines


if __name__ == '__main__':
    fileData = readFile('input_example.txt')

    maxDist = max([len(line) for line in fileData])
    center = [maxDist * 2, maxDist * 2]
 
    for path in fileData:
        tile = center
        for index, direction in enumerate(path):
            move = moves.get(direction) or moves.get(direction + path[index + 1])
            if move:
                tile[0] += move[0]  
                tile[1] += move[1]
        print(touchedTiles)
        if tile in touchedTiles:
            touchedTiles.remove(tile)
        else:
            touchedTiles.append(tile[0:])
    print(f'-- {len(touchedTiles)} tiles flipped --')
