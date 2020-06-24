#declaring a tuple
Tuple=(23,45,56,43)
print(Tuple)

#Splitting of tuples can be done similarly to Strings
print(Tuple[1:])
print(Tuple[:2])
print(Tuple[1:3])
print(Tuple[:-2])
print(Tuple[-1:0:-1])

#creating a nested tuple
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'CodeWayy') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: " + Tuple3 ) 

#Creating a Tuple with repetition 
Tuple1 = ('Coding',) * 3
print("\nTuple with repetition: " + Tuple1) 

#Concatenation of Tuples
Tuple3 = Tuple1 + Tuple2 
print("\nTuples after Concatenaton: ") 
print(Tuple3) 

#for finding max value in the tupple
print(max(tuple))

#for finding min value in the tupple
print(min(tuple))

#for finding som of values in the tupple
print(sum(tuple))

#for finding length of tupple
print(len(tuple))

#for converting a list into tuple
list=['3','4','5']
print(tuple(list))

#tuples are inmutable, hence values at any index cannot be updated
tuple[2]='9'
print(tuple)
#this will display error


