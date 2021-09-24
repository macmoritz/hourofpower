import itertools

from developerClass import Developer


resultWord = 'CODING'
allUsedLetters = list(resultWord)
developers = []
invalidResponses = []


def readFile(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    file.close()

    return lines


if __name__ == '__main__':
    file = readFile('input.txt')
    for line in file:
        name = line.split(':')[0]
        languages = line.split(':')[1].split(',')
        developers.append(Developer(name, languages, resultWord))
        # dev = developers[-1]

    for dev in developers:
        allUsedLetters = list(set(allUsedLetters) | set(dev.usedLetters))
        if dev.toManyLetters():
            invalidResponses.append((dev, f'{dev} is using too many (>10) letters!'))
            developers.remove(dev)

    allCombinations = set(itertools.permutations(list(allUsedLetters)))
    for comb in allCombinations:
        for dev in developers:
            print(f'calculating cv for {str(dev)}')
            for comb in allCombinations:
                dev.map = comb
                if comb[0] not in dev.getFirstLetters():
                    resultInt = dev.isCorrectMap()
                    if resultInt:
                        dev.CV = resultInt
                        print(f'{dev} has a solution, the CV is {resultInt}!')
                        break
            if dev.CV is None:
                invalidResponses.append((dev, f'{dev} has no possible solution {dev.CV}!'))
                developers.remove(dev)
        print('\n')

    print(f'1) Which software developer has the best CV?\n\tThe best CV has {max(developers, key=lambda x: x.CV)}\n')
    print(f'2) Which two responses are invalid (and why)?\n\tThe developers {invalidResponses} gave invalid responses!')
