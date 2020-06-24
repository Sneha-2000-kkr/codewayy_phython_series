# working with Dictionary

#declaring Dictionary
student={'name':'Sneha','age':20,'courses':['Btech cs','French']}

#accessing values 
print(student.values())
print(student.items())

#adding key and value in the Dictionary
student['phone no']='3455'
#using get function in Dictionary to fetch the value of desired or print not found
print(student.get('phone no','not found'))

#removing value from the Dictionary
print(student.pop('age'))

#updating value for the key in Dictionary
student.update({'name':'rekha'})
print(student)

#to display all the keys in the Dictionary
print(student.keys())

#to display all the items in the Dictionary
print(student.items())

#to display all the values in the Dictionary
print(student.values())

#to calculate length of the Dictionary
print(student.__len__())
    #or
print(len(student))

#for displaying keys and values via loop

for key,value in student.items():
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
