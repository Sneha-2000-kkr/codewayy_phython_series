# importing importedPythonFile python file , where all the functions are defined and used here.

import listFunctions
import logicalOperatorFunctions
import stringFunctions

# initilazing empty list
listFromUser=[]

#taking size of the list from the user
sizeOfList=int(input("enter the size of the list"))

#taking elements of list from the user
print("Enter the elements of the list")
for i in range(0,sizeOfList):
    elementValue=int(input())
    listFromUser.append(elementValue)
    
#taking a number from user for computing its square value
numBer=int(input("enter the number whose square is to be computed"))

#printing square of the number as taken from user
print("Square of ", numBer ," is ", listFunctions.sqaureOfNumberFunc(numBer))

#printing maximum value from list 
print("Maximum element from list is ",listFunctions.maximumFromListFunc(listFromUser))

#printing minimum value from the list
print("Minimum element from list is ",listFunctions.minimumFromListFunc(listFromUser))

#printing sum of all elements value from the list
print("Sum of all elements is ",listFunctions.sumOfAllElementsFromListFunc(listFromUser))




# taking  a string as input from user
stringGiven=str(input("Enter the string"))

#printing length of the string
print("length of string ",StringFuntions.lengthOfString(stringGiven))

#printing middle character of the string
print("Middle character of the string is ",stringFunctions.middleCharacterOfString(stringGiven))

#printing no of vowels in the string
print("no of vowels in the string ",stringFunctions.vowelsInString(stringGiven))

#printing no of words in the string
print("no of words in the string ",stringFunctions.wordsInString(stringGiven))



#taking two conditional input from the user
numBer1=str(input("enter your first condition"))
numBer2=str(input("enter your second condition"))

#printing results for and operator based on two conditions given by the user
print("applying and operator",logicalOperatorFunctions.logicalOperatorAndFunc(numBer1,numBer2))

#printing results for or operator based on two conditions given by the user
print("applying or operator",logicalOperatorFunctions.logicalOperatorOrFunc(numBer1,numBer2))

#printing results for not operator based on any one condition given by the user
print("applying not operator",logicalOperatorFunctions.logicalOperatorNotFunc(numBer1))
