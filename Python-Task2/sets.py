#Working with sets

#declaring sets
People = {"Jay", "Idrish", "Archi"} 
print(People)
#this is to notice that sets does not display the values inside it in neither
#given order nor in any sorted manner, hence indexing is not possible for sets

# for adding values in the set 
People.add("Daxit") 
print(People)


#performing union in the sets
People = {"Jay", "Idrish", "Archil"} 
Vampires = {"Karan", "Arjun"} 
Dracula = {"Deepanshu", "Raju"} 

#using union() function
Population = People.union(Vampires)
print(Population) 

#using '|' operator
Population = People|Dracula 
print(Population) 

#performing intersection in sets
Set1 = set() 
Set2 = set() 

#adding the values via loop in set1
for i in range(5): 
    set1.add(i) 
    
#adding the values via loop in set2 
for i in range(3,9): 
    Set2.add(i) 
   
# using intersection() function 
Set3 = Set1.intersection(Set2)    
print(Set3)

# Intersection using "&" operator 
Set3 = Set1 & Set2 
print(Set3)

#performing difference among sets
# using difference() function 
Set3 = Set1.difference(Set2) 
print(Set3)

# using '-' operator 
Set3 = Set1 - set2 
print(Set3)

#for comparison among the sets

#if set1 is equivalent to set2
print(Set1==Set2)
#displays false

#if set1 is superset of set2
print(Set1>=Set2)
#displays false 

#if set1 is not equivalent to set2
print(Set1 != Set2)
#displays true

# if set1 is subset of set2
print(Set1 <= Set2)
#displays false  


#for removing all values in the set
Set1.clear()
print(Set1)
#displays set1 is not defined

#for checking presence of a key value in the list
Set={22,98,23,98,45,21,43}
print(22 in Set)
#displays true













