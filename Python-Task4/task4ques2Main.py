import importedPythonFile
listFromUser=[]
sizeOfList=int(input("enter the size of the list"))
print("Enter the elements of the list")
for i in range(0,sizeOfList):
    elementValue=int(input())
    listFromUser.append(elementValue)
numBer=int(input("enter the number whose square is to be computed"))
print("Square of ", numBer ," is ", importedPythonFile.sqaureOfNumberFunc(numBer))
print("Maximum element from list is ",importedPythonFile.maximumFromListFunc(listFromUser))
print("Minimum element from list is ",importedPythonFile.minimumFromListFunc(listFromUser))
print("Sum of all elements is ",importedPythonFile.sumOfAllElementsFromListFunc(listFromUser))


import importedPythonFile
stringGiven=str(input("Enter the string"))
print("length of string ",importedPythonFile.lengthOfString(stringGiven))
print("Middle character of the string is ",importedPythonFile.middleCharacterOfString(stringGiven))
print("no of vowels in the string ",importedPythonFile.vowelsInString(stringGiven))
print("no of words in the string ",importedPythonFile.wordsInString(stringGiven))


import importedPythonFile
numBer1=str(input("enter your first condition"))
numBer2=str(input("enter your second condition"))
print("applying and operator",importedPythonFile.logicalOperatorAndFunc(numBer1,numBer2))
print("applying or operator",importedPythonFile.logicalOperatorOrFunc(numBer1,numBer2))
print("applying not operator",importedPythonFile.logicalOperatorNotFunc(numBer1))




