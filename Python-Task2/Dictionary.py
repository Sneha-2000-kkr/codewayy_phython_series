# working with Dictionary

#declaring Dictionary
StudentInfo={'name':'Sneha','age':20,'courses':['Btech cs','French']}

#accessing values 
print(StudentInfo.values())
print(StudentInfo.items())

#adding key and value in the Dictionary
StudentInfo['phone no']='3455'
#using get function in Dictionary to fetch the value of desired or print not found
print(StudentInfo.get('phone no','not found'))

#removing value from the Dictionary
print(StudentInfo.pop('age'))

#updating value for the key in Dictionary
StudentInfo.update({'name':'rekha'})
print(StudentInfo)

#to display all the keys in the Dictionary
print(StudentInfo.keys())

#to display all the items in the Dictionary
print(StudentInfo.items())

#to display all the values in the Dictionary
print(StudentInfo.values())

#to calculate length of the Dictionary
print(StudentInfo.__len__())
    #or
print(len(StudentInfo))

#for displaying keys and values via loop

for key,value in StudentInfo.items():
    print(key,value)
    
# Creating a NestedDictionary 
DictInUse = {'Dict1': {1: 'mago'}, 
        'Dict2': {'Name': 'Sneha'}} 
  
# Accessing element using key 
print(DictInUse['Dict1']) 
print(DictInUse['Dict1'][1]) 
print(DictInUse['Dict2']['Name']) 

#removing value from a NestedDictionary
del DictInUse['Dict1']['Dict2'] 

# Deleting entire Dictionary 
DictInUse.clear() 
print(DictInUse) 
#displays empty curly braces

