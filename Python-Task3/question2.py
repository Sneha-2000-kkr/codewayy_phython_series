
#defining the functions to calculate the length of two concated strings and returning the value by join and count method
#function for calculating length of String1
def lengthOfString1(string1,string2):
    return ((string2).join(string1).count(string2) + 1)

#function for calculating length of String2
def lengthOfString2(string1,string2):
    return ((string1).join(string2).count(string1) + 1)
    
#taking string inputs from the user
string1=str(input("Enter first String\n"))
string2=str(input("Enter second String\n"))

#printing the length of String1
print("length of first string by concatenating them ",lengthOfString1(string1,String2))

#printing the length of String2
print("length of second string by concatenating them ",LengthofString2(String1,String2))
