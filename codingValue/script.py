import itertools

from developerClass import Developer


resultWord = 'CODING'
developers = []
invalidResponses = []


def readFile(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]
    file.close()

    return lines


if __name__ == '__main__':
    file = readFile('input.txt')
    # file = readFile('input_example.txt')
    for line in file:
        name = line.split(':')[0]
        languages = line.split(':')[1].split(',')
        developers.append(Developer(name, languages, resultWord))

    for dev in developers:
        print(dev.getFirstLetters(), dev.languages)
        if dev.toManyLetters():
            print(f'{dev} is out!!! He/She is using too many (>10) letters!')
            invalidResponses.append(dev)
            developers.remove(dev)
        else:
            print(f'calculating cv for {str(dev)}')
            allCombinations = set(itertools.permutations(list(dev.usedLetters)))
            for comb in allCombinations:
                dev.map = comb
                if comb[0] not in dev.getFirstLetters():
                    resultInt = dev.isCorrectMap()
                    if resultInt:
                        dev.CV = resultInt
                        print(f'{dev} has a solution, the CV is {resultInt}!')
                        break
            if dev.CV is None:
                print(f'{dev} is out!!! He/She has no possible solution {dev.CV}!')
                invalidResponses.append(dev)
                developers.remove(dev)
        print('\n')

    print(f'all cv none devs {[str(dev) for dev in developers if dev.CV is None]}')
    print(f'The developers {[str(i) for i in invalidResponses]} gave invalid responses!')
    solutionDevelopers = [dev for dev in developers if dev not in invalidResponses and dev.CV is not None]
    print([(str(i), i.CV) for i in solutionDevelopers])
    print(f'\nThe best CV has {max(solutionDevelopers, key=lambda x: x.CV)}')
