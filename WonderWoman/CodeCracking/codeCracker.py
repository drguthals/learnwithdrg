# lassoLetter('A', 3) = 'D'
def lassoLetter(letter, shiftAmount):
    letterCode = ord(letter)

    capACode = ord('A')
    capZCode = ord('Z')
    lowACode = ord('a')
    lowZCode = ord('z')

    alphabetSize = 26

    if (letterCode >= capACode) & (letterCode <= capZCode):
        begAlphaCode = capACode
    else:
        begAlphaCode = lowACode

    decodedLetterCode = letterCode + shiftAmount

    trueLetterCode = begAlphaCode + ((letterCode - begAlphaCode) + shiftAmount) % alphabetSize

    decodedLetter = chr(trueLetterCode)

    return decodedLetter
    
def lassoWord( word, shiftAmount):
    decodedWord = ""

    for letter in word:
        decodedLetter = lassoLetter(letter, shiftAmount)

        decodedWord += decodedLetter
    
    return decodedWord

print(lassoWord("WHY", 13))
print(lassoWord("OsKzA", -18))
print(lassoWord("OHUpO", -1))
print(lassoWord("ed", 25))