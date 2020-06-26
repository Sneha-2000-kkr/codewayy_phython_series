#2.a
#defining function for computing and returning square of a given number
def sqaureOfNumberFunc(numberGiven):
    return(numberGiven*numberGiven)


#defining function for computing and returning maximum element from a given list
def maximumFromListFunc(listGiven):
    #initilizing first element of the list as maximum element
    maximumNumber=listGiven[0]
    #for loop for comparing all the elements in the list to maximum element 
    for i in listGiven:
        if(i>maximumNumber):
            #assining the value of newely found maximum to maximum element
            maximumNumber=i
    return maximumNumber


#defining function for computing and returning minimum element from a given list
def minimumFromListFunc(listGiven):
    #initilizing first element of the list as minimum element
    minimumNumber=listGiven[0]
    #for loop for comparing all the elements in the list to minimum element
    for i in listGiven:
        if(i<minimumNumber):
            #assining the value of newely found minimum to minimum element
            minimumNumber=i
    return minimumNumber


#defining function for computing and returning sum of all elements in the list
def sumOfAllElementsFromListFunc(listGiven):
    #initilizing sum of all elements in the list to zero
    sumOfList=0
    #adding elements from the list to the sum
    for i in listGiven:
        sumOfList=sumOfList+i
    return sumOfList


#2.b
#defining function for computing and returning length of a given string
def lengthOfString(givenString):
    #initilizing length of the string to zero
    counter = 0
    for s in givenString:
       counter = counter+1
    return counter


#defining function for computing and returning middle character of a given string
def middleCharacterOfString(givenString):
   return givenString[(lengthOfString(givenString)-1)//2:(lengthOfString(givenString)+2)//2]


#defining function for computing and returning words in a given string
def wordsInString(givenString):
    #initilizing no of words in a string to zero
    noOfWords=0
    for i in givenString:
        # if a blank space is found in the string it marks starting of next word
        if i==" ":
            noOfWords=noOfWords+1
    #total no of words in the string will be one more than blank spaces in the string        
    return noOfWords+1


#defining function for computing and returning no of vowels in a given string
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



#2.c
#defining function for computing and returning result on analysing two conditions with 'and' logical operator 
def logicalOperatorAndFunc(numBer1,numBer2):
    if(numBer1=='True'):
        if(numBer2=='True'):
            return ('True')
    else:
        return ('False')
    

#defining function for computing and returning result on analysing two conditions with 'or' logical operator
def logicalOperatorOrFunc(numBer1,numBer2):
    if(numBer1=='False'):
        if(numBer2=='False'):
            return ('False')
    else:
        return('True')
    
    
#defining function for computing and returning result on analysing a condition with 'not' logical operator
def logicalOperatorNotFunc(numBer1):
    if(numBer1=='True'):
        return ('False')
    else:
        return ('True')



