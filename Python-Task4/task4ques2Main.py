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

