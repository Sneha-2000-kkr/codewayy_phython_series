import math

#we are having two points between which distance is to be calculated
dimensionTaken=int(input("enter the dimension into which coordinates are palced"))

#taking coordinates along axis
print("Enter value along various dimensional axis for first coordinate")
firstCoordinate=[]
for i in range(dimensionTaken):
    coordinateValue=int(input())
    firstCoordinate.append(coordinateValue)
print("Enter value along various dimensional axis for second coordinate")
secondCoordinate=[]
for i in range(dimensionTaken):
    coordinateValue=int(input())
    secondCoordinate.append(coordinateValue)
    
# displaying distance between the points
print("distance between these two coordinates are ",math.dist(firstCoordinate,secondCoordinate))

# area covered within the region
radiusOfCircle=(math.dist(firstCoordinate,secondCoordinate)/2)
areaOfCircle=(math.pi *pow(radiusOfCircle,2))
print("Area of circle within which things are to be searched ",areaOfCircle)

#things to be collected within the region, without repetion
numberOfItem=int(input("Enter the no of item"))
choosenIems=int(input("Enter no of items to be chosen"))
print("number of ways to choose choosenIems items from numberOfItem items without repetition and without order",math.comb(numberOfItem, choosenIems))


#sorting functions for list,tuples and sets
# Function for Sorting List
def sortList():
    myList = []
    n = int(input("Enter the length of list:"))
    for num in range(n):
        listElement = int(input("Enter elements:"))
        myList.append(listElement)
    print("Your List in is:", myList)
    # Sorting the List

    myList.sort()
    print("Your list sorted in accesnding order:", myList)


# Fucntion of Sorting tuple on basis of first element of the tuple pair
def sortTuple():
    tupleList = []
    line = input("Enter the list of tuples:\n")
    while (line != ""):
        tupleList.append(tuple(line.split()))
        line = input()
    print("The Tuple is:", tupleList)
    sortedTuple = sorted(tupleList)
    print("The sorted tuple is:", sortedTuple)


# Function for Sorting set
def sortSet():
    mySet = set()
    sizeSet = int(input("Enter the size of set:"))
    for i in range(sizeSet):
        setElement = int(input("Enter elements:"))
        mySet.add(setElement)

    # Sorting in a set
    sortedSet = sorted(mySet)
    print("Your sorted set is:", sortedSet)


# menu driven code for opting which sort to be done
userChoice = input("Enter The choice \n A List\n B Tuple\n C Set\n")
if (userChoice == "A"):
    sortList()
elif (userChoice == "B"):
    sortTuple()
elif (userChoice == "C"):
    sortSet()

