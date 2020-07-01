listGiven=[(),(),('',),('a','b'),('a','b','c'),('d')]
deleteList=[]
print("Indexes and Elements which are to be deleted from list")
for i in range(len(listGiven)):
    if(listGiven[i]==()):
        deleteList.append(i)

for i in deleteList:
    print(i , listGiven.pop(deleteList[i-1]))
print("Desired List")
print(listGiven)
