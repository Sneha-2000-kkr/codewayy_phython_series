
# Defining function for counting occurence of at in the String irrespective of it's case
def countOccurenceOfAt(stringGiven):
    
    # Initializing counter variable to zero
    countOfAt = 0
    for wordInString in stringGiven.split():
        
        # if at is a Word itself in the string
        if (wordInString == 'At' or wordInString == 'AT'):
            countOfAt = countOfAt + 1
        else:
            
            # If at is present in any word of the string
            wordList = []
            for charachterInWord in wordInString:
                wordList.append(charachterInWord)
            for indexOfCharachter in range(len(wordList)):
                if ((wordList[indexOfCharachter] == 'a' or wordList[indexOfCharachter] == 'A') and (
                        wordList[indexOfCharachter + 1] == 't' or wordList[indexOfCharachter + 1] == 'T')):
                    countOfAt = countOfAt + 1
    return(countOfAt)


# Taking string input from the user
stringGiven=str(input("enter the string"))
print("occurence of At in the String is ",countOccurenceOfAt(stringGiven))
