letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "m", "x", "y", "z"]

encryptedWord = ""
userWord = input("Podaj wyraz do zahashowania: ")
cesarIndex = int(input("Podaj przesunięcie do szyfru Cezara: "))

for i in userWord:
    currentLetterIndex = letters.index(i)
    currentLetterHashedIndex = currentLetterIndex + cesarIndex
    if currentLetterHashedIndex > len(letters):
        currentLetterHashedIndex -= len(letters)
    encryptedWord += letters[currentLetterHashedIndex]

print(encryptedWord)
