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
