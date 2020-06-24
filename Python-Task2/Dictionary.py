# working with Dictionary

#declaring Dictionary
Student={'name':'Sneha','age':20,'courses':['Btech cs','French']}

#accessing values 
print(Student.values())
print(Student.items())

#adding key and value in the Dictionary
Student['phone no']='3455'
#using get function in Dictionary to fetch the value of desired or print not found
print(Student.get('phone no','not found'))

#removing value from the Dictionary
print(Student.pop('age'))

#updating value for the key in Dictionary
Student.update({'name':'rekha'})
print(Student)

#to display all the keys in the Dictionary
print(Student.keys())

#to display all the items in the Dictionary
print(Student.items())

#to display all the values in the Dictionary
print(Student.values())

#to calculate length of the Dictionary
print(Student.__len__())
    #or
print(len(Student))

#for displaying keys and values via loop

for key,value in Student.items():
    print(key,value)
    
# Creating a NestedDictionary 
Dict = {'Dict1': {1: 'mago'}, 
        'Dict2': {'Name': 'Sneha'}} 
  
# Accessing element using key 
print(Dict['Dict1']) 
print(Dict['Dict1'][1]) 
print(Dict['Dict2']['Name']) 

#removing value from a NestedDictionary
del Dict['Dict1']['Dict2'] 

# Deleting entire Dictionary 
Dict.clear() 
print(Dict) 
#displays empty curly braces
