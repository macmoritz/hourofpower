from types import resolve_bases
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
    print(len(developers))

    for dev in developers:
        if dev.checkLetterCount():
            print(f'{dev} is out!!! He/She is using to many (>10) letters!')
            invalidResponses.append(dev)
            developers.remove(dev)
        # print(dev.getFirstLetters(resultWord))

    for dev in developers:
        # print(dev)
        for letter in dev.usedLetters:
            for num in range(0, 9):
                usedLetters = list(dev.usedLetters)
                if num != 0 and usedLetters[num] not in dev.getFirstLetters():
                    dev.map = usedLetters[num:] + usedLetters[:num]
                    if dev.applyMap():
                        print(dev.map)
                # print(dev.map)

    print(len(developers))
