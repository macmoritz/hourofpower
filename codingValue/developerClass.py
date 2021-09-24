import itertools


class Developer():
    def __init__(self, name, languages, resultword):
        self.name = name
        self.languages = set(languages)
        self.resultword = resultword
        self.map = None

        self.usedLetters = list(set(''.join(self.languages)) | set(self.resultword))
        while len(self.usedLetters) < 10:
            self.usedLetters.append(['x', 'y', 'z'][len(self.usedLetters) % 3])
        self.CV = None

    def __str__(self):
        return self.name

    def toManyLetters(self):
        if len(self.usedLetters) > 10:
            return True
        return False

    def getFirstLetters(self):
        firstLetters = ''
        firstLetters += self.resultword[0]
        for language in self.languages:
            firstLetters += language[0]
        return ''.join(set(firstLetters))

    def getMappedNumFromStr(self, string):
        num = ''
        for letter in string:
            num += str(self.map.index(letter) % 10)
        return int(num)

    def isCorrectMap(self):
        resultwordInt = self.getMappedNumFromStr(self.resultword)
        languagesInt = [self.getMappedNumFromStr(language) for language in self.languages]
        if sum(languagesInt) == resultwordInt:
            return resultwordInt
        return False

    def calculateCV(self):
        print(f'{self.name} gets calculated')
        allCombinations = set(itertools.permutations(self.usedLetters))
        for comb in allCombinations:
            self.map = comb
            if comb[0] not in self.getFirstLetters():
                resultInt = self.isCorrectMap()
                if resultInt:
                    self.CV = resultInt
                    # print(f'{self.name} has a solution, the CV is {resultInt}!')
                    break
                # if self.CV is None:
                    # invalidResponses.append((self, f'{self} has no possible solution {self.CV}!'))
