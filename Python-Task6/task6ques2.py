# list given in question
listGiven=[(),(),('',),('a','b'),('a','b','c'),('d')]

# Storing the index from the list which are to be deleted
deleteList=[]
print("Indexes and Elements which are to be deleted from list")
for i in range(len(listGiven)):
    if(listGiven[i]==()):
        deleteList.append(i)

#deleting desired indexes from the given list               
for i in deleteList:
    print(i , listGiven.pop(deleteList[i-1]))
    
# Displaying desired list
print("Desired List")
print(listGiven)
