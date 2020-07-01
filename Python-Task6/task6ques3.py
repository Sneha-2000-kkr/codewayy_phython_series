
# Defining function for counting upper and lower case letters in the  string
def countUpperLowerCase(stringGiven):
    
    #initlizing value for count for upper and lower case to zero
    countUpper = 0
    countLower= 0
    
    # Checking for upper cases and incrementing the counter variable accordingly 
    for i in stringGiven:
        if (i.isupper()):
            countUpper = countUpper + 1
    print(countUpper)
    
    # Checking for lower cases and incrementing the counter variable accordingly
    for i in stringGiven:
        if(i.islower()):
            countLower = countLower+1
    print(countLower)
    
 # Taking string input from the user   
stringGiven=str(input("enter the string"))
countUpperLowerCase(stringGiven)
