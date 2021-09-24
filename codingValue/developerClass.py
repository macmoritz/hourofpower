class Developer():
    def __init__(self, name, languages, resultword):
        self.name = name
        self.languages = set(languages)
        self.resultword = resultword
        self.map = None
        self.usedLetters = set(''.join(self.languages)) | set(self.resultword)
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
            num += str(self.map.index(letter))
        return int(num)

    def isCorrectMap(self):
        resultwordInt = self.getMappedNumFromStr(self.resultword)
        languagesInt = [self.getMappedNumFromStr(language) for language in self.languages]
        if sum(languagesInt) == resultwordInt:
            return resultwordInt
        return False
