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
        lines = [line.strip() for line in f if line != '\n']
    f.close()

    p1 = [int(x) for x in lines[1:getSplitIndex(lines)]]
    p2 = [int(x) for x in lines[getSplitIndex(lines) + 1:]]

    return {
        'p1': p1,
        'p2': p2,
    }


def game(gameCount, p1, p2):
    round = 0
    
    if p1 in p1Decks and p2 in p2Decks:
        print('Spieler 1 hat gewonnen! Das Deck kam im Spiel schon vor!')
        return p1
        
    while len(p1) > 0 and len(p2) > 0:
        round += 1
        print(f'-- Runde {round} (Spiel {gameCount}) --')
        printDecks(p1, p2)
        print(f'Spieler 1 legt: {p1[0]}')
        print(f'Spieler 2 legt: {p2[0]}')

        if p1[0] == (len(p1) - 1) and p2[0] == (len(p2) - 1):
            winner = game(gameCount+1, p1[:(p1[0] + 1)], p2[:(p2[0] + 1)])
        elif p1[0] > p2[0]:
            print(f'Spieler 1 gewinnt Runde {round} von Spiel 1!\n')
            winner = p1
        else:
            print(f'Spieler 2 gewinnt Runde {round} von Spiel 1!\n')
            winner = p2

        if winner == p1:
            placeCards(winner=p1, loser=p2)
        elif winner == p2:
            placeCards(winner=p2, loser=p1)
    
    p1Decks.append(p1[0:])
    p2Decks.append(p2[0:])
    return winner


if __name__ == "__main__":
    fileData = readFile('input.txt')

    p1 = fileData['p1']
    p2 = fileData['p2']

    p1Decks = []
    p2Decks = []

    while True:        
        winner = game(1, p1, p2)
        if len(p1) == 0 or len(p2) == 0:
            break
    
    print('== Kartendeck nach Spiel ==')
    printDecks(p1, p2)
    print('\n\n')
    calcScore(winner)
