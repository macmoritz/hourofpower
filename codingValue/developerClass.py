class Developer():
    def __init__(self, name, languages):
        self.name = name
        self.languages = set(languages)

    def __str__(self):
        return self.name

    def checkLetterCount(self, resultword):
        languagesLetters = set(''.join(self.languages))
        resultwordLetters = set(resultword)
        letters = languagesLetters | resultwordLetters
        if len(letters) > 10:
            return True
        return False

    def getFirstLetters(self, resultword):
        firstLetters = ""
        firstLetters += resultword[0]
        for language in self.languages:
            firstLetters += language[0]
        return ''.join(set(firstLetters))
