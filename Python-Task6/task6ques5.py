# defining function for counting number of words in the string
def noOfwordsInString(givenString):
   
   #using split storing each word in the list , so length of list will give number of words in string
   return(len(givenString.split()))

# taking string input from user
givenString=str(input("Enter the string"))
print("no of words in string ",noOfwordsInString(givenString))
