#initializing the IndianPlayers list
IndianPlayers=['Virat kohli','MS Dhoni','Rohit Sharma','KL Rahul']

#Displaying entire list
print(IndianPlayers)

#Displaying list value at a particular index i , here i=1
print(IndianPlayers[1])

#list are mutable , therefore value of list at any index can be updated
IndianPlayers[2]='Hardik Pandya'
print(IndianPlayers)

#Splitting of list can be done similarly to Strings
print(IndianPlayers[1:])
print(IndianPlayers[:2])
print(IndianPlayers[1:3])
print(IndianPlayers[:-2])
print(IndianPlayers[-1:0:-1])

#Adding list in present list
AllPlayers=IndianPlayers+['Steve Smith','Aaron Fich','David Warner']
print(AllPlayers)

#Adding  a value to the end of the list
AllPlayers.append('Gllen maxwell')
print(AllPlayers)

#Adding value at a particular index i, here i=2
AllPlayers.insert(2,'Rohit Sharma')
print(AllPlayers)

# append() adds a value at the end of the list while insert() adds value at a particular index

#Removing value from the list
#removes first two values in the list and display the rest
AllPlayers[:2]=[]
print(AllPlayers)

#removes first values from reverse in the list and display the rest
AllPlayers[-1:]= [ ]
print(AllPlayers)

#list facilitates keeping collection of various data types
values=[9.32,'naveen',34]
print(values)

#Displaying various list in same list 
Grand=[AllPlayers,Values]
print(Grand)
#now Grand is a multi-dimensional list

#for accessing values from multi-dimensional list
print(Grand[0][1]) 

#Declaring a number list
NumberList=[23,45,67,78]

#for adding values in the exixting list via inbuilt function ie extend()
NumberList.extend([23,34,45])
print(NumberList)

#deleting a value from the list

#at a given index i, here i=3
print(NumberList.pop(3))

#as per data structure concept 
print(NumberList.pop())

#for computing sum of values in the NumberList
print(sum(NumberList))

#for computing max among all the values
print(max(NumberList))

#for computing min among all the values
print(min(NumberList))

#for calculating length of the list
print(NumberList.__len__())

#for calculating occurance of a value in the list
print(grand.count('23'))












