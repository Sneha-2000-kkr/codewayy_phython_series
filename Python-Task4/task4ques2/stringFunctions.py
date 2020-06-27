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
