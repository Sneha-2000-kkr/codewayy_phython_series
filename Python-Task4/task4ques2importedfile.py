def sqaureOfNumberFunc(numberGiven):
    return(numberGiven*numberGiven)

def maximumFromListFunc(listGiven):
    maximumNumber=listGiven[0]
    for i in listGiven:
        if(i>maximumNumber):
            maximumNumber=i
    return maximumNumber


def minimumFromListFunc(listGiven):
    minimumNumber=listGiven[0]
    for i in listGiven:
        if(i<minimumNumber):
            minimumNumber=i
    return minimumNumber

def sumOfAllElementsFromListFunc(listGiven):
    sumOfList=0
    for i in listGiven:
        sumOfList=sumOfList+i
    return sumOfList

def lengthOfString(givenString):
    counter = 0
    for s in givenString:
       counter = counter+1
    return counter

def middleCharacterOfString(givenString):
   return givenString[(lengthOfString(givenString)-1)//2:(lengthOfString(givenString)+2)//2]

def wordsInString(givenString):
    noOfWords=0
    for i in givenString:
        if i==" ":
            noOfWords=noOfWords+1
    return noOfWords+1


def vowelsInString(givenString):
    # Initializing count variable to 0
    countOfVowels = 0

    # Creating a set of vowels
    vowelAlphabets = set("aeiouAEIOU")

    # Loop to traverse the alphabet
    # in the given string
    for i in givenString:

        # If alphabet is present
        # in set vowel
        if i in vowelAlphabets:
            countOfVowels = countOfVowels + 1
    return countOfVowels



