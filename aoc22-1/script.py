def getSplitIndex(lines):
    for index, line in enumerate(lines):
        if line == 'Player 2:':
            return index


def printDecks(p1, p2):
    print(f'Karten Spieler 1: {p1}')
    print(f'Karten Spieler 2: {p2}')


def placeCards(winner, loser):
    winner.append(winner[0])
    winner.append(loser[0])
    winner.pop(0)
    loser.pop(0)


def calcScore(cards):
    score = 0
    output = ''
    for i in range(len(cards), 0, -1):
        output += f'\t{cards[len(cards) - i]} *\t{i}'
        score += cards[len(cards) - i] * i
        print(output)
        output = '+'
    print(f'= {score}')


def readFile(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f if line != '\n']
    f.close()

    p1 = [int(x) for x in lines[1:getSplitIndex(lines)]]
    p2 = [int(x) for x in lines[getSplitIndex(lines) + 1:]]

    return {
        'p1': p1,
        'p2': p2,
    }


if __name__ == "__main__":
    fileData = readFile('input.txt')

    p1 = fileData['p1']
    p2 = fileData['p2']

    game = 0
    while len(p1) > 0 and len(p2) > 0:
        game += 1
        print(f'-- Runde {game} --')
        printDecks(p1, p2)

        print(f'Spieler 1 legt: {p1[0]}')
        print(f'Spieler 2 legt: {p2[0]}')

        if p1[0] > p2[0]:
            print('Spieler 1 gewinnt Runde!')
            placeCards(winner=p1, loser=p2)
            winner = p1
        else:
            print('Spieler 2 gewinnt Runde!')
            placeCards(winner=p2, loser=p1)
            winner = p2
    else:
        print('== Kartendeck nach Spiel ==')
        printDecks(p1, p2)
        print('\n\n')
        calcScore(winner)
