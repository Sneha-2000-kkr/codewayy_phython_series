
#defining the functions to calculate the length of two concated strings and returning the value by join and count method
#function for calculating length of String1
def LengthofString1(String1,String2):
    return ((String2).join(String1).count(String2) + 1)

#function for calculating length of String2
def LengthofString2(String1,String2):
    return ((String1).join(String2).count(String1) + 1)
    
#taking string inputs from the user
String1=str(input("Enter first String\n"))
String2=str(input("Enter second String\n"))

#printing the length of String1
print("length of first string by concatenating them ",LengthofString1(String1,String2))

#printing the length of String2
print("length of second string by concatenating them ",LengthofString2(String1,String2))
