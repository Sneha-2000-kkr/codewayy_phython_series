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

