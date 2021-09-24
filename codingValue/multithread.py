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
    for line in file:
        name = line.split(':')[0]
        languages = line.split(':')[1].split(',')
        developers.append(Developer(name, languages, resultWord))
        
        dev = developers[-1]
        if dev.toManyLetters():
            invalidResponses.append((dev, f'{dev} is using too many (>10) letters!'))
            developers.remove(dev)
   
    for dev in developers:
        dev.calculateCV()
    
    for dev in developers:
        if dev.CV is None:
            developers.remove(dev)
            invalidResponses.append((dev, f'{dev} has no possible solution'))

    solutionDevelopers = [dev for dev in developers if dev not in invalidResponses]  # and dev.CV is not None]
    print(f'1) Which software developer has the best CV?\n\tThe best CV has {max(solutionDevelopers, key=lambda x: x.CV)}\n')
    print(f'2) Which two responses are invalid (and why)?\n\tThe developers {invalidResponses} gave invalid responses!')
