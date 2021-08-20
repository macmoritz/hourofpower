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


def getSplitIndex(lines):
    for index, line in enumerate(lines):
        if line == 'Player 2:':
            return index


class Game():
    def __init__(self):
        self.history = []
        # self.p1History = []
        # self.p2History = []


    def printDecks(self, p1, p2):
        print(f'Karten Spieler 1: {p1}')
        print(f'Karten Spieler 2: {p2}')


    def calcScore(self, cards):
        score = 0
        output = ''
        for i in range(len(cards), 0, -1):
            output += f'\t{cards[len(cards) - i]} *\t{i}'
            score += cards[len(cards) - i] * i
            print(output)
            output = '+'
        print(f'= {score}')


    def printEnd(self, winner):
        print('== Kartendeck nach Spiel ==')
        self.printDecks(p1, p2)
        print('\n\n')
        self.calcScore(winner)


    def play(self, gameCount, p1, p2):
        round = 1
        
        while True:
            print(f'-- Runde {round} (Spiel {gameCount}) --')
            self.printDecks(p1, p2)

            if len(p1) < 1:
                print(f'Spieler 1 hat keine Karten mehr!')
                self.printEnd(p2)
                return 'p1'
            elif len(p2) < 1:
                print(f'Spieler 2 hat keine Karten mehr!')
                self.printEnd(p1)
                return 'p2'
            else:
                print(f'Spieler 1 legt: {p1[0]}')
                print(f'Spieler 2 legt: {p2[0]}')
                
                if (p1 + p2) in self.history:
                # if p1 in self.p1History and p2 in self.p2History:
                    print('Spieler 1 hat gewonnen! Das Deck kam im Spiel schon vor!')
                    return 'p1'
                
                self.history.append(p1 + p2)
                # self.p1History.append(p1[0:])
                # self.p2History.append(p2[0:])

                p1i0 = p1[0]
                p1.pop(0)

                p2i0 = p2[0]
                p2.pop(0)

                if p1i0 <= len(p1) and p2i0 <= len(p2):
                    sub = Game()
                    winner = sub.play(gameCount+1, p1[:p1i0], p2[:p2i0])
                    if winner == 'p1':
                        p1.append(p1i0)
                        p1.append(p2i0)
                    elif winner == 'p2':
                        p2.append(p2i0)
                        p2.append(p1i0)

                elif p1i0 > p2i0:
                    print(f'Spieler 1 gewinnt Runde {round} von Spiel {gameCount}!\n')
                    p1.append(p1i0)
                    p1.append(p2i0)
                else:
                    print(f'Spieler 2 gewinnt Runde {round} von Spiel {gameCount}!\n')
                    p2.append(p2i0)
                    p2.append(p1i0)
                
                round += 1


if __name__ == "__main__":
    fileData = readFile('input.txt')

    p1 = fileData['p1']
    p2 = fileData['p2']
    
    game = Game()
    game.play(1, p1, p2)