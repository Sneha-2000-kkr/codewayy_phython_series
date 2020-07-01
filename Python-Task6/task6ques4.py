def countOccurenceOfAt(stringGiven):
    countOfAt = 0
    for wordInString in stringGiven.split():
        if (wordInString == 'At' or wordInString == 'AT'):
            countOfAt = countOfAt + 1
        else:
            wordList = []
            for charachterInWord in wordInString:
                wordList.append(charachterInWord)
            for indexOfCharachter in range(len(wordList)):
                if ((wordList[indexOfCharachter] == 'a' or wordList[indexOfCharachter] == 'A') and (
                        wordList[indexOfCharachter + 1] == 't' or wordList[indexOfCharachter + 1] == 'T')):
                    countOfAt = countOfAt + 1
    return(countOfAt)

stringGiven=str(input("enter the string"))
print("occurence of At in the String is ",countOccurenceOfAt(stringGiven))
