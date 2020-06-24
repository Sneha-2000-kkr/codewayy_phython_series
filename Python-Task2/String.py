# Working with Strings
# declaration of string in single quotes
String="hello"

#splitting of a string

#To get  a character at a particular index i, here i=0
print(String[0])

#To get a sub string in  the index range i to j, here i=0 and j=3
print(String[0:3])

# To get a sub string in  the index range from beginning to j, here j=2
print(String[:2])

#To get a entire string, here i=0 and j=till end of the string
print(String[:])

#To get a sub string in  the index range i to j, here i=2 and j= till end of the string
print(String[2:])

#To get a character at ith index in reverse string, here i=-1
print(String[-1])

#To get a sub string in  the index range from beginning to j, here j=-2
print(String[:-2])

#To get a sub string in  the index range i to j, here i=-2 and j=till end of the string
print(String[-2:])

#reversing a string
String='reverse'
SubString=string[::-1]
print(SubString)

#For Calculating length of a String
print(len(String))

#For updating a character or deleting a character at a particular index in string is **not allowed** , this will display error

#for updation
String='Sneha Singh'
String[7]='D'
print(String)
#displays error

#for deletion
del String[2]  
print(String)
#displays error

#Entire String can be updated and assigned a new value and can be deleted as well

#assigning a new value to the string
String='CodeWayy'
print(String)
String='jackpot'
print(String)
#displays a updated value

#Deleting a String
del String
print(String)
#Displays String is not defined

# Escaping Single Quote
String = 'I\'m a "Sneha"'
print("\nEscaping Single Quote: "+ String)

#Printing Paths with the use of Escape Sequences 
String1 = "C:\\Users\\Sneha Singh\\"
print("\nEscaping Backslashes: " + String1) 

# Formatting of Strings 
  
# Default order 
String1 = "{} {} {}".format('Masti', 'in', 'Life') 
print("Print String in default order: " + String1) 
  
# Positional Formatting 
String1 = "{1} {0} {2}".format('Masti', 'in', 'Life') 
print("\nPrint String in Positional order: " + String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Masti', f = 'in', l = 'Life') 
print("\nPrint String in order of Keywords: " + String1) 


# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 

# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Sneha','Singh','Dixit') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 


String='hello my name is Sneha'

#Displays the String with first character of first word capitalized
print(String.capitalize())

#Returns true or false if String is alpha-numeric or not
print(String.isalnum())

#returns the string in upper-case , all character are in capital letter
print(String.upper())

