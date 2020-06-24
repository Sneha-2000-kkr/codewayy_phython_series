#Working with sets

#declaring sets
people = {"Jay", "Idrish", "Archi"} 
print(people)
#this is to notice that sets does not display the values inside it in neither
#given order nor in any sorted manner, hence indexing is not possible for sets

# for adding values in the set 
people.add("Daxit") 
print(people)


#performing union in the sets
people = {"Jay", "Idrish", "Archil"} 
vampires = {"Karan", "Arjun"} 
dracula = {"Deepanshu", "Raju"} 

#using union() function
population = people.union(vampires)
print(population) 

#using '|' operator
population = people|dracula 
print(population) 

#performing intersection in sets
set1 = set() 
set2 = set() 

#adding the values via loop in set1
for i in range(5): 
    set1.add(i) 
    
#adding the values via loop in set2 
for i in range(3,9): 
    set2.add(i) 
   
# using intersection() function 
set3 = set1.intersection(set2)    
print(set3)

# Intersection using "&" operator 
set3 = set1 & set2 
print(set3)

#performing difference among sets
# using difference() function 
set3 = set1.difference(set2) 
print(set3)

# using '-' operator 
set3 = set1 - set2 
print(set3)

#for comparison among the sets

#if set1 is equivalent to set2
print(set1==set2)
#displays false

#if set1 is superset of set2
print(set1>=set2)
#displays false 

#if set1 is not equivalent to set2
print(s1 != s2)
#displays true

# if set1 is subset of set2
print(s1 <= s2)
#displays false  


#for removing all values in the set
set1.clear()
print(set1)
#displays set1 is not defined

#for checking presence of a key value in the list
set={22,98,23,98,45,21,43}
print(22 in set)
#displays true












